from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from api.main import app
from api.config import settings
from api.database import get_db
from api.database import Base
from alembic import command

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password123@localhost:5432/fastapi_test'
# SQLALCHEMY_DATABASE_URL = f"{settings.database_url}_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
# engine = create_engine(settings.database_url)

TestingSessionLocal = sessionmaker(autocommit= False, autoflush= False, bind= engine)
# Base.metadata.create_all(bind= engine)
# Base = declarative_base()

#dependency
# def override_get_db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# app.dependency_overrides[get_db] = override_get_db


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind= engine)
    Base.metadata.create_all(bind= engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()




# client = TestClient(app)

@pytest.fixture()
def client(session):
    # Base.metadata.drop_all(bind= engine)
    # run our code before we run our test
    # Base.metadata.create_all(bind= engine)
    # command.upgrade("head")
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db  
    yield TestClient(app)
    # command.downgrade("base")
    # run our code after our test finishes
    # Base.metadata.drop_all(bind= engine)
