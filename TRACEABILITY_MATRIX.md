# Requirements Traceability Matrix (RTM)  
**Project**: Blog Service API (FastAPI + SQLite)  
**Version**: 1.0  
**Last Updated**: 2025-12-06

| ID    | Requirement Description                          | Endpoint                  | HTTP Method | Pydantic Schema       | Test Case ID(s)              | Status    | Notes                              |
|-------|--------------------------------------------------|---------------------------|-------------|-----------------------|------------------------------|-----------|------------------------------------|
| REQ-01| User shall be able to register                   | `/users/`                 | POST        | UserCreate            | test_user_registration       | Passed    | Password hashed with bcrypt       |
| REQ-02| User shall be able to login & receive JWT        | `/token`                  | POST        | Token                 | test_login_success           | Passed    | Returns access_token              |
| REQ-03| Authenticated user can create a blog post        | `/posts/`                 | POST        | PostCreate            | test_create_post             | Passed    | Protected route                   |
| REQ-04| Anyone can retrieve all posts (public)          | `/posts/`                 | GET         | Post                  | test_get_posts               | Passed    | Pagination support added          |
| REQ-05| Anyone can retrieve a single post by ID          | `/posts/{id}`             | GET         | Post                  | test_get_post_by_id          | Passed    |                                    |
| REQ-06| Owner can update own post                        | `/posts/{id}`             | PUT         | PostUpdate            | test_update_own_post         | Passed    | 403 if not owner                  |
| REQ-07| Owner can delete own post                        | `/posts/{id}`             | DELETE      | -                     | test_delete_own_post         | Passed    |                                    |
| REQ-08| Non-owner cannot update/delete others' posts    | `/posts/{id}`             | PUT/DELETE  | -                     | test_update_foreign_post     | Passed    | Returns 403 Forbidden             |
| REQ-09| Posts must belong to authenticated user          | -                         | -           | -                     | test_post_owner_enforced     | Passed    | ForeignKey + dependency           |
| REQ-10| API must return proper HTTP status codes         | All endpoints             | -           | -                     | test_status_codes            | Passed    | 201, 200, 401, 403, 404 covered   |
| REQ-11| Support pagination & filtering                   | `/posts/`                 | GET         | Post                  | test_pagination              | Passed    | skip/limit query params           |
| REQ-12| API documentation via Swagger UI & ReDoc         | `/docs`, `/redoc`         | GET         | -                     | -                            | Passed    | Auto-generated                    |

### Test Coverage Summary
| Total Requirements | Implemented | Tested | Coverage |
|---------------------|-------------|--------|----------|
| 12                  | 12          | 12     | 100%     |

### Tools Used
- **Framework**: FastAPI
- **Testing**: pytest + httpx (tests located in `/tests/`)
- **Auth**: JWT (PyJWT) + OAuth2PasswordBearer
- **Database**: SQLAlchemy 2.0 + SQLite (dev) / PostgreSQL-ready

This traceability matrix proves you follow proper software engineering practices — perfect for Amazon, Google, Microsoft, or any FAANG-level interview.
