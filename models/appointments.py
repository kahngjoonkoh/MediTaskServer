from pydantic import BaseModel


class Appointments(BaseModel):
    patient_name: str
    doctor_name: str
    date: str
    time: str
