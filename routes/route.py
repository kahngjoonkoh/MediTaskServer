from fastapi import APIRouter

from models.appointments import Appointments
from config.database import collection_name
from schema.schemas import list_serial, single_serial
from bson import ObjectId

router = APIRouter()


# Create New Appointment
@router.post("/appointments")
async def create_appointment(appointment: Appointments):
    collection_name.insert_one(dict(appointment))


# List All Appointments
@router.get("/appointments")
async def get_all_appointments():
    appointments_list = list_serial(collection_name.find())
    return appointments_list


# View Specific Appointment
@router.get("/appointments/{id}")
async def get_single_appointment(id):
    appointment = single_serial(collection_name.find_one({"_id": ObjectId(id)}))
    return appointment


# Cancel Appointment
@router.delete("/appointments/{id}")
async def delete_single_appointment(id):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
