output "server_ips" {
  value = aws_instance.app_server[*].public_ip
}

output "ssh_command" {
  value = "ssh -i ../ansible/vertex-key.pem ubuntu@${aws_instance.app_server[0].public_ip}"
}