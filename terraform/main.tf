terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region  = var.aws_region
}

#найсвіжіша Ubuntu LTS автоматично
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"] #канон

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"]
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

#ssh для доступу
resource "tls_private_key" "pk" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "kp" {
  key_name   = "${var.project_name}-key"
  public_key = tls_private_key.pk.public_key_openssh
}

#зберіг приватний ключ у папку ansible (щоб могли зайти на сервер)
resource "local_file" "ssh_key" {
  filename        = "../ansible/vertex-key.pem"
  content         = tls_private_key.pk.private_key_pem
  file_permission = "0400" # тільки читання власнику (вимога SSH)
}

#firewall(secgroup)
resource "aws_security_group" "web_sg" {
  name        = "${var.project_name}-sg"
  description = "Allow SSH and HTTP"

  #ssh
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  #djangoweb(8000)
  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  #http(80) - на майбутнє (nginx)
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  #дозвіл серверам виходити в інтернет качати оновлення
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

#ec2
resource "aws_instance" "app_server" {
  count         = var.instance_count
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type
  key_name      = aws_key_pair.kp.key_name
  
  vpc_security_group_ids = [aws_security_group.web_sg.id]

  tags = {
    Name = "${var.project_name}-vm-${count.index + 1}"
  }
}

#файл інвентарю ansible
resource "local_file" "ansible_inventory" {
  filename = "../ansible/inventory.ini"
  content = templatefile("${path.module}/inventory.tpl", {
    ip_addrs = aws_instance.app_server[*].public_ip
    ssh_key  = "./vertex-key.pem"
  })
}

#стара локалка
# provider "docker" {}

# resource "docker_image" "nginx" {
#   name         = "nginx:latest"
#   keep_locally = false
# }

# resource "docker_container" "nginx" {
#   count = var.container_count
#   image = docker_image.nginx.image_id
#   name  = "${var.container_name}-${count.index + 1}"
  
#   ports {
#     internal = 80
#     external = 8000 + count.index # Порти 8000 і 8001
#   }
# }

#
# resource "local_file" "inventory" {
#   content = templatefile("inventory.tpl", {
#     containers = docker_container.nginx
#   })
#   filename = "./inventory"
# }