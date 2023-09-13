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
            "bikes": [str(bike) for bike in self.bikes]
        }


#funcao hash_password para salvar a password + hash
    def hash_password(self):
        self.password = bcrypt.hash(self.password)
#funcao de verificacao da senha usando bcrypt
    def verify_password(self, password):
        return bcrypt.verify(password, self.password)