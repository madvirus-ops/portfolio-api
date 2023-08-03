import sys
sys.path.append("./")
import strawberry
from datetime import datetime,date

@strawberry.type
class BioData:
    first_name: str
    middle_name: str
    last_name: str
    email: str
    location: str
    date_of_birth: date
    gender: str
    nationality: str
    languages: str
    interests: str
    headline: str
    education: "Education"
    biodata:"Certificate"


@strawberry.type
class Education:
    biodata_id:str
    school_name: str
    course: str
    degree_type: str
    year_entered: date
    year_finished: date
    biodata: "BioData"


@strawberry.type
class Certificate:
    biodata_id: str
    issuer: str
    certificate_type: str
    year_issued: date
    biodata: "BioData"
