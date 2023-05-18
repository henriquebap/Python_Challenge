import re
from passlib.hash import bcrypt

class User:
    def __init__(self, first_name, last_name, cpf, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.cpf = cpf
        self.email = email
        self.password = password
        self.bikes = []


    users = []

    def hash_password(self):
        self.password = bcrypt.hash(self.password)
        
    def verify_password(self, password):
        return bcrypt.verify(password, self.password)

def login(users):
    id_mail = input("Digite o seu email: ")
    id_password = input("Digite a senha: ")
    for user in users:
         if user.email == id_mail and user.verify_password(id_password):
            return user
    print("A senha ou email estao incorretos")
    return None

def remove_user(users):#testar fun
    email = input("Digite o email do usuário a ser removido: ")
    id_password = input("Digite a Senha do usuario: ")
    for user in users:
        if user.email == email and user.verify_password(id_password):
            users.remove(user)
            print("Usuário removido com sucesso.")
            return
    print("O usuário não foi encontrado.")

def cadastro_user(users):
    while True:
        first_name = input("Digite seu primeiro nome: ")
        if not first_name.isalpha():
            print("Por favor, digite apenas letras.")
            continue
        first_name = re.sub(r'[^a-zA-Z]', '', first_name)
        break

    while True:
        last_name = input("Digite seu sobrenome: ")
        if not last_name.isalpha():
            print("Por favor, digite apenas letras.")
            continue
        last_name = re.sub(r'[^a-zA-Z]', '', last_name)
        break

    while True:
        cpf = input("Digite o seu CPF: ")
        if not cpf.isdigit() or len(cpf) != 11:
            print("CPF inválido. Verifique a quantidade de dígitos.")
            continue
        else:
            cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            break

    while True:
        email = input("Digite o seu email: ").lower()#testar o re
        padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(padrao, email):
            print("Porfavor verifique o formato do seu email")
            continue
        else:
            break

    while True:
        id_password = input("Crie uma Senha: ")
        id_input = input("Digite a sua senha novamente para verificar: ")
        if id_password != id_input:
            print("As senhas não correspondem. Tente novamente.")
            continue

        user = User(first_name, last_name, cpf, email, id_password)
        user.hash_password()
        users.append(user)
        print("Usuário cadastrado com sucesso.")
        return user
