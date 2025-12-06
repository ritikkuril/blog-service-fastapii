# Requirements Traceability Matrix (RTM)  
**Project**: Blog Service API (FastAPI + SQLite)  
**Version**: 1.0  
**Last Updated**: 2025-12-06

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

### Test Coverage Summary
| Total Requirements | Implemented | Tested | Coverage |
|---------------------|-------------|--------|----------|
| 09                 | 09         | 09     | 100%     |

### Tools Used
- **Framework**: FastAPI
- **Testing**: pytest + httpx (tests located in `/tests/`)
- **Auth**: JWT (PyJWT) + OAuth2PasswordBearer
- **Database**: SQLAlchemy 2.0 + SQLite (dev) 


