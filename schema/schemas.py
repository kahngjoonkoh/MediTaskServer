# Serializing functions
def single_serial(appointment) -> dict:
    return {
        "id": str(appointment["_id"]),
        "patient_name": appointment["patient_name"],
        "doctor_name": appointment["doctor_name"],
        "date": appointment["date"],
        "time": appointment["time"],
    }


def list_serial(appointments) -> list:
    return [single_serial(appointment) for appointment in appointments]
