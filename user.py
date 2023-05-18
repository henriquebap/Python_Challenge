import re
from passlib.hash import bcrypt

users = []

def login(users):
    id_mail = input("Digite o seu email: ")
    id_password = input("Digite a senha: ")
    for user in users:
         if user['email'] == id_mail and user['password'] == id_password:
            return user
    print("A senha ou email estao incorretos")
    return None

def remove_user(users):
    email = input("Digite o email do usuário a ser removido: ")#PEdir senha para remover
    for user in users:
        if user['email'] == email:
            users.remove(user)
            print("Usuário removido com sucesso.")
            return
    print("O usuário não foi encontrado.")

def hash_id(id_password):
    hashed_id = bcrypt.hash(id_password)
    return hashed_id
def verify_id(id_password, hashed_id):
    return bcrypt.verify(id_password, hashed_id)
    

def cadastro_user():
    first_name = input("Digite seu primeiro nome: ")
    first_name = re.sub(r'[^a-z]','',first_name)#improve this
    first_name = str(first_name)
    last_name = input("Digite seu sobrenome: ")
    last_name = re.sub(r'[^a-z]','',last_name)
    last_name = str(last_name)
    while True:
        CPF = input("Digite o seu CPF: ")
        CPF.isalpha
        CPF = re.sub('[^0-9]', '', CPF)
        if len(CPF) != 11:#testar cpf len
            print("CPF inválido. Verifique a quantidade de dígitos.")
            continue
            #cpf_formatado = f"{CPF[:3]}.{CPF[3:6]}.{CPF[6:9]}-{CPF[9:]}"      
        else:
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

        hashed_id = hash_id(id_password)
        id_input = input("Digite a sua senha novamente para verificar: ")
        id_match = verify_id(id_input, hashed_id)
        if id_match:
            print("Senha Salva com sucesso")
            break
        else:
            print("Senha Incorreta")
            continue
        
    user = { #Melhorar a saida do discionario
        'first_name': first_name,
        'last_name': last_name,
        'cpf': CPF,
        'email': email,
        'password': id_password,
        'bikes': [] # initialize empty bikes list
    }
    users.append(user)
    return user
