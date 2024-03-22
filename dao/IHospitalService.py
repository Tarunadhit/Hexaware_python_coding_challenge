from abc import ABC, abstractmethod
from entity.appointment import Appointment
from typing import List
from util.DBConnection import DBConnection
from datetime import date


class HospitalService:
    def __init__(self):
        pass

    def get_appointment_by_id(self, appointment_id):
        pass

    def get_appointments_for_patient(self, patient_id):
        pass

    def get_appointments_for_doctor(self, doctor_id):
        pass

    def schedule_appointment(self, appointment):
        pass

    def update_appointment(self, date, new_description, appointment_id):
        pass

    def cancel_appointment(self, appointment_id):
        pass
