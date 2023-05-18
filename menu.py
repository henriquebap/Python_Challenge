import cv2
#if you get the "ModuleNotFoundError, he suggests that the module cv2 is not installed in your Python enviroment, so to fix that you need install cv2 using pip command"
#You can run this pip install opencv-python-headless at the terminal or command prompt to install cv2
from option import option, opt_bike
from user import login, remove_user, cadastro_user
from bike import cad_bike, edit_bike, remove_bike, list_user_bike

#improve all of these dictionarys
bikes =[]
users = []
#bike_img = [] #database...?

while True:
    try:
        Option = option()
    except ValueError:
        print("Opcai Invalida. Por favor, digite um numero valido.")
        continue
    if Option == 1:
        user = login(users)
        if user:
            print(f"Seja Bem-vindo {user.first_name}, vamos continuar com o seu processo")
            while True:
                inp_bike = opt_bike()
                if inp_bike == 0: 
                    break
                if inp_bike == 1:
                    bike = cad_bike(user) #adding a bike to user's bike list
                    bikes.append(bike)
                elif inp_bike == 2:
                    pass
                    #bike = survey_bike(bikes)
                    #bike_img.append(bike)
                elif inp_bike == 3:
                    list_user_bike(user)
                elif inp_bike == 4:
                    edit_bike(user.bikes)
                elif inp_bike == 5:
                    remove_bike(bikes, user)
        else:
            print("Nao foi encontrado o usuario")
            confirm = input("Gostaria de Criar um Usuario? (s/n)")
            while confirm.lower() not in ["s", "n"]:
                print("Por favor, digite 's' para Sim ou 'n' para Não.")
                confirm = input("Gostaria de criar um usuário? (s/n)")
            if confirm.lower() == "s":
                user = cadastro_user(users)
                print("Usuário cadastrado com sucesso.")
                users.append(user)
            else:
                continue
    elif Option == 2:
        user = cadastro_user(users)
        print("Usuario cadastrado com sucesso")
        users.append(user)
    elif Option == 3:
        remove_user(users)
    elif Option == 0:
        break
    else:
        print("Digite um numero funcional")