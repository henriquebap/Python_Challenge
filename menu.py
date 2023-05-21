#Imports necessary imports
from option import option, opt_bike
from user import login, remove_user, cadastro_user
from bike import cad_bike, edit_bikes, remove_bike, list_user_bike

#improve all of these dictionarys
bikes =[]
users = []

#While True para ficar em loop 
while True:
    #Tratamento de execao 
    try:
        print("---"*40)
        print("Olá, Selecione uma opcao para executar uma ação.")
        Option = option()
    except ValueError:
        print("Opcai Invalida. Por favor, digite um numero valido.")
        continue
    #Funcao da primeira opcao de input
    if Option == 1:
        user = login(users)
        if user:
            print(f"Seja Bem-vindo {user.first_name}, vamos continuar com o seu processo")
            #Entra no laco de Opcao bike, funcoes direcionadas a bike
            while True:
                inp_bike = opt_bike()
                if inp_bike == 0: 
                    break
                if inp_bike == 1:
                    bike = cad_bike(user) #Cria uma bike
                    bikes.append(bike)
                #elif inp_bike == 2:
                 #   pass
                    #bike = survey_bike(bikes)
                    #bike_img.append(bike)
                elif inp_bike == 2:
                    list_user_bike(user)#Mostra bikes atreladas ao perfil logado
                elif inp_bike == 3:
                    edit_bikes(user.bikes)#Modifica entradas que foram digitadas errado e adiciona itens (modificacoes + valor da modificao)
                elif inp_bike == 4:#Remove a bike do perfil do ususario
                    remove_bike(bikes, user)
        else:
            print("Nao foi encontrado o usuario") #Se o ususario colocado na entrada nao estiver cadastrado ele retona uma mensagem
            confirm = input("Gostaria de Criar um Usuario? (s/n): ")
            while confirm.lower() not in ["s", "n"]:
                print("Por favor, digite 's' para Sim ou 'n' para Não.")
                confirm = input("Gostaria de criar um usuário? (s/n): ")
            if confirm.lower() == "s": #Condicional se a entrada for "sim"
                user = cadastro_user(users) #funcao cadastrar usuario
                print("Usuário cadastrado com sucesso.")
                users.append(user)
            else:
                continue
    elif Option == 2: #Input 2 chama a funcao cadastro dentro dessa condicao
        user = cadastro_user(users)
        users.append(user) #atrela user dentro da lista users
    elif Option == 3: 
        remove_user(users) #condicao do input 3 chama a funcao remover usuario 
    elif Option == 0:
        break #Condicao do input 0 finaliza o programa
    else:
        print("Digite um numero funcional")