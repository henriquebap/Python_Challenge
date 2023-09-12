from menu import MainMenu

def main():
    menu = MainMenu()      
    while True:
        menu.show_options()
        menu.user_input()
        if input("Deseja Sair do programa? S/N: ").strip().upper() == "S":
            break

if __name__ == '__main__':
    main()