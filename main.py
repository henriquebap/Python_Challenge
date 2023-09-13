from menu import MainMenu
from app_state import AppState
import user_tools
import sys

def main():
    menu = MainMenu()      
    while True:
        menu.show_options()
        menu.user_input()
        if input("Deseja Sair do programa? S/N: ").strip().upper() == "S":
            break

if __name__ == "__main__":
    app_state = AppState()  # Crie uma instância de AppState
    app_state.users = user_tools.load_user("users_json")

    main_menu = MainMenu(app_state)

    while True:
            print("1. Login")
            print("2. Registrar")
            print("3. Sair")
            
            choice = input("Escolha uma opção: ")
            
            if choice == "1":  # Opção de login
                user = user_tools.login(app_state)  # A função de login retorna o usuário autenticado
                
                if user:
                    app_state.current_user = user  # Configure o usuário atual em app_state
                    print("Login bem-sucedido!")
                    break
                else:
                    print("Falha no login. Tente novamente.")

            elif choice == "2":  # Opção de registro
                user = user_tools.cadastro_user(app_state.users)  # Passe a lista de usuários como argumento
                app_state.users.append(user)  # Adicione o usuário à lista em app_state
                app_state.current_user = user  # Configure o usuário atual em app_state
                print("Registro bem-sucedido!")
                break

            elif choice == "3":
                print("saindo do Programa")  # Opção de sair
                sys.exit()

    main_menu.show_options()
    main_menu.user_input()