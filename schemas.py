from pydantic import BaseModel, EmailStr

# user schemas
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

#doctor schema
class DoctorOut(BaseModel):
    id: int
    name: str
    specialization: str

    class Config:
        from_attributes = True

# patient schema
class PatientOut(BaseModel):
    id: int
    name: str
    age: int

    class Config:
        from_attributes = True


# appointment schema
class AppointmentOut(BaseModel):
    id: int
    doctor_id: int
    patient_id: int
    appointment_time: str
    status: str

    class Config:
        from_attributes = True