# Blog Service API – FastAPI + JWT + SQLAlchemy

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-00bf7b?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)](https://python.org)
[![Traceability](https://img.shields.io/badge/Traceability-100%25-success?style=for-the-badge)](#traceability-matrix)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

A **production-ready** blog backend with user authentication, ownership control, pagination, full testing & **100% requirement traceability**.

## Features
- Register / Login with JWT authentication
- CRUD blog posts (owner-only update/delete)
- Public post listing with pagination
- Auto-generated Swagger UI & ReDoc
- Proper HTTP status codes & error handling
- 100% test coverage + traceability matrix

## Live Documentation (when running)
- **Swagger UI** → http://localhost:8000/docs  
- **ReDoc** → http://localhost:8000/redoc

## Quick Start (< 2 minutes)

```bash
git clone https://github.com/ritikkuril/blog-service-fastapii.git
cd blog-service-fastapii

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Server starts at: http://localhost:8000

## API Endpoints

### Authentication
| Endpoint          | Method | Description                  | Auth Required |
|-------------------|--------|------------------------------|----------------|
| `/auth/register`  | POST   | Register new user            | No             |
| `/auth/login`     | POST   | Login → get JWT token        | No             |

### Blogs
| Endpoint                | Method | Description                  | Auth Required    |
|-------------------------|--------|------------------------------|------------------|
| `/blogs/create`         | POST   | Create new blog              | Yes              |
| `/blogs/`               | GET    | Get all blogs (paginated)    | No               |
| `/blogs/{id}`           | GET    | Get blog by ID               | No               |
| `/blogs/update/{id}`    | PUT    | Update own blog              | Yes (Owner only) |
| `/blogs/delete/{id}`    | DELETE | Delete own blog              | Yes (Owner only) |

## Screenshots

**Register**  
![Register User](https://github.com/user-attachments/assets/ee630358-8f67-406d-85d4-7c27fe9b5fec)

**Login**  
![Login](https://github.com/user-attachments/assets/0473b86b-ab0b-40c3-8f5e-aca58498fca7)

**Swagger UI**  
![Swagger UI](https://github.com/user-attachments/assets/28c157af-11e8-4af9-902f-b3a821b86256)

**Blog Operations**  
![Blog CRUD](https://github.com/user-attachments/assets/b88523d7-67c8-48df-a3b5-f0bb5fdd7c40)

## Traceability Matrix (100% Coverage)

| ID     | Requirement                            | Endpoint                | Method  | Status  | Notes                     |
|--------|----------------------------------------|-------------------------|---------|---------|---------------------------|
| REQ001 | User registration                      | `/auth/register`        | POST    | Passed  | Password hashed           |
| REQ002 | User login with JWT                    | `/auth/login`           | POST    | Passed  | Returns access_token      |
| REQ003 | Create blog (authenticated)            | `/blogs/create`         | POST    | Passed  | Owner auto-assigned       |
| REQ004 | List all blogs                         | `/blogs/`               | GET     | Passed  | skip/limit support        |
| REQ005 | Get single blog                        | `/blogs/{id}`           | GET     | Passed  | 404 if not found          |
| REQ006 | Update own blog                        | `/blogs/update/{id}`    | PUT     | Passed  | 403 if not owner          |
| REQ007 | Delete own blog                        | `/blogs/delete/{id}`    | DELETE  | Passed  | 403 if not owner          |
| REQ008 | Proper HTTP status codes               | All                     | -       | Passed  | 200/201/401/403/404       |
| REQ009 | Interactive API documentation          | `/docs`, `/redoc`       | GET     | Passed  | Auto-generated            |



## Project Structure
├── app/
│   ├── main.py
│   ├── routers/
│   ├── models/
│   ├── schemas/
│   ├── database.py
│   └── dependencies.py
├── tests/
├── requirements.txt
└── README.md
