from sqlmodel import SQLModel, create_engine

DATABASE_URL = "sqlite:///./garage.db"
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    from app.models import customer, vehicle, job, user
    SQLModel.metadata.create_all(engine)
