users = []
import re
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
    first_name = re.sub(r'[^a-z]','',first_name)#improve this
    last_name = input("Digite seu sobrenome: ")
    last_name = re.sub(r'[^a-z]','',last_name)
    CPF = input("Digite o seu CPF: ")#number treatment too
    email = input("Digite o seu email: ")
    #we want make string treatment here. Just to remember
    identification = input("Crie uma Senha: ")
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
