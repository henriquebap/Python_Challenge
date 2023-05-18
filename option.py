def option():
    print("1 - Realizar o login")
    print("2 - Criar um cadastro")
    print("3 - Remover um usuário cadastrado")
    print("0 - Sair")
    try:
        Option = int(input())
        return Option
    except ValueError:
        print("Porfavor digite um opcao com o numero")
    except:
        print("Digite uma opcao valida")

def opt_bike():
    print("1 - Cadastrar uma bike no seguro")
    print("2 - Realizar uma vistoria de uma bike - (Not ready)")
    print("3 - Visualizar o processo do seguro")
    print("4 - Editar uma bike cadastrada")
    print("5 - Remover uma bike do cadastro")
    print("0 - Sair")
    try:
        inp_bike = int(input())
        return inp_bike
    except ValueError:
        print("Digite um valor valido para a opcao")
    except:
        print("Digite uma opcao valida")


def try_and_except():
    pass
