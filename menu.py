import re
def option():
    print("1 - Realizar o login")
    print("2 - Criar um cadastro")
    print("3 - Remover um usuário cadastrado")
    print("0 - Sair")

    Option = int(input())
    return Option

def opt_bike():
    print("1 - Cadastrar uma bike no seguro")
    print("2 - Realizar uma vistoria de uma bike")
    print("3 - Visualizar o processo do seguro")
    print("4 - Editar uma bike cadastrada")
    print("5 - Remover uma bike do cadsatro")
    print("0 - Sair")

    inp_bike = int(input())
    return inp_bike

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
    first_name = re.sub(r'[^a-z]','',first_name)
    last_name = input("Digite seu sobrenome: ")
    last_name = re.sub(r'[^a-z]','',last_name)
    CPF = input("Digite o seu CPF: ")
    email = input("Digite o seu email: ")
    identification = input("Crie uma Senha: ")
    user = {
        'first_name': first_name,
        'last_name': last_name,
        'cpf': CPF,
        'email': email,
        'password': identification,
        'bikes': [] # initialize empty bikes list
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

def edit_bike(bikes):
    bike_id = input("Digite o ID da bike que deseja editar: ")
    for bike in bikes:
        if bike['bike_id'] == bike_id:
            print("Bike selecionada:")
            print(bike)
            new_name = input("Digite o novo nome da bike (Deixe em branco para manter o mesmo): ")
            if new_name != "":
                bike['bike_name'] = new_name
            new_model = input("Digite o novo modelo da bike (Deixe em branco para manter o mesmo): ")
            if new_model != "":
                bike['bike_model'] = new_model
            new_year = input("Digite o novo ano da bike (Deixe em branco para manter o mesmo): ")
            if new_year != "":
                bike['bike_year'] = new_year
            new_value = input("Digite o novo valor da bike (Deixe em branco para manter o mesmo): ")
            if new_value != "":
                bike['bike_value'] = new_value
            print("Bike atualizada com sucesso.")
            return
    print("Bike não encontrada.")

def remove_bike(bikes, user):
    bike_id = input("Digite o ID da bike que deseja remover: ")
    for bike in bikes:
        if bike['bike_id'] == bike_id and bike in user['bikes']:
            user['bikes'].remove(bike)
            bikes.remove(bike)
            print("Bike removida com sucesso.")
            return
    print("Bike não encontrada ou não está cadastrada para este usuário.")

def survey_bike(bikes):
### the idea here it's to give an option to open the camera and then the user will take pictures of the product(bike) or make a video of the bike
#the type of pic is side, front, wheels, id and model.
#the video needs show full body bike
#has a limit time to make the survey
#the user couldn't open the gallery and take old pictures of the bike
#to verify this option we will probably use IA using deeplearning with TensorFlow Object Detection: Detection Models, but we need a big bike database
    pass

def list_user_bike(bikes_users):
    print(bikes_users)

bikes =[]
users = []
bikes_users = [bikes, users]
bike_img = [] #database...

while True:
    Option = option()
    if Option == 1:
        user = login(users)
        if user:
            continue
        else:
            print("Nao foi encontrado o usuario")
            confirm = input("Gostaria de Criar um Usuario? (s/n)")
            if confirm == "s":
                user = cadastro_user()
                users.append(user)
            else:
                break
        print(f"Seja Bem-vindo {user['first_name']}, vamos continuar com o seu processo")
        
        while True:
            inp_bike = opt_bike()
            if inp_bike == 0: 
                break
            if inp_bike == 1:
                bike = cad_bike()
                bikes.append(bike)
            elif inp_bike == 2:
                bike = survey_bike()
                bike_img.append(bike)
            elif inp_bike == 3:
                list_user_bike(bikes_users)
            elif inp_bike == 4:
                edit_bike(bikes)
            elif inp_bike == 5:
                remove_bike(bikes, user)
            else:
                print("Digite uma opcao valida")
    elif Option == 2:
        user = cadastro_user()
        users.append(user)
    elif Option == 3:
        remove_user(users)
    elif Option == 0:
        break
    else:
        print("Digite uma opcao valida")

    