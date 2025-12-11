# variables.tf

variable "aws_region" {
  description = "aws region"
  type        = string
}

variable "project_name" {
  description = "project name"
  type        = string
}

variable "instance_count" {
  description = "number of ec2"
  type        = number
}

variable "instance_type" {
  description = "ec2 type"
  type        = string
}