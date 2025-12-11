variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "eu-north-1"
}

variable "project_name" {
  description = "project title"
  type        = string
  default     = "vertex-app"
}

variable "instance_type" {
  description = "servet type"
  type        = string
  default     = "t2.micro"
}

variable "instance_count" {
  description = "amount of servers"
  type        = number
  default     = 2
}