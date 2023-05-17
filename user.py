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
    email = input("Digite o email do usuário a ser removido: ")
    for user in users:
        if user['email'] == email:
            users.remove(user)
            print("Usuário removido com sucesso.")
            return
    print("O usuário não foi encontrado.")

def cadastro_user():
    first_name = input("Digite seu primeiro nome: ")
    try:
        first_name = re.sub(r'[^a-z]','',first_name)#improve this
        first_name = str(first_name)
    except:
        print("Porfavor, digite o seu nome somente com Letras")
    last_name = input("Digite seu sobrenome: ")
    try:
        last_name = re.sub(r'[^a-z]','',last_name)
    except:
        print("Porfavor Digite o seu sobrenome somente com letras")
    CPF = input("Digite o seu CPF: ")#number treatment too
    try:
        CPF.isalpha
        CPF = re.sub('[^0-9]', '', CPF)
        if len(CPF) != 11:
            return "CPF inválido. Verifique a quantidade de dígitos."
    except:
        print("Porfavor Coloque somente numeros no seu cpf")

    cpf_formatado = f"{CPF[:3]}.{CPF[3:6]}.{CPF[6:9]}-{CPF[9:]}"

    email = input("Digite o seu email: ").strip()
    try:
        padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(padrao, email):
            return "Porfavor verifique o formato do seu email"
    except:
        print("Dgiite um email valido")
    #we want make string treatment here. Just to remember
    def hash_id(identification):
        hashed_id = bcrypt.hash(identification)
        return hashed_id
    def verify_id(identification, hashed_id):
        return bcrypt.verify(identification, hashed_id)
    
    identification = input("Crie uma Senha: ")

    hashed_id = hash_id(identification)
    
    id_input = input("Digite a sua senha novamente para verificar: ")
    id_match = verify_id(id_input, hashed_id)
    if id_match:
        print("Senha Salva com sucesso")
    else:
        print("Senha Incorreta")

    user = {
        'first_name': first_name,
        'last_name': last_name,
        'cpf': CPF,
        'email': email,
        'password': identification,
        'bikes': [] # initialize empty bikes list
    }
    users.append(user)
    return user
