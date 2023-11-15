from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Define o banco de dados e a sua conexao com o programa
SQLALCHEMY_DATABASE_URL = (
    "oracle+oracledb://RM97796:280703@oracle.fiap.com.br/?service_name=orcl"
)

# Declara a egine que vai ser usada
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    bind=engine, autoflush=False, autocommit=False, expire_on_commit=False
)

Base = declarative_base()
