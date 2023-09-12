import utilities
import bike
import user_tools
import api_ia
import json
#User.users
users = []
bikes = []
user = user_tools.User(first_name=None, last_name=None, cpf=None, email=None,password=None)

class MenuItem:
    def __init__(self, description, action):
        self.description = description
        self.action = action

class MainMenu:
    def __init__(self):
        #self.cadastro_realizado = False
        users
        self.options = [
            MenuItem("Realizar Login", lambda: user_tools.login(users)),
            MenuItem("Iniciar processo da bike", lambda: self.open_submenu()),
            MenuItem("Cadastrar Usuario", lambda: user_tools.cadastro_user(users)),
            MenuItem("Mostrar perfil", lambda: user_tools.carregar_user(users)),
            MenuItem("Excluir conta", lambda: user_tools.remove_user(users)),
            MenuItem("Sair", None)

        ]

        self.submenu = BikeMenu()

    new_user = lambda: user_tools.cadastro_user(users)

    def open_submenu(self):
        #if self.cadastro_realizado:
        self.submenu.show_options()
        self.submenu.user_input()
        #else:
            #print("Voce deve realizar o cadastro primeiro.")

    #def cadastro_usuario(self):
     #   user.cadastro_user(self.users)
      #  self.cadastro_realizado = True
       # print("Cadastro realizado com sucesso! ") 
    #def login(self):
     #   self.logged_in_user = user_tools.login(users)

    def show_options(self):
        for index, option in enumerate(self.options, 1):
            print(f"{index} - {option.description}")

    def user_input(self):
        while True:
            print("---"*40)
            print("Olá, Selecione uma opcao para executar uma ação.")
            option = input("Digite a opção que deseja: ")
            option = utilities.get_int(option)
            if option:
                break
            print("Informe um numero inteiro")

        if option > len(self.options):
            print("Selecione uma opcao valida")
            print("")
            return
        
        selected_option = self.options[option - 1]
        if selected_option.action:
            selected_option.action()
        input("Pressione enter para continuar...")


class BikeMenu():
    def __init__(self):
        user
        bikes
        self.options = [
            MenuItem("Bike Menu - Cadastrar uma Bike",lambda: bike.cad_bike(user)),
            MenuItem("Bike Menu - Editar uma Bike", lambda: bike.edit_bikes(bikes)),
            MenuItem("Bike Menu - Remover uma Bike criada", lambda: bike.remove_bike(user)),
            MenuItem("Bike Menu - Listar Bikes cadastradas", lambda: bike.list_user_bike(user)),
            MenuItem("Bike Menu - Enviar Imagens da bike", api_ia.cv_api),
            MenuItem("ENTER - para voltar ao menu principal", None)
        ]

    def show_options(self):
        for index, option in enumerate(self.options, 1):
            print(f"{index} - {option.description}")

    def user_input(self):
        while True:
            print("---"*40)
            print("Olá, Selecione uma opcao para executar uma ação.")
            option = input("Digite a opção que deseja: ")
            option = utilities.get_int(option)
            if option:
                break
            print("Informe um numero inteiro")

        if option > len(self.options):
            print("Selecione uma opcao valida")
            print("")
            return
        
        selected_option = self.options[option - 1]
        if selected_option.action:
            selected_option.action()
        input("Pressione enter para continuar...")
