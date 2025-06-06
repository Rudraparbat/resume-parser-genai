from fastapi import FastAPI , Request , HTTPException , UploadFile , File , Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import *
from models import *
from typing import Annotated
import asyncio
from ai import *
import os
from frontend  import *
from utils import *
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(routers)

allow_origin = [
    "http://127.0.0.1:8000",
]
# include middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

# Start the FastAPI application with a redirect to the resume parser Frontend
@app.get("/")
async def main():
    return RedirectResponse(url="/resume-parser/")


# Initializing file and db dependencies
file_dependency = Annotated[UploadFile , File(...)]
db_dependency = Annotated[Session, Depends(get_db)]

# Directory to store uploaded resumes
UPLOAD_DIR = "uploaded_resumes/"
# Ensure the upload directory exists if not then creating it
os.makedirs(UPLOAD_DIR , exist_ok=True)


@app.post("/upload_resume" , status_code=200)
async def Resumeuploader(file : file_dependency , db : db_dependency) :
    try : 
        filename = file.filename
        filepath = os.path.join(UPLOAD_DIR , filename)

        # Check the file type and extract text accordingly
        if str(filename).endswith(".pdf") :
            await SaveResume(filepath , file)
            parsed_text = await pdf_extracter(filepath)

        elif str(filename).endswith(".docx") :
            await SaveResume(filepath , file)
            parsed_text = await docx_extractor(filepath)

        else :
            return HTTPException(status_code=400 , detail= "It only support pdf and docx files")

        # Parsing the resume using ResumeParserAI
        resumeparserai = ResumeParserAI(parsed_text)
        parsed_data = await  resumeparserai.Resumeaparser()

   
        clean_json = await cleanJson(parsed_data)
        load_data = json.loads(clean_json)

        # Started async task for data saving
        asyncio.create_task(SaveDataTodb(load_data , filename , filepath , db))

        return {
            "file name" : filename , 
            "file path" : filepath,
            "parsed_data" : load_data
        }
    except Exception as e :
        db.rollback()
        raise HTTPException(status_code= 500 , detail=str(e))


@app.get("/get_resumes/" ,name="get_resumes" , status_code= 200)
async def GetUploadedResumeDetails(db : db_dependency) :
    try :
        # Fetch Resume details from the database
        resume_details = db.query(ResumeData).all()

        # Decode the parsed data for each resume
        for resumes in resume_details :
            resumes.parsed_data = await decode_parsed_data(resumes.parsed_data)

        return resume_details
    
    except Exception as e :
        return HTTPException(status_code= 500 , detail= str(e))


@app.get("/resume/details/{ids}" ,name="resume_detail_by_id" ,  status_code= 200) 
async def GetPerResumeDetails(ids : int , db : db_dependency) :
    try :
        # Fetch the specific resume details by ID
        resume_detail = db.query(ResumeData).get(ids)

        if not resume_detail:
            return  HTTPException(status_code=404, detail="Resume not found")

        resume_detail.parsed_data = await decode_parsed_data(resume_detail.parsed_data)
        return resume_detail

    except Exception as e :
        return HTTPException(status_code= 500 , detail= str(e))


# Endpoint to download the resume file
@app.get("/download/resume/" ,name= "download_resume", status_code= 200) 
async def download_resume(file_path: str):
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(
        path=file_path,
        filename=os.path.basename(file_path),  
        media_type='application/octet-stream'  
    )
