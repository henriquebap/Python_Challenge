from menu import MainMenu  # Import the MainMenu class from your Menu module
from database import crud  # Import your database-related functions


def main():
    main_menu = MainMenu()
    main_menu.root.mainloop()


if __name__ == "__main__":
    main()
