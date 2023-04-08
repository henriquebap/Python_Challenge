import re
import cv2
#if you get the "ModuleNotFoundError, he suggests that the module cv2 is not installed in your Python enviroment, so to fix that you need install cv2 using pip command"
#You can run this pip install opencv-python-headless at the terminal or command prompt to install cv2


def option():
    print("1 - Realizar o login")
    print("2 - Criar um cadastro")
    print("3 - Remover um usuário cadastrado")
    print("0 - Sair")

    Option = int(input())
    return Option

def opt_bike():
    print("1 - Cadastrar uma bike no seguro")
    print("2 - Realizar uma vistoria de uma bike - (Not ready)")
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
    
def cad_bike(user):
    bike_name = input("Digite a marca da bike: ")#Inprove the accuracy with saving lot of bike brands
    bike_model = input("Digite o modelo da bike (Ex: Montain, Street, Speed etc): ")#improve the input
    bike_id = input("Digite o Num de fabrica (Ex: 00000): ")#verify the code with an API or bike data
    bike_year = input("Digite o ano de fabricacao da bike: ")#improve the input
    bike_value = input("Digite o valor da bike: ")#improve the input
    bike = {
        'bike_name': bike_name,
        'bike_model': bike_model,
        'bike_id': bike_id,
        'bike_year': bike_year,
        'bike_value': bike_value
    }
    user['bikes'].append(bike) #add bike to user's bike list
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
    # define image and video capture objects
    #This is a prototype of what we what to include
    cap = cv2.VideoCapture(0) # use the default camera
    img_counter = 0
    vid_counter = 0

    # define maximum survey time
    survey_time = 60 # in seconds

    # initialize image and video names
    img_names = ['side', 'front', 'wheels', 'id', 'model']
    vid_name = 'full_body'

    # loop until maximum survey time is reached
    start_time = cv2.getTickCount()
    while True:
        # check if survey time is exceeded
        current_time = cv2.getTickCount()
        if (current_time - start_time) / cv2.getTickFrequency() > survey_time:
            break

        # read image from camera
        ret, frame = cap.read()

        # display image
        cv2.imshow('frame', frame)

        # check for keypresses
        k = cv2.waitKey(1)
        if k == 27: # ESC key to exit
            break
        elif k == 32: # space key to capture image
            if img_counter < len(img_names):
                img_name = '{}.jpg'.format(img_names[img_counter])
                cv2.imwrite(img_name, frame)
                img_counter += 1
        elif k == ord('v'): # 'v' key to start recording video
            vid_name = 'full_body.avi'
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(vid_name, fourcc, 20.0, (640, 480))
        elif k == ord('r'): # 'r' key to stop recording video
            out.release()
            vid_counter += 1

    # release image and video capture objects
    cap.release()
    cv2.destroyAllWindows()

    # run object detection on captured images
    # use TensorFlow Object Detection API

    # return results
    return img_names, vid_name

def list_user_bike(bikes_users):#need ideas to improve
    print(bikes_users)

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
                    bike = survey_bike(bikes)
                    bike_img.append(bike)
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

    