from user import cadastro_user
class Bike:
    def __init__(self, brand, model, serial_number, year, value):
        self.brand = brand
        self.model = model
        self.serial_number = serial_number
        self.year = year
        self.value = value 

def cad_bike(user):#Colocar as excecoes 
    bike_brand = input("Digite a marca da bike: ")#Inprove the accuracy with saving lot of bike brands
    bike_model = input("Digite o modelo da bike (Ex: Montain, Street, Speed etc): ")#improve the input
    bike_id = input("Digite o Num de fabrica (Ex: 00000): ")#verify the code with an API or bike data
    bike_year = input("Digite o ano de fabricacao da bike: ")#improve the input
    bike_value = input("Digite o valor da bike: ")#improve the input
    bike = Bike(bike_brand, bike_model, bike_id, bike_year, bike_value)
    user.bikes.append(bike)
    print("Bike Cadastrada com sucesso")
    return user

def edit_bike(bikes):#adicionar funcao para colocar um item de valor a mais
    bike_id = input("Digite o ID da bike que deseja editar: ")
    for bike in bikes:
        if bike.serial_number == bike_id:
            print("Bike selecionada:")
            print(bike)
            new_name = input("Digite o novo nome da bike (Deixe em branco para manter o mesmo): ")
            if new_name != "":
                bike.brand = new_name
            new_model = input("Digite o novo modelo da bike (Deixe em branco para manter o mesmo): ")
            if new_model != "":
                bike.model = new_model
            new_year = input("Digite o novo ano da bike (Deixe em branco para manter o mesmo): ")
            if new_year != "":
                bike.year = new_year
            new_value = input("Digite o novo valor da bike (Deixe em branco para manter o mesmo): ")
            if new_value != "":
                bike.value = new_value
            print("Bike atualizada com sucesso.")
            return
    print("Bike não encontrada.")

def remove_bike(bikes, user):
    bike_id = input("Digite o ID da bike que deseja remover: ")
    for bike in bikes:
        if bike.serial_number == bike_id and bike in user.bikes:
            user.bikes.remove(bike)
            bikes.remove(bike)
            print("Bike removida com sucesso.")
            return
    print("Bike não encontrada ou não está cadastrada para este usuário.")

def list_user_bike(user):#mostrar modificacoes extras da bike
        print("----"*10)
        print(f"Ola {user.first_name} Aqui esta as suas bicicletas cadastradas")
        if len(user.bikes) == 0:
            print("Nenhuma bike cadastrada")
        else:
            for bike in user.bikes:
                print("----"*10)
                print("Marca:",bike.brand)
                print("Modelo:",bike.model)
                print("Num de Serie:",bike.serial_number)
                print("Ano:",bike.year)
                print("Preco:",bike.value)
                print("----"*10)


