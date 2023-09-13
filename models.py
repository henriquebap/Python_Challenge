import re
import os
from passlib.hash import bcrypt

class User:
    def __init__(self, first_name, last_name, cpf, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.cpf = cpf
        self.email = email
        self.password = password
        self.bikes = []

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "cpf": self.cpf,
            "email": self.email,
            "password": self.password,
            "bikes": [bike.to_dict() for bike in self.bikes]
        }

    def hash_password(self):
        self.password = bcrypt.hash(self.password)

    def verify_password(self, password):
        return bcrypt.verify(password, self.password)


class Bike:
    def __init__(self,user, brand, bike_type, serial_number, year, value, additional_modifications):
        self.user = user
        self.brand = brand
        self.bike_type = bike_type
        self.serial_number = serial_number
        self.year = year
        self.value = value
        self.additional_modifications = additional_modifications or []

    def to_dict(self):
        return {
            "brand": self.brand,
            "bike_type": self.bike_type.to_dict(),  # Serializa o objeto BikeType
            "serial_number": self.serial_number,
            "year": self.year,
            "value": self.value,
            "additional_modifications": self.additional_modifications
        }

    def __str__(self):
        modifications = "\n".join(self.additional_modifications) if self.additional_modifications else "Nenhuma modificação adicional"
        return f"Marca: {self.brand}\nModelo: {self.bike_type.name}\nNum de Série: {self.serial_number}\nAno: {self.year}\nPreço: {self.value}\nModificações adicionais:\n{modifications}\n"


class BikeType:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description
        }

def serialize_bike_type(bike_type):
    return bike_type.to_dict()
