from fastapi import FastAPI
from app.database import Base, engine
from app.models import User, Doctor, Patient, Appointment
from app.routes.auth_routes import router as auth_router
from app.routes.doctor_routes import router as doctor_router
from app.routes.patient_routes import router as patient_router
from app.routes.appointment_routes import router as appointment_router
from app.monitor import router as monitor_router

# create database tables
Base.metadata.create_all(bind=engine)

# create FastAPI app
app = FastAPI(
    title="Hospital Appointment System",
    description="Backend system for managing hospital appointments",
    version="1.0"
)

#register routes
app.include_router(auth_router)
app.include_router(doctor_router)
app.include_router(patient_router)
app.include_router(appointment_router)
app.include_router(monitor_router)


# health check route
@app.get("/")
def home():
    return {
        "message": "Hospital Appointment System API is running"
    }