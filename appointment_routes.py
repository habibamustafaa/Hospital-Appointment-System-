from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models import Appointment
from app.services.security import patient_required, doctor_required, admin_required
from app.schemas import AppointmentOut
from app.logger import logger

router = APIRouter()

#book appointment patientt
@router.post("/appointments")
def book_appointment(
    doctor_id: int,
    patient_id: int,
    appointment_time: str,
    db: Session = Depends(get_db),
    user=Depends(patient_required)
):

    existing = db.query(Appointment).filter(
        Appointment.doctor_id == doctor_id,
        Appointment.appointment_time == appointment_time
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Doctor already booked")

    appointment = Appointment(
        doctor_id=doctor_id,
        patient_id=patient_id,
        appointment_time=appointment_time,
        status="Scheduled"
    )

    db.add(appointment)
    db.commit()

    logger.info("Appointment booked")

    return {"message": "Appointment booked"}


# get all appointments (admin onlyyy)
@router.get("/appointments", response_model=list[AppointmentOut])
def get_all_appointments(
    db: Session = Depends(get_db),
    user=Depends(admin_required)
):
    return db.query(Appointment).all()


# doctor view of appointments
@router.get("/appointments/doctor/{doctor_id}")
def doctor_appointments(
    doctor_id: int,
    db: Session = Depends(get_db),
    user=Depends(doctor_required)
):
    return db.query(Appointment).filter(Appointment.doctor_id == doctor_id).all()


# patient view of appointmentss
@router.get("/appointments/patient/{patient_id}")
def patient_appointments(
    patient_id: int,
    db: Session = Depends(get_db),
    user=Depends(patient_required)
):
    return db.query(Appointment).filter(Appointment.patient_id == patient_id).all()


# update status (doctor only)
@router.put("/appointments/{id}/status")
def update_status(
    id: int,
    status: str,
    db: Session = Depends(get_db),
    user=Depends(doctor_required)
):

    appt = db.query(Appointment).filter(Appointment.id == id).first()

    if not appt:
        raise HTTPException(status_code=404, detail="Not found")

    appt.status = status
    db.commit()

    logger.info("Appointment status updated")

    return {"message": "Updated"}


# cancel appointment (admin only)
@router.delete("/appointments/{id}")
def cancel_appointment(
    id: int,
    db: Session = Depends(get_db),
    user=Depends(admin_required)
):

    appt = db.query(Appointment).filter(Appointment.id == id).first()

    if not appt:
        raise HTTPException(status_code=404)

    db.delete(appt)
    db.commit()

    logger.info("Appointment cancelled")

    return {"message": "Cancelled"}