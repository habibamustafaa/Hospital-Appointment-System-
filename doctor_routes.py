from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import json
from app.dependencies import get_db
from app.models import Doctor
from app.services.security import admin_required
from app.services.cache_service import get_cache, set_cache
from app.schemas import DoctorOut
from app.logger import logger

router = APIRouter()

# create doctor (admin only)
@router.post("/doctors")
def create_doctor(
    name: str,
    specialization: str,
    db: Session = Depends(get_db),
    user=Depends(admin_required)
):

    doctor = Doctor(name=name, specialization=specialization)

    db.add(doctor)
    db.commit()

    set_cache("doctors", None)

    logger.info("Doctor created")

    return {"message": "Doctor created"}


# get all doctors
@router.get("/doctors", response_model=list[DoctorOut])
def get_doctors(db: Session = Depends(get_db)):

    cached = get_cache("doctors")
    if cached:
        return json.loads(cached)

    doctors = db.query(Doctor).all()

    set_cache(
        "doctors",
        json.dumps([{"id": d.id, "name": d.name, "specialization": d.specialization} for d in doctors])
    )

    return doctors


# get doctor by id
@router.get("/doctors/{doctor_id}", response_model=DoctorOut)
def get_doctor(doctor_id: int, db: Session = Depends(get_db)):

    doc = db.query(Doctor).filter(Doctor.id == doctor_id).first()

    if not doc:
        raise HTTPException(status_code=404)

    return doc



# update doctor (admin only)
@router.put("/doctors/{doctor_id}")
def update_doctor(
    doctor_id: int,
    name: str,
    specialization: str,
    db: Session = Depends(get_db),
    user=Depends(admin_required)
):

    doc = db.query(Doctor).filter(Doctor.id == doctor_id).first()

    if not doc:
        raise HTTPException(status_code=404)

    doc.name = name
    doc.specialization = specialization

    db.commit()
    set_cache("doctors", None)

    logger.info("Doctor updated")

    return {"message": "Updated"}


# delete doctor (admin only)
@router.delete("/doctors/{doctor_id}")
def delete_doctor(
    doctor_id: int,
    db: Session = Depends(get_db),
    user=Depends(admin_required)
):

    doc = db.query(Doctor).filter(Doctor.id == doctor_id).first()

    if not doc:
        raise HTTPException(status_code=404)

    db.delete(doc)
    db.commit()

    set_cache("doctors", None)

    logger.info("Doctor deleted")

    return {"message": "Deleted"}