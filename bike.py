
def cad_bike(user):#Melhorar as excecoes
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

def list_user_bike(bikes_users):#need ideas to improve
    print(bikes_users)
