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

def login(users):#Trouble in verification section, it is passing through
    id_mail = input("Digite o seu email: ")
    id_password = input("Digite a senha: ")
    for user in users:
         if user['email'] == id_mail and user['password'] == id_password:
            return user
    print("A senha ou email estao incorretos")
    return None     
    
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
    bike_name = input("Digite a marca da bike: ")
    bike_model = input("Digite o modelo da bike (Ex: Montain, Street, Speed etc): ")
    bike_id = input("Digite o Num de fabrica (Ex: 00000): ")
    bike_year = input("Digite o ano de fabricacao da bike: ")
    bike_value = input("Digite o valor da bike: ")
    bike = {
        'bike_name': bike_name,
        'bike_model': bike_model,
        'bike_id': bike_id,
        'bike_year': bike_year,
        'bike_value': bike_value
    }
    return bike

bikes =[]
users = []

while True:
    Option = option()
    if Option == 1:
        user = login(users)
        if user:
            print(f"Seja Bem-vindo {user['first_name']}")
        else:
            print("Nao foi encontrado o usuario")
            confirm = input("Gostaria de Criar um Usuario? (s/n)")
            if confirm == "s":
                user = cadastro_user()
                users.append(user)
            else:
                break
        print(f"Seja Bem-vindo {user['first_name']}, vamos continuar com o seu processo")
        inp_bike = opt_bike()
        if inp_bike == 0: 
            break
        if inp_bike == 1:
            bike = cad_bike()
            bikes.append(bike)
        elif inp_bike == 2:
            pass

    elif Option == 2:
        user = cadastro_user()
        users.append(user)
    else:
        print("Digite uma opcao valida")

    