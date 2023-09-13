# app_state.py
class AppState:
    def __init__(self):
        self.current_user = None
        self.users = []
        self.bikes = []

    def set_current_user(self, user):
        self.current_user = user

    def get_current_user(self):
        return self.current_user

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    # Métodos para gerenciar bicicletas podem ser adicionados, se necessário
