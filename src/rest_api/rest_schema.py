import sys
sys.path.append("./")

from pydantic import BaseModel
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