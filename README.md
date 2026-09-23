
# Dockerized Flask DevOps Project

![Flask Docker CI](https://github.com/chinmmayipedapati/docker-flask-devops/actions/workflows/ci.yml/badge.svg)
A Python Flask web application containerized using
Docker and managed using Docker Compose.

## Technologies Used

- Python
- Flask
- Docker
- Docker Compose
- Ubuntu WSL 2
- Git and GitHub

## Features

- Containerized Flask web application
- Docker Compose configuration
- Application health-check endpoint
- Port mapping for local development

## Run the Application

Clone the repository:

git clone https://github.com/chinmmayipedapati/docker-flask-devops.git

Navigate to the project:

cd docker-flask-devops

Build and start the application:

docker compose up -d --build

Open your browser:

http://localhost:5000

Health check:

http://localhost:5000/health

## Author

Chinmmayi Pedapati

GitHub: https://github.com/chinmmayipedapati