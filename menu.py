import utilities
import api_ia
from database import models
from database import crud


class MenuItem:
    def __init__(self, description, action):
        self.description = description
        self.action = action


class MainMenu:
    def __init__(self, user):
        self.user = user
        self.options = [
            MenuItem("Iniciar processo da bike", lambda: self.open_submenu()),
            MenuItem("Mostrar Perfil", lambda: self.carregar_user()),
            MenuItem("Exluir conta", lambda: self.remove_user()),
            MenuItem("Sair", None),
        ]

        self.submenu = BikeMenu(user)

    def login(self):
        pass

    def cadastro_user(self):
        crud.create_user(self.user)

    def carregar_user(self):
        crud.read_user(self.user)

    def remove_user(self):
        crud.delete_user(self.user)

    def open_submenu(self):
        self.submenu.show_options()
        self.submenu.user_input()

    def show_options(self):
        for index, option in enumerate(self.options, 1):
            print(f"{index} - {option.description}")

    def user_input(self):
        while True:
            print("---" * 40)
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
    def __init__(self, user):
        self.user = user
        self.options = [
            MenuItem("Bike Menu - Cadastrar uma Bike", lambda: self.cad_bike()),
            MenuItem("Bike Menu - Editar uma Bike", lambda: self.edit_bikes()),
            MenuItem("Bike Menu - Remover uma Bike criada", lambda: self.remove_bike()),
            MenuItem(
                "Bike Menu - Listar Bikes cadastradas", lambda: self.list_user_bike()
            ),
            MenuItem("Bike Menu - Enviar Imagens da bike", api_ia.cv_api),
            MenuItem("Menu Principal - para voltar ao menu principal", action=None),
        ]

    def cad_bike(self):
        crud.create_bike(self.user)

    def edit_bikes(self):
        crud.update_bike(self.user)

    def remove_bike(self):
        crud.delete_bike(self.user)

    def list_user_bike(self):
        crud.read_bike(self.user)

    def pred_ia(self):
        image_path, prediction_image_path, predicted_class, confidence = api_ia.cv_api()

        # Crie uma bicicleta associada ao usuário
        new_bike = crud.create_bike(self.user)

        # Crie uma instância de PredictionResult com as informações da API
        api_response = models.PredictionResult(
            image_path=image_path,
            prediction_image_path=prediction_image_path,
            predicted_class=predicted_class,
            confidence=confidence,
            bike_id=new_bike.id,
        )

    def show_options(self):
        for index, option in enumerate(self.options, 1):
            print(f"{index} - {option.description}")

    def user_input(self):
        while True:
            print("---" * 40)
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
