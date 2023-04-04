def option():
    print("1 - Realizar o login")
    print("2 - Criar um cadastro")
    print("0 - Sair")

    Option = int(input())
    return Option

def opt_bike():
    print("1 - Cadastrar uma bike no seguro")
    print("2 - Realizar uma vistoria de uma bike")
    print("3 - Visualizar o processo do seguro")
    print("0 - Sair")

    inp_bike = int(input())
    return inp_bike

def login(users):
    id_mail = input("Digite o seu email: ")
    id_password = input("Digite a senha: ")
    for user in users:
        if user ['email'] == id_mail:
            if user ['password'] == id_password:
                return user
        else:
            print("A senha ou email estao incorretos")
            return id_mail

def cadastro_user():
    first_name = input("Digite seu primeiro nome: ")
    last_name = input("Digite seu sobrenome: ")
    CPF = input("Digite o seu CPF: ")
    email = input("Digite o seu email: ")
    identification = input("Crie uma Senha: ")
    user = {
        'first_name': first_name,
        'last_name': last_name,
        'cpf': CPF,
        'email': email,
        'password': identification
    }
    return user
    
def cad_bike():
    pass 

bikes =[]
users = []

while True:
    Option = option()
    if Option == 1:
        user = login(users)
        if user:
            print(f"Seja Bem-vindo {user['first_name']}")
        inp_bike = opt_bike()
        if inp_bike == 0: 
            break
        if inp_bike == 1:
            pass 
        elif inp_bike == 2:
            pass
    

        else:
            print("Nao foi encontrado o usuario")
            confirm = input("Gostaria de Criar um Usuario? (s/n)")
            if confirm == "s":
                user = cadastro_user()
                users.append(user)

    elif Option == 2:
        user = cadastro_user()
        users.append(user)