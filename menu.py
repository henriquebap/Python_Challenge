import utilities
import bike
import user_tools
import api_ia
import json
from app_state import AppState
#users = []
#bikes = []
#user = user_tools.User(first_name=None, last_name=None, cpf=None, email=None,password=None)

class MenuItem:
    def __init__(self, description, action):
        self.description = description
        self.action = action

class MainMenu:
    def __init__(self, app_state):
        #users
        self.app_state = app_state
        self.options = [
            MenuItem("Iniciar processo da bike", lambda: self.open_submenu()),
            MenuItem("Mostrar perfil", lambda: self.carregar_user()),
            MenuItem("Excluir conta", lambda: self.remove_user()),
            MenuItem("Sair", None)

        ]

        self.submenu = BikeMenu(app_state)

    #new_user = lambda: user_tools.cadastro_user(users)

    def login(self):
        user_tools.login(self.app_state)

    def cadastro_user(self):
        user_tools.cadastro_user(self.app_state)
    
    def carregar_user(self):
        user_tools.carregar_user(self.app_state)

    def remove_user(self):
        user_tools.remove_user(self.app_state)

    def open_submenu(self):
        self.submenu.show_options()
        self.submenu.user_input()
        

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


class BikeMenu:
    def __init__(self, app_state):
        #user
        #bikes
        self.app_state = app_state
        self.options = [
            MenuItem("Bike Menu - Cadastrar uma Bike",lambda: self.cad_bike()),
            MenuItem("Bike Menu - Editar uma Bike", lambda: self.edit_bikes()),
            MenuItem("Bike Menu - Remover uma Bike criada", lambda: self.remove_bike()),
            MenuItem("Bike Menu - Listar Bikes cadastradas", lambda: self.list_user_bike()),
            MenuItem("Bike Menu - Enviar Imagens da bike", api_ia.cv_api),
            MenuItem("Menu Principal - para voltar ao menu principal", action=None)
        ]


    def cad_bike(self):
        bike.cad_bike(self.app_state)

    def edit_bikes(self):
        bike.edit_bikes(self.app_state)

    def remove_bike(self):
        bike.remove_bike(self.app_state)

    def list_user_bike(self):
        bike.list_user_bike(self.app_state)



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
