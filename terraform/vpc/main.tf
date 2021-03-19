provider "aws" {
    region = "us-west-2"
    profile = "ADD_YOUR_AWS_PROFLE_HERE"
}


#create a VPC
resource "aws_vpc" "prod-vpc" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "prod-vpc"
  }
}

#create IGW
resource  "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.prod-vpc.id
  tags = {
    Name = "Prod-gw"
  }
}

# create route table
resource "aws_route_table" "Prod-rt" {
  vpc_id = aws_vpc.prod-vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }

  route {
    ipv6_cidr_block        = "::/0"
    gateway_id = aws_internet_gateway.gw.id
  }

  tags = {
    Name = "rt-Prod"
  }
}

#create a subnet
resource "aws_subnet" "prod_subnet"{
  vpc_id = aws_vpc.prod-vpc.id
  availability_zone = "us-west-2a"
  cidr_block = "10.0.1.0/24"
  tags = {
    Name = "prod_subnet"
  }

}
# subnet association
resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.prod_subnet.id 
  route_table_id = aws_route_table.Prod-rt.id
}

#SGs
resource "aws_security_group" "allow_tls" {
  name        = "allow_tls"
  description = "Allow TLS inbound traffic"
  vpc_id      = aws_vpc.prod-vpc.id

  ingress {
    description = "TLS from VPC"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    description = "TLS from VPC"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    description = "TLS from VPC"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "allow_tls"
  }
}

# ENI
resource "aws_network_interface" "webserver-nic" {
  subnet_id       = aws_subnet.prod_subnet.id
  private_ips     = ["10.0.1.50"]
  security_groups = [aws_security_group.allow_tls.id]

}

#EIP
resource "aws_eip" "one" {
  vpc                       = true
  network_interface         = aws_network_interface.webserver-nic.id
  associate_with_private_ip = "10.0.1.50"
  depends_on = [aws_internet_gateway.gw]
}

#ec2
resource "aws_instance" "prod_ec2" {
  ami           = "ami-0528a5175983e7f28"
  instance_type = "t2.micro"
  subnet_id = aws_subnet.prod_subnet.id
  availability_zone = "us-west-2a"
  key_name = "TerraformKey.pem"
  network_interface {
    device_index = 0
    network_interface_id = aws_network_interface.webserver-nic.id
  }
  user_data = <<-EOF
            #!/bin/bash
            sudo yum update -y 
            sudo yum install apache2 -y
            sudo systemctl start apache2
            sudo bash -c 'echo Hi there! > /var/www/html/index.html'
            EOF
  tags = {
    Name = "prod_ec2"
  }
}