#Importa o modulo "re"
import re
#modulo datetime
from datetime import datetime
#from user import cadastro_user
#Classe bike que cria objeto Bike com todos os atributos de uma bike
class Bike:
    def __init__(self, brand, bike_type, serial_number, year, value, additional_modifications):
        self.brand = brand
        self.bike_type = bike_type
        self.serial_number = serial_number
        self.year = year
        self.value = value
        self.additional_modifications = additional_modifications or []

    bikes =[]

    #STR permite que o print(bike) retorne uma mensagem certa, mostrando os atributos de uma bike
    def __str__(self):
        modifications = "\n".join(self.additional_modifications) if self.additional_modifications else "Nenhuma modificação adicional"
        return f"Marca: {self.brand}\nModelo: {self.bike_type.name}\nNum de Série: {self.serial_number}\nAno: {self.year}\nPreço: {self.value}\nModificações adicionais:\n{modifications}"
#Class bike Type define modelo de bike especifico com nome e descricao
class BikeType(Bike):
    def __init__(self, name, description):
        self.name = name
        self.description = description
#Criando e instanciando modelos de bikes atribuindo a classe bikeType
mountain_bike_type = BikeType("Mountain Bike","Feita para off-road")
road_bike_type = BikeType("Street","Bike feita para andar nas ruas")
bmx_bike_type = BikeType("BMX","Bike feita para manobras")
folding_bike_type = BikeType("Folding bike","Bike que dobra e e bem pequena")
eletric_bike_type = BikeType("Bike eletrica","Bike com motorzinho eletrico")
speed_bike_type = BikeType("Speed","Bike com pneu fino e que corre")
#Criando uma lista de bike_types
bike_types = [mountain_bike_type, road_bike_type, bmx_bike_type, folding_bike_type, eletric_bike_type, speed_bike_type]

#funcao para cadastrar a bike em um user
def cad_bike(user):
    while True:
        bike_brand = input("Digite a marca da bike: ").strip(" #@!$%^&*")
        if not bike_brand.isalpha(): #validacao se a entrada foi de String
            print("Por favor, digite o nome da marca com somente letras.")
            continue
        bike_brand = re.sub(r'[^a-zA-Z]', '', bike_brand) #Se sobrar alguma sujeira e limpado aqui
        break
    while True:
        print("Tipos de bike disponíveis:")
        for bike_type in bike_types:
            print(bike_type.name)
            
        bike_type_input = input("Digite o tipo da bike: ").strip().lower()
        valid_bike_type = False
        
        for bike_type in bike_types:
            if bike_type_input == bike_type.name.lower():
                valid_bike_type = True
                break
        
        if not valid_bike_type:
            print("Por favor, digite um tipo de bike válido.")
            continue
        
        break
    while True:
        bike_id = input("Digite o Num de serie (Ex: 00000): ") 
        if not bike_id.isdigit() or len(bike_id) != 5: #Numero de serie limitado a 5 digitos e somente digitos
            print("Por favor, digite um numero de serie valido (5 Digitos).")
            continue
        break
    while True:
        bike_year = input("Digite o ano de fabricacao da bike: ") 
        if not bike_year.isdigit() or len (bike_year) != 4: #limitado a 4 digitos e somente numero
            print("Por favor, Digite os 4 digitos do ano da bike.")
            continue
        bike_year = int(bike_year) #Valida se o ano digitado e valido, se for maior do que o ano que estamos gera um erro
        if bike_year > 2023:
            print("Por Favor, digite um ano valido ate 2023.")
            continue
        break
    while True:
        bike_value = input("Digite o valor da bike: ")
        try:
            bike_value = float(bike_value) #Transforma a entrada em float
            break
        except ValueError: #Valida se a entrada e um numero e senao for retorna um value error
            print("Por favor, digite um valor numerico valido")

    bike = Bike(bike_brand, bike_type, bike_id, bike_year, bike_value, additional_modifications=0) #Depois de todas as entradas ele atribui a Bike cada valor
    user.bikes.append(bike) #Adiciona essa bike em user
    print("Bike Cadastrada com sucesso") 
    return user
#Funcao de editar as bikes 
def edit_bikes(bikes):
    bike_serial_number = input("Digite o ID da bike que deseja editar: ")
    bike = None  # Inicialize a variável bike fora do loop for
    for b in bikes:
        if b.serial_number == bike_serial_number:
            bike = b
            print(f"Bike Selecionada: {bike}")
            total_additional_modifications = 0

    if bike is None:
        print("Bike nao encontrada!")
        return

    while True:
        print("---" * 40)
        print("O que voce deseja editar?")
        print("1. Marca")
        print("2. Modelo")
        print("3. Ano")
        print("4. Adicionar uma nova modificacao")
        print("0. Voltar ao bike menu")

        try:
            choice = int(input("Digite o numero correspondente a opcao desejada: "))
        except ValueError:
            print("Por favor, digite um numero correspondente a opcao")
            continue

        if choice == 1:
            print(f'O nome da sua marca da sua bike atualmente e {bike.brand}')
            while True:
                new_brand = input("Digite a nova marca: ")
                if not new_brand.isalpha():
                    print("Por favor, digite o nome da marca com somente letras.")
                    continue
                new_brand = re.sub(r'[^a-zA-Z]', '', new_brand)
                bike.brand = new_brand
                break
        elif choice == 2:
            print("Tipos de bike disponíveis:")
            for bike_type in bike_types:
                print(bike_type.name)
            print("---" * 40)
            print(f"O Tipo atual da sua bike e {bike.bike_type.name}")
            while True:
                new_type = input("Digite o novo tipo da bike: ").strip()
                if not any(new_type.lower() == bike_type.name.lower() for bike_type in bike_types):
                    print("Por favor, Digite um tipo de bike Valido.")
                    continue
                bike.bike_type.name = new_type
                break
        elif choice == 3:
            new_bike_year = input("Digite o ano correto da bike: ")
            if not new_bike_year.isdigit() or len(new_bike_year) != 4:
                print("Por favor, digite os 4 digitos do ano da bike.")
                continue
            new_bike_year = int(new_bike_year)
            if new_bike_year > 2023:
                print("Por favor, digite um ano valido ate 2023")
                continue
            bike.bike_year = new_bike_year
        elif choice == 4:
            total_additional_modifications = 0  # Inicialize total_additional_modifications fora do loop while
            while True:
                additional_modification = input("Digite uma modificação adicional para a bike (Deixe em branco para sair): ")
                if additional_modification == "":
                    break
                else:
                    modification_value = input("Digite o valor da modificação adicional: ")
                    try:
                        modification_value = float(modification_value)
                        total_additional_modifications += modification_value
                        bike.additional_modifications.append(f"{additional_modification} + {modification_value} reais")
                    except ValueError:
                        print("Valor inválido. Digite um valor numérico válido.")
            bike.value += total_additional_modifications
            break
        elif choice == 0:
            return
def remove_bike(bikes):
    bike_serial_number = input("Digite o ID da bike que deseja remover: ")
    for bike in bikes:
        if bike.serial_number == bike_serial_number:
            bikes.remove(bike)
            print("Bike removida com sucesso!")
            return
    print("Bike não encontrada!")

def list_user_bike(user): #Mostra o usuario e as suas bikes salvas
        print("----"*10)
        print(f"Ola {user.first_name} Aqui esta as suas bicicletas cadastradas")
        if len(user.bikes) == 0:
            print("Nenhuma bike cadastrada")
        else:
            for bike in user.bikes:
                print("----"*10)
                print("Marca:",bike.brand)
                print("Modelo:",bike.bike_type.name)
                print("Num de Serie:",bike.serial_number)
                print("Ano:",bike.year)
                print("Preco:",bike.value)
                print("Modificacoes:", bike.additional_modifications)
                print("----"*10)


