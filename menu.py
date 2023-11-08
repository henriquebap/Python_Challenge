import tkinter as tk
from tkinter import messagebox
from database import crud
import api_ia
from database import models
from tkinter import filedialog


class MainMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Main Menu")

        self.user = None  # Store the user information

        self.options = [
            ("Menu User", self.menu_user),
            ("Sair", self.root.quit),
        ]

        self.submenu = None

        self.create_menu()

    def create_menu(self):
        for i, (option_text, option_action) in enumerate(self.options):
            tk.Button(
                self.root,
                text=option_text,
                command=option_action,
            ).pack(fill=tk.X)

    def menu_user(self):
        if self.user is None:
            user_info = self.create_user()
            if user_info:
                self.user = user_info
        if self.user:
            self.root.destroy()
            self.submenu = UserMenu(self.user)
            self.submenu.create_menu()
            self.submenu.root.mainloop()

    def create_user(self):
        user_info = crud.create_user()
        messagebox.showinfo("User Created", "User created successfully.")
        return user_info


class UserMenu:
    def __init__(self, user):
        self.user = user
        self.root = tk.Tk()
        self.root.title("User Menu")

        self.options = [
            ("Menu Bike", self.menu_bike),
            ("Mostrar Perfil", self.carregar_user),
            ("Excluir Conta", self.remove_user),
            ("Sair", self.root.quit),
        ]

        self.submenu = None

    def create_menu(self):
        for i, (option_text, option_action) in enumerate(self.options):
            tk.Button(
                self.root,
                text=option_text,
                command=option_action,
            ).pack(fill=tk.X)

    def menu_bike(self):
        if self.user:
            self.root.destroy()
            self.submenu = BikeMenu(self.user)
            self.submenu.create_menu()
            self.submenu.root.mainloop()

    def carregar_user(self):
        user_info = crud.read_user(self.user)
        messagebox.showinfo(
            "Perfil",
            f"Nome: {user_info.first_name} {user_info.last_name}\nCPF: {user_info.cpf}\nEmail: {user_info.email}",
        )

    def remove_user(self):
        crud.delete_user(self.user)
        messagebox.showinfo("Conta Excluída", "Sua conta foi excluída com sucesso.")
        self.root.quit()


class BikeMenu:
    def __init__(self, user):
        self.user = user
        self.root = tk.Tk()
        self.root.title("Bike Menu")

        self.options = [
            ("Enviar Imagens da Bike", self.pred_ia),
            ("Editar uma Bike", self.edit_bikes),
            ("Remover uma Bike criada", self.remove_bike),
            ("Listar Bikes cadastradas", self.list_user_bikes),
            ("Voltar ao Menu Principal", self.return_to_main_menu),
        ]

    def create_menu(self):
        for i, (option_text, option_action) in enumerate(self.options):
            tk.Button(
                self.root,
                text=option_text,
                command=option_action,
            ).pack(fill=tk.X)

    def pred_ia(self):
        # Create a file dialog to select an image file
        file_path = filedialog.askopenfilename(
            title="Select an image",
            filetypes=(("Image files", "*.jpg *.png *.jpeg"), ("All files", "*.*")),
        )

        if file_path:
            # Pass the selected image file to the cv_api function
            (
                image_path,
                prediction_image_path,
                predicted_class,
                confidence,
            ) = api_ia.cv_api(file_path)

            # Create a bicycle associated with the user
            new_bike = crud.create_bike(self.user)

            # Create an instance of PredictionResult with the API information
            api_response = models.PredictionResult(
                image_path=image_path,
                prediction_image_path=prediction_image_path,
                predicted_class=predicted_class,
                confidence=confidence,
                bike_id=new_bike.bike_id,  # Make sure you use the correct attribute for bike_id
            )

    def cad_bike(self):
        crud.create_bike(self.user)

    def edit_bikes(self):
        crud.update_bike(self.user)

    def remove_bike(self):
        crud.delete_bike(self.user)

    def list_user_bikes(self):
        # Fetch and list user's bikes
        user_bikes = crud.read_bike(self.user)
        if user_bikes:
            for bike in user_bikes:
                print(f"Brand: {bike.brand}, Serial Number: {bike.serial_number}")
        else:
            print("No bikes found for this user.")

    def return_to_main_menu(self):
        self.root.destroy()
        main_menu = MainMenu(self.user)
        main_menu.create_menu()
        main_menu.root.mainloop()
