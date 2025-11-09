# 🚗 Vehicle Management API

A simple Django REST Framework API for managing **cars** and **bikes**, using **PostgreSQL** and deployed on **Render**.

---

## 🧠 Features

- CRUD operations for **Cars** and **Bikes**  
- RESTful endpoints with **versioned structure** (`/api/v1/`)  
- **PostgreSQL** database integration  
- **Django Admin** dashboard for easy data management  
- Clean **Model–Serializer–View** architecture  
- Deployed on **Render** using Gunicorn  
- Lightweight and easy to extend for new vehicle types

---

## ⚙️ Tech Stack

- **Backend:** Django 5.2 + Django REST Framework  
- **Database:** PostgreSQL  
- **Server:** Gunicorn  
- **Deployment:** Render  
- **Language:** Python 3.x  

---

## 🌐 Live Demo

🔗 **Base URL:**  
[https://vehicle-management-api-j125.onrender.com/](https://vehicle-management-api-j125.onrender.com/)

Example Response:
```json
{
  "status": "ok",
  "message": "Welcome to the Vehicle Management API 🚗",
  "available_endpoints": [
    "/api/v1/vehicle/cars/",
    "/api/v1/vehicle/bikes/"
  ]
}

---

## 🧰 Setup

```bash
# 1️⃣ Clone the repository
git clone https://github.com/mopy7/vehicle-management-api.git
cd vehicle-management-api

# 2️⃣ Create and activate a virtual environment
python -m venv venv
source venv/bin/activate     # (Linux/macOS)
venv\Scripts\activate        # (Windows)

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Apply migrations
cd src/core
python manage.py migrate

# 5️⃣ Run the development server
python manage.py runserver

Access locally at:
👉 http://127.0.0.1:8000/

---

## 🧩 API Endpoints

| Endpoint | Method | Description |
|-----------|--------|-------------|
| `/api/v1/vehicle/cars/` | GET, POST | List all cars or create a new car |
| `/api/v1/vehicle/cars/<id>/` | GET, PUT, DELETE | Retrieve, update, or delete a car |
| `/api/v1/vehicle/bikes/` | GET, POST | List all bikes or create a new bike |
| `/api/v1/vehicle/bikes/<id>/` | GET, PUT, DELETE | Retrieve, update, or delete a bike |

---

## 🧑‍💻 Author

**Mopy**  
🔗 [GitHub Profile](https://github.com/mopy7)  
💬 “Miles to go before I sleep...”

---
