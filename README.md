
# Auth API

A RESTful API for handling authentication and user management, designed for easy integration and deployment. This guide provides step-by-step instructions for setting up the project locally and using Docker, along with sample `curl` commands to test the API.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
  - [User Registration](#user-registration)
  - [User Login](#user-login)
  - [Profile Information](#profile-information)
- [Example Curl Commands](#example-curl-commands)
- [Configuration](#configuration)

---

## Prerequisites

Ensure you have the following installed:
- **Pyhton** 
- **Django** 
- **Postman** (optional, for testing API endpoints)

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/abhay-2789/auth-api.git
   cd auth-api
   ```

2. **Set up environment variables**:
   - Create a Venv and install the requriments.
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
   
3. **Run the server**:
```
pyhton manage.py runserver
```
   

The server should now be running on `http://localhost:8000` by default.

## API Endpoints

### 1. User Registration
- **URL**: `/api/register`
- **Method**: `POST`
- **Body**: 
  - `username` (string)
  - `email` (string)
  - `password` (string)

### 2. User Login
- **URL**: `/api/login`
- **Method**: `POST`
- **Body**:
  - `email` (string)
  - `password` (string)

### 3. Profile Information
- **URL**: `/api/profile`
- **Method**: `GET`
- **Headers**:
  - `Authorization`: `Bearer <token>`

---

## Example Curl Commands

### Register a New User
```bash
curl -X POST http://localhost:3000/api/register   -H "Content-Type: application/json"   -d '{"username": "newuser", "email": "newuser@example.com", "password": "password123"}'
```

### Log in as a User
```bash
curl -X POST http://localhost:3000/api/login   -H "Content-Type: application/json"   -d '{"email": "newuser@example.com", "password": "password123"}'
```

### Access User Profile (Requires Token)
Replace `<token>` with the JWT token received from the login endpoint.
```bash
curl -X GET http://localhost:3000/api/profile   -H "Authorization: Bearer <token>"
```






