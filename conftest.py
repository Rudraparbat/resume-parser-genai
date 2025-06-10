import pytest
from main import get_db
from models import ResumeData

@pytest.fixture(scope="session", autouse=True)
def clear_db_once():
    db = next(get_db())  
    print("clearing Database")
    db.query(ResumeData).delete()
    db.commit()
    db.close()


