from menu import MainMenu
from app_state import AppState
import user_tools
import sys

def main():
    app_state = AppState()
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
                while True:
                    main_menu.show_options()
                    main_menu.user_input()
                    return_to_main_menu = input("Deseja voltar ao menu principal? (S/N): ").strip().upper()
                    if return_to_main_menu == "S":
                        break
                    else:
                        continue
                
            else:
                print("Falha no login. Tente novamente.")

        elif choice == "2":  # Opção de registro
            user = user_tools.cadastro_user(app_state.users)  # Passe a lista de usuários como argumento
            app_state.users.append(user)  # Adicione o usuário à lista em app_state
            app_state.current_user = user  # Configure o usuário atual em app_state
            print("Registro bem-sucedido!")
            while True:
                main_menu.show_options()
                main_menu.user_input()
                return_to_main_menu = input("Deseja voltar ao menu principal? (S/N): ").strip().upper()
                if return_to_main_menu == "S":
                    break
                else:
                    continue
            

        elif choice == "3":
            print("Saindo do Programa")  # Opção de sair
            sys.exit()

        
        

if __name__ == "__main__":
    main()
