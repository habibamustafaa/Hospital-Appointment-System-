Hospital Appointment System

A backend system built using FastAPI for managing hospital appointments between patients and doctors. The system supports authentication, role-based authorization, appointment scheduling, caching, logging, and API testing.

Project Idea

The purpose of this project is to help hospitals manage:

Doctors
Patients
Appointments

The system allows:

Patients to book appointments
Doctors to manage appointment status
Admins to manage doctors and patients

The project follows RESTful API principles and uses JWT authentication for security.

Technologies Used
Python
FastAPI
SQLite
SQLAlchemy
Pydantic
JWT Authentication
Redis
Pytest
Uvicorn
Features
Authentication
User Registration
User Login
JWT Token Generation
Protected Routes
Role-Based Authorization
Admin
Manage doctors
Manage patients
Delete appointments
Doctor
View appointments
Update appointment status
Patient
Book appointments
Cancel appointments
View personal appointments
Appointment Features
Book appointments
Cancel appointments
Prevent double booking
View schedules
Update appointment status:
Scheduled
Completed
Cancelled
Project Structure
hospital_appointment_system/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── config.py
│   ├── dependencies.py
│
│   ├── models/
│   ├── schemas/
│   ├── routes/
│   ├── services/
│   ├── tests/
│
│   ├── logger.py
│   └── monitor.py
│
├── requirements.txt
├── .env
├── README.md
├── Dockerfile
└── docker-compose.yml
Database Tables
Users

Stores:

username
email
password
role
Doctors

Stores:

doctor name
specialization
Patients

Stores:

patient name
age
Appointments

Stores:

doctor_id
patient_id
appointment_time
status
API Endpoints
Authentication
Method	Endpoint	Description
POST	/auth/register	Register user
POST	/auth/login	Login user
Doctors
Method	Endpoint
GET	/doctors
GET	/doctors/{id}
POST	/doctors
PUT	/doctors/{id}
DELETE	/doctors/{id}
Patients
Method	Endpoint
GET	/patients
GET	/patients/{id}
Appointments
Method	Endpoint
POST	/appointments
GET	/appointments
GET	/appointments/doctor/{id}
GET	/appointments/patient/{id}
PUT	/appointments/{id}/status
DELETE	/appointments/{id}
Setup Instructions
1. Clone Repository
git clone <repository_link>
cd hospital_appointment_system
2. Create Virtual Environment
python -m venv venv

Activate:

Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate
3. Install Requirements
pip install -r requirements.txt
4. Create .env File
SECRET_KEY=mysecretkey123
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

DATABASE_URL=sqlite:///./hospital.db

REDIS_HOST=localhost
REDIS_PORT=6379
5. Run Project
uvicorn app.main:app --reload
Swagger Documentation

Open:

http://127.0.0.1:8000/docs
Redis Caching

Redis is used to cache frequently accessed doctor data to improve performance.

Implemented:

GET all doctors caching
Cache invalidation after updates
Logging

The project uses Python logging to log:

User registration/login
Appointment actions
Errors and exceptions
API Testing

Testing is implemented using:

pytest
FastAPI TestClient

Tests include:

Authentication testing
Protected routes testing
Appointment testing

Run tests:

pytest
Docker (Bonus)

The project supports Docker using:

Dockerfile
docker-compose

Run using:

docker-compose up --build
Team Members Tasks
Member 1

Authentication and Security

Member 2

Doctor Management + Caching

Member 3

Patient Management

Member 4

Appointment Management

Member 5

Testing, Logging, Monitoring, Docker

Future Improvements
Frontend integration
Email notifications
Better dashboard analytics
PostgreSQL integration
