from langchain_community.document_loaders import PyPDFLoader , Docx2txtLoader
from fastapi.responses import FileResponse
import os , shutil
import base64
import json
from models import *



async def SaveResume(filepath : str , file) :
    with open(filepath , "wb") as newfile :
        shutil.copyfileobj(file.file , newfile)


async def pdf_extracter(filepath : str) :
    loader = PyPDFLoader(filepath)
    pages = loader.load()
    return pages[0].page_content


async def docx_extractor(filepath : str) :
    loader = Docx2txtLoader(filepath)
    data  = loader.load()
    return data[0].page_content

async def encode_parsed_data(data) : 
    encoded_data = base64.b64encode(data.encode("utf-8")).decode("utf-8")
    return encoded_data

async def decode_parsed_data(encoded_data) :
    decoded_json_str = base64.b64decode(encoded_data.encode("utf-8")).decode("utf-8")
    decoded_data = json.loads(decoded_json_str)
    return decoded_data

async def cleanJson(parsed_data) :
    clean_json = parsed_data.strip("```json").strip("```").strip()
    clean_json = clean_json.replace('\\"', '"')
    return clean_json

async def SaveDataTodb(parsed_data , filename , filepath , db) :
    try :
    
        fullname = parsed_data.get("fullName")
        encoded_data = await encode_parsed_data(json.dumps(parsed_data))
        db_table = ResumeData()
        db_table.filename = filename
        db_table.filepath = filepath
        db_table.fullname = fullname
        db_table.parsed_data = encoded_data

        db.add(db_table)
        db.commit()
        db.refresh(db_table)
    except Exception as e :
        db.rollback()
        raise ValueError("Something wrong with database")

