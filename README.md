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

Project ScreenShots---------------------------------------
Register----------
<img width="1492" height="692" alt="image" src="https://github.com/user-attachments/assets/ee630358-8f67-406d-85d4-7c27fe9b5fec" />
Login--------------
<img width="1587" height="759" alt="image" src="https://github.com/user-attachments/assets/0473b86b-ab0b-40c3-8f5e-aca58498fca7" />
<img width="695" height="621" alt="image" src="https://github.com/user-attachments/assets/28c157af-11e8-4af9-902f-b3a821b86256" />

<img width="1375" height="493" alt="image" src="https://github.com/user-attachments/assets/b88523d7-67c8-48df-a3b5-f0bb5fdd7c40" />








