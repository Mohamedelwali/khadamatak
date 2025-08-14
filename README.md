# 🚀 Khadamatak

[![Django](https://img.shields.io/badge/Django-REST_Framework-green?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![React](https://img.shields.io/badge/React-18-blue?style=flat-square&logo=react)](https://react.dev/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?style=flat-square&logo=postgresql)](https://www.postgresql.org/)

**Khadamatak** is a platform that connects customers with service providers across various fields.  
It allows users to search, book services, leave reviews, and mark favorites, with support for Arabic and English (RTL included).

---

## 📌 Table of Contents
- [About](#about)
- [Features](#features)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Environment Variables](#environment-variables)
- [License](#license)

---

## 📖 About
Khadamatak makes it easier for customers to connect with service providers by offering:
- Search by location and category
- Online booking system
- Ratings and reviews
- Favorites system
- Multi-language support with Arabic RTL

---

## ✨ Features

### Backend (Django REST Framework)
- JWT Authentication (Login, Register, Token Refresh)
- User roles: Customer & Service Provider
- CRUD operations for service categories & listings
- Booking system with status tracking
- Reviews & favorites
- Service area support using GeoJSON

### Frontend (React)
- Fully responsive design
- Multi-language support (Arabic/English) with i18next
- Authentication & protected routes
- Search with filters & map view
- Service provider dashboard
- Customer dashboard

---

## 📂 Project Structure
```

Khadamatak/
│
├── backend/               # Django REST Framework backend
│   ├── khadamatak/         # Project settings
│   ├── accounts/           # Authentication & user profiles
│   ├── services/           # Services & categories
│   ├── bookings/           # Booking system
│   ├── reviews/            # Reviews & favorites
│   ├── core/               # Shared utilities
│   ├── requirements.txt
│   └── manage.py
│
├── frontend/               # React frontend
│   ├── public/
│   ├── src/
│   │   ├── api/            # Axios instance
│   │   ├── assets/         # Images & icons
│   │   ├── components/     # UI components
│   │   ├── context/        # Global state
│   │   ├── hooks/          # Custom hooks
│   │   ├── i18n/           # Translations
│   │   ├── pages/          # Page views
│   │   ├── routes/         # App routes
│   │   ├── styles/         # Global styles
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json
│   └── README.md
│
├── .gitignore
└── README.md               # This file

````

---

## 🛠 Tech Stack
**Backend:**
- Django REST Framework
- Simple JWT
- PostgreSQL + PostGIS

**Frontend:**
- React
- React Router DOM
- Axios
- i18next

---

## ⚙ Installation & Setup

### Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate   # On Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
````

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

---

## 🔑 Environment Variables

### Backend (.env)

```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```

### Frontend (.env)

```
REACT_APP_API_URL=http://localhost:8000/api
```

---

## 📄 License

This project is open-source and free to use under the MIT License.