import sys

sys.path.append("./")

from pydantic import BaseModel, EmailStr
from typing import Optional, Union
from datetime import date, datetime


class BioDataIn(BaseModel):
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


class BioDataOut(BioDataIn):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True


class AllBioData(BaseModel):
    id: str
    first_name: str
    gender: str
    email: str
    nationality: str
    created_at: datetime

    class Config:
        orm_mode = True


class BioDataUpdate(BaseModel):
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    location: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    nationality: Optional[str] = None
    languages: Optional[str] = None
    interests: Optional[str] = None
    headline: Optional[str] = None


class EducationIn(BaseModel):
    biodata_id: str
    school_name: str
    course: str
    degree_type: str
    year_entered: date
    year_finished: date


class EducationOut(EducationIn):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True


class AllEducation(BaseModel):
    id: str
    biodata_id: str
    school_name: str
    created_at: datetime

    class Config:
        orm_mode = True


class EducationUpdate(BaseModel):
    biodata_id: Optional[str] = None
    school_name: Optional[str] = None
    course: Optional[str] = None
    degree_type: Optional[str] = None
    year_entered: Optional[date] = None
    year_finished: Optional[date] = None


# EducationIn,EducationOut,EducationUpdate,  AllEducation


class CertificateIn(BaseModel):
    biodata_id: str
    issuer: str
    certificate_type: str
    year_issued: date


class CertificateOut(CertificateIn):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True


class CertificateUpdate:
    biodata_id: Optional[str] = None
    issuer: Optional[str] = None
    certificate_type: Optional[str] = None
    year_issued: Optional[date] = None


class AllCertificate(BaseModel):
    id: str
    biodata_id: str
    issuer: str

    class Config:
        orm_mode = True
