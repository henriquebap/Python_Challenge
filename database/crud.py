from database import SessionLocal, models


def create_user(user_data):
    db = SessionLocal()
    try:
        user = models.User(user_data)
        db.add(user)
        db.commit()
        db.refresh(user)
    finally:
        db.close()

    return user


def read_user(user_id: int):
    db = SessionLocal()
    try:
        return db.query(models.User).filter(models.User.user_id == user_id).first()
    finally:
        db.close()


def update_user(user_id: int, user_data: dict):
    db = SessionLocal()
    try:
        user = db.query(models.User).filter(models.User.user_id == user_id).first()
        if user:
            for key, value in user_data.items():
                setattr(user, key, value)
            db.commit()
            db.refresh(user)
        return user
    finally:
        db.close()


def delete_user(user_id: int):
    db = SessionLocal()
    try:
        user = db.query(models.User).filter(models.User.user_id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
        return user
    finally:
        db.close()


def read_user_by_cpf(cpf: str):
    db = SessionLocal()
    try:
        return db.query(models.User).filter(models.User.cpf == cpf).first()
    finally:
        db.close()


def create_bike(user_id, bike_data):
    db = SessionLocal()
    try:
        new_bike = models.Bike(user_id=user_id, **bike_data)
        db.add(new_bike)
        db.commit()
        db.refresh(new_bike)
        print("Bicicleta cadastrada com sucesso.")
    finally:
        db.close()
    return new_bike


# Função para ler uma bicicleta por número de série
def read_bike(user, bike_serial_number):
    db = SessionLocal()
    try:
        bike = (
            db.query(models.Bike)
            .filter(
                models.Bike.user == user,
                models.Bike.serial_number == bike_serial_number,
            )
            .first()
        )
        if bike:
            # Exibir as informações da bicicleta
            print("Marca:", bike.brand)
            print("Modelo:", bike.bike_type.name)
            # Exibir outras informações da bicicleta
            return bike
        else:
            print("Bicicleta não encontrada.")
            return None
    finally:
        db.close()


# Função para atualizar uma bicicleta
def update_bike(user, bike_serial_number, bike_data):
    db = SessionLocal()
    try:
        bike = (
            db.query(models.Bike)
            .filter(
                models.Bike.user == user,
                models.Bike.serial_number == bike_serial_number,
            )
            .first()
        )
        if bike:
            for key, value in bike_data.items():
                setattr(bike, key, value)
            db.commit()
            db.refresh(bike)
            print("Bicicleta atualizada com sucesso.")
            return bike
        else:
            print("Bicicleta não encontrada.")
            return None
    finally:
        db.close()


# Função para deletar uma bicicleta por número de série
def delete_bike(user, bike_serial_number):
    db = SessionLocal()
    try:
        bike = (
            db.query(models.Bike)
            .filter(
                models.Bike.user == user,
                models.Bike.serial_number == bike_serial_number,
            )
            .first()
        )
        if bike:
            user.bikes.remove(bike)
            db.delete(bike)
            db.commit()
            print("Bicicleta removida com sucesso.")
        else:
            print("Bicicleta não encontrada.")
    finally:
        db.close()


# Função para criar um novo tipo de bicicleta
def create_bike_type(name, description):
    db = SessionLocal()
    try:
        bike_type = models.BikeType(name=name, description=description)
        db.add(bike_type)
        db.commit()
        db.refresh(bike_type)
    finally:
        db.close()
    return bike_type


# Função para ler um tipo de bicicleta por ID
def read_bike_type(bike_type_id: int):
    db = SessionLocal()
    try:
        return (
            db.query(models.BikeType)
            .filter(models.BikeType.bike_type_id == bike_type_id)
            .first()
        )
    finally:
        db.close()
        # Função para atualizar o nome e a descrição do tipo de bicicleta


# Função para atualizar um tipo de bicicleta por ID
def update_bike_type(bike_type_id: int, new_name: str, new_description):
    db = SessionLocal()
    try:
        bike_type = read_bike_type(db, bike_type_id)
        if bike_type:
            bike_type.name = new_name
            bike_type.description = new_description
            db.commit()
            db.refresh(bike_type)
            return bike_type
    finally:
        db.close()
    return None


# Função para deletar um tipo de bicicleta por ID
def delete_bike_type(bike_type_id: int):
    db = SessionLocal()
    try:
        bike_type = read_bike_type(db, bike_type_id)
        if bike_type:
            db.delete(bike_type)
            db.commit()
            return bike_type
    finally:
        db.close()
    return None
