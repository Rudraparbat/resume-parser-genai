from sqlalchemy import Column , String, Integer , JSON 
from database import Base

class ResumeData(Base) :
    __tablename__ = "resume_data"

    id = Column(Integer , primary_key=True)
    filename = Column(String)
    filepath = Column(String)
    fullname = Column(String)
    parsed_data = Column(String)
