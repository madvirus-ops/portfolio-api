import sys
sys.path.append("./")

from pydantic import BaseModel,EmailStr
from typing import Optional,Union
from datetime import date


class BioDataIn(BaseModel):
    first_name :str
    middle_name :str
    last_name :str
    email :str
    location :str
    date_of_birth:date
    gender :str
    nationality :str
    languages :str
    interests :str
    headline :str

class BioDataOut(BioDataIn):
    id:str

    class Meta:
        orm_mode = True

class AllBioData(BaseModel):
    id:str
    first_name :str
    gender :str
    email:str
    nationality :str



class BioDataUpdate(BaseModel):
    first_name :Optional[str] = None 
    middle_name :Optional[str] = None 
    last_name :Optional[str] = None 
    email :Optional[EmailStr] = None 
    location :Optional[str] = None 
    date_of_birth:Optional[date] = None
    gender :Optional[str] = None 
    nationality :Optional[str] = None 
    languages :Optional[str] = None 
    interests :Optional[str] = None 
    headline :Optional[str] = None 