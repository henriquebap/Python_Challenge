# import re
# import json
# import os
# from models import User
# from app_state import AppState
# from models import Bike
# #Criando class user e passando todos os atributos que um user tem


# def load_user(database_folder="users_json"):
#     users = []
#     database_folder = "users_json"
#     if not os.path.exists(database_folder):
#         os.makedirs(database_folder)
#     for json_file in os.listdir(database_folder):
#         if json_file.endswith(".json"):
#             json_file_path = os.path.join(database_folder, json_file)
#             with open(json_file_path, "r") as json_file:
#                 user_data = json.load(json_file)
#                 user = User(
#                     user_data["first_name"],
#                     user_data["last_name"],
#                     user_data["cpf"],
#                     user_data["email"],
#                     user_data["password"]
#                 )
#                 users.append(user)

#     return users

# #funcao que apos criar o user ele consegue fazer o login validando o email e a senha criada do ususario
# def login(app_state):
#     users = app_state.users

#     if not users:
#         print("Nao existe nenhum usuario cadastrado")
#         return
#     id_mail = input("Digite o seu email: ").lower()
#     id_password = input("Digite a senha: ")
#     for user in users:
#          if user.email == id_mail and user.verify_password(id_password): # faz a validacao
#             return user
#     print("A senha ou email estao incorretos")
#     return None

# def remove_user(app_state): #remove o ususario, com a entrada pedindo email e senha para excluir o usuario
#     users = app_state.users

#     cpf = input("Digite o seu CPF: ").strip(" #@!$%^&*")
#     if not cpf.isdigit() or len(cpf) != 11:
#         print("CPF inválido. Verifique a quantidade de dígitos.")


#     cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
#     cpf = cpf_formatado
#     id_password = input("Digite a Senha do usuario: ")
#     user_to_remove = None

#     for user in users:
#         if user.verify_password(id_password):
#             user_to_remove = user

#             if user_to_remove:
#                 users.remove(user_to_remove)
#                 print("Usuário removido com sucesso.")

#                 # Formate o CPF novamente para ser usado como nome de arquivo
#                 cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
#                 json_file_path = f"users_json/{cpf}.json"

#                 if os.path.exists(json_file_path):
#                     os.remove(json_file_path)
#                     print(f"Arquivo JSON {cpf_formatado}.json excluído.")
#             else:
#                 print("O usuário não foi encontrado.")


# def cadastro_user(users):

#     while True:
#         first_name = input("Digite seu primeiro nome: ").strip(" #@!$%^&*")
#         if not first_name.isalpha():
#             print("Por favor, digite apenas letras.")
#             continue
#         first_name = re.sub(r'[^a-zA-Z]', '', first_name)
#         break

#     while True:
#         last_name = input("Digite seu sobrenome: ").strip(" #@!$%^&*")
#         if not last_name.isalpha():
#             print("Por favor, digite apenas letras.")
#             continue
#         last_name = re.sub(r'[^a-zA-Z]', '', last_name)
#         break

#     while True:
#         cpf = input("Digite o seu CPF: ").strip(" #@!$%^&*")
#         if not cpf.isdigit() or len(cpf) != 11:
#             print("CPF inválido. Verifique a quantidade de dígitos.")
#             continue

#         cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
#         cpf = cpf_formatado

#         cpf_existente = any(user.cpf == cpf for user in users)
#         json_folder = "users_json"
#         if os.path.exists(json_folder):
#             json_files = os.listdir(json_folder)
#             cpf_existente_json = any(f"{cpf}.json" == json_file for json_file in json_files)
#         else:
#             cpf_existente_json = False

#         # Se o CPF já existir em qualquer lugar, exibir uma mensagem
#         if cpf_existente or cpf_existente_json:
#             print("Este CPF já está cadastrado. Por favor, tente outro CPF.")
#             continue
#         break

#     while True:
#         email = input("Digite o seu email: ").lower().strip(" #@!$%^&*")#testar o re
#         padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
#         if not re.match(padrao, email):
#             print("Porfavor verifique o formato do seu email")
#             continue
#         else:
#             break

#     while True:
#         id_password = input("Crie uma Senha: ")
#         id_input = input("Digite a sua senha novamente para verificar: ")
#         if id_password != id_input:
#             print("As senhas não correspondem. Tente novamente.")
#             continue

#         user = User(first_name, last_name, cpf, email, id_password)
#         user.hash_password()
#         users.append(user)


#         database_folder = "users_json"
#         if not os.path.exists(database_folder):
#             os.makedirs(database_folder)


#         json_file_path = os.path.join(database_folder, f"{user.cpf}.json")

#         # Create the folder if it doesn't exist
#         if not os.path.exists(json_file_path):
#             with open(json_file_path, "w") as arquivo_json:
#                 json.dump(user.to_dict(), arquivo_json)
#             print("Usuário cadastrado com sucesso.")
#         else:
#             print("O arquivo JSON já existe para este usuário.")

#         return user

# def carregar_user(app_state):
#     users = app_state.users
#     bikes = app_state.bikes

#     if not users:
#         print("Nenhum usuario cadastrado")
#         return

#     while True:
#         cpf = input("Digite o seu CPF: ").strip(" #@!$%^&*")
#         id_password = input("Digite a Senha do usuario: ")
#         if not cpf.isdigit() or len(cpf) != 11:
#             print("CPF inválido. Verifique a quantidade de dígitos.")
#             continue
#         cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
#         cpf = cpf_formatado
#         for user in users:
#             if user.verify_password(id_password):
#                 try:
#                     # Tente carregar os dados do usuário a partir do arquivo JSON
#                     json_file_path = os.path.join("users_json", f"{cpf_formatado}.json")

#                     with open(json_file_path, "r") as arquivo_json:
#                         dados_usuario = json.load(arquivo_json)

#                     # Crie um objeto User a partir dos dados carregados
#                     user = User(
#                         dados_usuario["first_name"],
#                         dados_usuario["last_name"],
#                         dados_usuario["cpf"],
#                         dados_usuario["email"],
#                         dados_usuario["password"]
#                     )

#                     # Carregue as bicicletas do usuário
#                     for bike_info in dados_usuario["bikes"]:

#                         bike = Bike(
#                             user=user,
#                             brand=bike_info["brand"],
#                             bike_type=bike_info["bike_type"],
#                             serial_number=bike_info["serial_number"],
#                             year=bike_info["year"],
#                             value=bike_info["value"],
#                             additional_modifications=bike_info.get("additional_modifications", [])
#                         )
#                         user.bikes.append(bike)


#                     print("Informações do usuário carregado:")
#                     print(f"Nome: {user.first_name} {user.last_name}")
#                     print(f"CPF: {user.cpf}")
#                     print(f"Email: {user.email}")
#                     print(f"Bikes: {user.bikes}")
#                     for bike in user.bikes:
#                         print(f"Marca: {bike.brand}")
#                         print(f"Tipo: {bike.bike_type}")
#                         print(f"Número de Série: {bike.serial_number}")
#                         print(f"Ano: {bike.year}")
#                         print(f"Valor: {bike.value}")
#                         print(f"Modificações Adicionais: {', '.join(bike.additional_modifications)}")

#                     return user


#                 except FileNotFoundError:
#                     print(f"Arquivo JSON para o usuário {cpf_formatado} não encontrado.")
#                     return None
#         break
