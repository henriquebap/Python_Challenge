from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from database import models

SQLALCHEMY_DATABASE_URL = (
    "oracle+oracledb://RM97796:280703@oracle.fiap.com.br/?service_name=orcl"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    bind=engine, autoflush=False, autocommit=False, expire_on_commit=False
)

Base = declarative_base()


# api_response = models.PredictionResult(data=prediction_result)
# SessionLocal.add(api_response)
# SessionLocal.commit()
