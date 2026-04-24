# 🛒 CityShop – DRF E-commerce API

CityShop is a backend e-commerce REST API built using **Django REST Framework (DRF)**.  
It provides core e-commerce functionalities such as product management, category organization, cart handling, and order processing.

The project also includes **JWT authentication** and **interactive API documentation**.

---

## 🚀 Features

- 🔐 JWT Authentication (Djoser)
- 📦 Product Management
- 🗂️ Category Management
- 🛒 Cart System
- 📑 Order Processing
- 📖 Swagger API Documentation (drf-yasg)
- 🧩 Modular & Scalable Architecture

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Authentication:** JWT (Djoser)
- **Documentation:** drf-yasg (Swagger UI)
- **Database:** SQLite / PostgreSQL

---


---

## 🔑 Authentication

CityShop uses **JWT (JSON Web Tokens)** for secure authentication.

### Auth Endpoints

- `POST /auth/jwt/create/` → Get access & refresh token
- `POST /auth/jwt/refresh/` → Refresh access token
- `POST /auth/users/` → Register user

---

## 📦 API Endpoints

### 🔹 Products

- `GET /products/` → List products  
- `GET /products/{id}/` → Product details  
- `POST /products/` → Create product (Admin)  
- `PATCH /products/{id}/` → Update product  
- `DELETE /products/{id}/` → Delete product  

---

### 🔹 Categories

- `GET /categories/`  
- `POST /categories/`  
- `GET /categories/{id}/`  
- `PATCH /categories/{id}/`  
- `DELETE /categories/{id}/`  

---

### 🛒 Cart

- `POST /carts/` → Create cart  
- `GET /carts/{id}/` → Retrieve cart  
- `POST /carts/{id}/items/` → Add item  
- `PATCH /carts/{id}/items/{item_id}/` → Update item  
- `DELETE /carts/{id}/items/{item_id}/`  

---

### 📑 Orders

- `POST /orders/` → Create order  
- `GET /orders/` → List user orders  
- `GET /orders/{id}/` → Order details  
- `POST /orders/{id}/cancel/` → Cancel order  

---

## 📖 API Documentation

Swagger UI available at:
/swagger/ or
/redoc/


## 👨‍💻 Author

Arman Islam |
CSE Student | Backend Developer