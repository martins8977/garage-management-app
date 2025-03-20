from sqlmodel import Session
from app.database import engine
from app.models.user import User
from app.core.security import get_password_hash

def seed():
    user = User(
        username="admin",
        email="admin@example.com",
        hashed_password=get_password_hash("admin"),
        is_active=True,
        is_superuser=True
    )

    with Session(engine) as session:
        existing = session.query(User).filter(User.username == user.username).first()
        if existing:
            print("Admin user already exists.")
            return

        session.add(user)
        session.commit()
        print("Admin user created successfully.")

if __name__ == "__main__":
    seed()
