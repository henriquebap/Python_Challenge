def edit_bike(bikes):
    bike_id = input("Digite o ID da bike que deseja editar: ")
    for bike in bikes:
        if bike.serial_number == bike_id: #se a entrada do usuario for de acordo com um Numero de serie de uma bike existente ele continua
            print("Bike selecionada:")
            print(bike) #Mostra a bike puxando o __str__
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
            while True:    
                print(f'O nome da sua marca da sua bike atualmente e {bike.brand}')
                new_name = input("Digite o nome da marca corretamente(Deixe em branco para manter o mesmo): ")
                if new_name.strip() != "": #condicional que se ele deixar vazio ele continua com o mesmo valor inicial
                    break
                elif not new_name.isalpha():
                    print("Por favor, digite o nome somente com letras")
                    continue    
                bike.brand = new_name
                    #verificar o erro de loop infinito nao deixando o vazio ser uma opcao de entrada
            while True:
                print("Tipos de bike disponíveis:")
                for bike_type in bike_types:
                    print(bike_type.name)
                print("---"*40)
                print(f"O Tipo atual da sua bike e {bike.bike_type.name}")
                new_type = input("Corriga o Tipo de bike (Deixe em branco para manter o mesmo): ")
                if new_type.strip() != "":
                    break
                elif not any(new_type.lower() == bike_type.name.lower() for bike_type in bike_types):
                    print("Por favor, Digite um tipo de bike Valido.")
                    continue    
                bike.bike_type = new_type
            f'\n'
            print("---"*40)
            while True:
                print(f"O ano atual da sua bike e {bike.year}")
                new_year = input("Corriga o Ano da sua bike (Deixe em branco para manter o mesmo): ")
                if new_year.strip() != "":
                    break
                elif not new_year.isdigit() or len(new_year) != 4:
                    print("Ano inválido. Digite um ano válido com 4 dígitos.")
                    continue
                current_year = datetime.now().year
                if int(new_year) > current_year:
                    print("Ano inválido. Um ano ate o ano atual.")
                    continue
                bike.year = new_year
            print("Bike atualizada com sucesso.")
            return

    print("Bike não encontrada.")


while True:
        print("Tipos de bike disponíveis:")
        for bike_type in bike_types: #Para todos os tipos de bike no BikeType mostra todos os nomes
            print(bike_type.name)
        bike_type_input = input("Digite o tipo da bike: ").strip(" #@!$%^&*")
        if not any(bike_type_input.lower() == bike_type.name.lower() for bike_type in bike_types): #Se a entrada do ususario nao for nenhuma opcao dada, retorna erro
            print("Por favor, Digite um tipo de bike Valido.")
            continue
        break