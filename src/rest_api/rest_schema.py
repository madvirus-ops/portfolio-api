import sys
sys.path.append("./")

from pydantic import BaseModel
from datetime import date


class BioDataIn(BaseModel):
    first_name :str
    middle_name :str
    email :str
    location :str
    last_name :str
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