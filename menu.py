import utilities
import bike
import user
import api_ia
#User.users

class MenuItem:
    def __init__(self, description, action):
        self.description = description
        self.action = action

class MainMenu:
    def __init__(self):
        #self.cadastro_realizado = False
        self.users = []

        self.options = [
            MenuItem("Realizar Login", lambda: user.login(self.users)),
            MenuItem("Iniciar processo da bike", lambda: self.open_submenu()),
            MenuItem("Cadastrar Usuario", lambda: user.cadastro_user(self.users)),
            MenuItem("Excluir conta", lambda: user.remove_user(self.users)),
            MenuItem("Sair", None)

        ]

        self.submenu = BikeMenu()

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
    def __init__(self):
        self.user = "Usuario padrao"
        self.bikes = []

        self.options = [
            MenuItem("Bike Menu - Cadastrar uma Bike", lambda user=self.user: bike.cad_bike(user)),
            MenuItem("Bike Menu - Editar uma Bike", lambda bikes=self.bikes: bike.edit_bikes(bikes)),
            MenuItem("Bike Menu - Remover uma Bike criada", lambda user=self.user: bike.remove_bike(user)),
            MenuItem("Bike Menu - Listar Bikes cadastradas", lambda user=self.user: bike.list_user_bike(user)),
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
