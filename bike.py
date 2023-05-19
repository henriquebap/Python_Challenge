#Importa o modulo "re"
import re
#modulo datetime
import datetime
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
    #Laco de repeticao
    while True:
        bike_brand = input("Digite a marca da bike: ")
        if not bike_brand.isalpha(): #validacao se a entrada foi de numeros
            print("Por favor, digite o nome da marca com somente letras.")
            continue
        bike_brand = re.sub(r'[^a-zA-Z]', '', bike_brand) #Tira toda a sujeita do input
        break
    while True:
        print("Tipos de bike disponíveis:")
        for bike_type in bike_types: #Para todas os tipos de bike no tipo de bike mostrar todos os nomes
            print(bike_type.name)
        bike_type_input = input("Digite o tipo da bike: ")
        if not any(bike_type_input.lower() == bike_type.name.lower() for bike_type in bike_types): #Se a entrada do ususario nao for nenhuma opcao dada, retorna erro
            print("Por favor, Digite um tipo de bike Valido.")
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
            bike_value = float(bike_value) #Validacao se a entrada foi um numero mesmo
            break
        except ValueError:
            print("Por favor, digite um valor numerico valido")

    bike = Bike(bike_brand, bike_type, bike_id, bike_year, bike_value, additional_modifications=0) #Depois de todas as entradas ele atribui a Bike cada valor
    user.bikes.append(bike) #Adiciona essa bike em user
    print("Bike Cadastrada com sucesso") 
    return user
#Funcao de editar as bikes 
def edit_bike(bikes):
    bike_id = input("Digite o ID da bike que deseja editar: ")
    for bike in bikes:
        if bike.serial_number == bike_id: #se a entrada do usuario for de acordo com um Numero de serie de uma bike existente ele continua
            print("Bike selecionada:")
            print(bike) #Mostra a bike puxando o __STR__
            total_additional_modifications = 0
            while True:
                additional_modification = input("Digite uma modificação adicional para a bike (Deixe em branco para sair): ")
                if additional_modification == "":
                    break
                else:
                    modification_value = input("Digite o valor da modificação adicional: ")
                    try: #Valida o numero de input e adiciona ao valor inicial
                        modification_value = float(modification_value)
                        total_additional_modifications += modification_value #a cada modificacao com valor atribuido ele soma e deixa no valor total
                        bike.additional_modifications.append(f"{additional_modification} + {modification_value} reais")
                    except ValueError:
                        print("Valor inválido. Digite um valor numérico válido.")
            bike.value += total_additional_modifications #Finaliza somando o valor total de modificacao + O valor inicial 
            print("---"*40)
            print(f'O nome da sua marca da sua bike atualmente e {bike.brand}')
            new_name = input("Digite o nome da marca corretamente(Deixe em branco para manter o mesmo): ")
            if new_name != "": #condicional se ele deixar vazio ele continua com o mesmo valor inicial
                break
            if not new_name.isalpha():
                print("Por favor, digite o nome somente com letras")
            else:
                bike.brand = new_name
                #verificar o erro de loop infinito nao deixando o vazio ser uma opcao de entrada
            while True:
                print("Tipos de bike disponíveis:")
                for bike_type in bike_types:
                    print(bike_type.name)
                print("---"*40)
                print(f"O Tipo atual da sua bike e {bike.bike_type.name}")
                new_type = input("Corriga o Tipo de bike (Deixe em branco para manter o mesmo): ")
                if new_type != "":
                    break
                elif not any(new_type.lower() == bike_type.name.lower() for bike_type in bike_types):
                    print("Por favor, Digite um tipo de bike Valido.")
                    continue    
                bike.bike_type = new_type
                break
            f'\n'
            print("---"*40)
            print(f"O ano atual da sua bike e {bike.year}")
            new_year = input("Corriga o Ano da sua bike (Deixe em branco para manter o mesmo): ")
            if new_year != "":
                if not new_year.isdigit() or len(new_year) != 4:
                    print("Ano inválido. Digite um ano válido com 4 dígitos.")
                    continue
                current_year = datetime.now().year
                if int(new_year) > current_year:
                    print("Ano inválido. Digite um ano igual ou anterior ao ano atual.")
                    continue
                bike.year = new_year
            print("Bike atualizada com sucesso.")
            return

    print("Bike não encontrada.")

def remove_bike(bikes, user):# Precisa de Tratamento de excecao
    bike_id = input("Digite o ID da bike que deseja remover: ")
    for bike in bikes:
        #Verificar o erro de excluir
        if bike.serial_number == bike_id and bike in user.bikes: #se o serial number do input for valido com alguma bike criada e salva em user ele apaga a bike
            user.bikes.remove(bike)
            bikes.remove(bike)
            print("Bike removida com sucesso.")
            return
    print("Bike não encontrada ou não está cadastrada para este usuário.")

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


