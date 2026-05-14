from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models import Patient
from app.services.security import admin_required
from app.schemas import PatientOut
from app.logger import logger

router = APIRouter()

# create patient (admin only)
@router.get("/patients", response_model=list[PatientOut])
def get_patients(
    db: Session = Depends(get_db),
    user=Depends(admin_required)
):
    return db.query(Patient).all()


# get patient by id (admin onlyyy)
@router.get("/patients/{patient_id}", response_model=PatientOut)
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    user=Depends(admin_required)
):

    patient = db.query(Patient).filter(Patient.id == patient_id).first()

    if not patient:
        raise HTTPException(status_code=404)

    return patient