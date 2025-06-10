from fastapi.testclient import TestClient
import os
from main import *
from models import *


client =TestClient(app)

def test_main() :
    response = client.get("/")
    assert response.status_code == 200
    assert str(response.url).endswith("/resume-parser/") == True


def test_upload_resume() :
    file_path = os.path.join(os.getcwd() , "sample_data/RudraParbat-pythondeveloper.pdf")
    with open(file_path , "rb") as file :
        response = client.post("/upload_resume/" , files={"file": file})
    assert response.status_code == 200
    assert response.json().get("filename") == "RudraParbat-pythondeveloper.pdf"

def test_get_resume() :
    response  = client.get("/get_resumes/")
    response_data =  response.json()
    assert response.status_code == 200
    assert  response_data.get("message") == "SUCCESS"
    assert response_data.get("Fetched_Data") == True


