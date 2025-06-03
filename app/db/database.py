from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

# Usa variável de ambiente ou fallback padrão
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://user:password@localhost/db")

# Criação do engine e factory da session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()

# Gerador para injeção com Depends()
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
