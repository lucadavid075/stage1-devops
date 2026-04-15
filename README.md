# HNG Stage 1 DevOps Tasks

## Project Description

This is a simple REST API built using FastAPI and deployed on a Linux server using Nginx as a reverse proxy.

The project demonstrates how to build and deploy a production-ready API with process management using systemd and secure HTTPS configuration.

## How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/lucadavid075/stage1-devops.git
cd stage1-devops
```

### 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate


### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the application
uvicorn main:app --host 0.0.0.0 --port 8000

## API Endpoints

### GET /

Returns a message confirming the API is running.

Test locally:

curl http://127.0.0.1:8000/

**Response:**
```json
{
  "message": "API is running"
}
```

GET /health

Returns the health status of the API.

Test locally:

curl http://127.0.0.1:8000/health

**Response:**
```json
{
  "message": "healthy"
}
```

GET /me

Returns user information.

Test locally:

curl http://127.0.0.1:8000/

**Response:**
```json
{
  "name": "David Luke",
  "email": "daiveedlucas049@gmail.com",
  "github": "https://github.com/lucadavid075"
}```

## Live Deployment

The API is publicly accessible at:

https://hngdevops-david.duckdns.org