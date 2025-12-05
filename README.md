# FastAPI Project

A modern FastAPI application with automatic interactive documentation (Swagger UI).

## Quick Setup & Run (One-Time)

```bash
# 1. Clone the project (if using git)
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

# 2. Create virtual environment
python -m venv venv
# or on macOS/Linux: python3 -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the app with auto-reload
uvicorn app.main:app --reload
```

Server will be available at: http://localhost:8000
Interactive API Documentation (Swagger UI)
Open your browser and go to:
http://localhost:8000/docs

Project Structure

| Endpoint         | Method | Description             |
| ---------------- | ------ | ----------------------- |
| `/auth/register` | POST   | Register a new user     |
| `/auth/login`    | POST   | Login and get JWT token |


| Endpoint             | Method | Description       |
| -------------------- | ------ | ----------------- |
| `/blogs/create`      | POST   | Create a new blog |
| `/blogs/`            | GET    | Get all blogs     |
| `/blogs/{id}`        | GET    | Get blog by ID    |
| `/blogs/update/{id}` | PUT    | Update a blog     |
| `/blogs/delete/{id}` | DELETE | Delete a blog     |





