import cv2
#if you get the "ModuleNotFoundError, he suggests that the module cv2 is not installed in your Python enviroment, so to fix that you need install cv2 using pip command"
#You can run this pip install opencv-python-headless at the terminal or command prompt to install cv2
from Options.option import option, opt_bike
from user.user import login, remove_user, cadastro_user
from bike.bike import cad_bike, edit_bike, remove_bike, list_user_bike

#improve all of these dictionarys
bikes =[]
users = []
bikes_users = [bikes, users]#for sure improve this
bike_img = [] #database...?

while True:
    Option = option()
    if Option == 1:
        user = login(users)
        if user:
            print(f"Seja Bem-vindo {user['first_name']}, vamos continuar com o seu processo")
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
                    list_user_bike(bikes_users)
                elif inp_bike == 4:
                    edit_bike(bikes)
                elif inp_bike == 5:
                    remove_bike(bikes, user)
                else:
                    print("Digite uma opcao valida")
        else:
            print("Nao foi encontrado o usuario")
            confirm = input("Gostaria de Criar um Usuario? (s/n)")
            if confirm.lower() == "s":
                user = cadastro_user()
                print("Usuario Cadastrado com sucesso")
                users.append(user)
            else:
                break
    elif Option == 2:
        user = cadastro_user()
        print("Usuario cadastrado com sucesso")
        users.append(user)
    elif Option == 3:
        remove_user(users)
    elif Option == 0:
        break
    else:
        print("Digite uma opcao valida")

    