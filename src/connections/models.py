import sys

sys.path.append("./")
from sqlalchemy import (
    Column,
    DateTime,
    Boolean,
    Integer,
    String,
    Text,
    ForeignKey,
    Date,
)
from datetime import datetime
import pytz
import uuid
from sqlalchemy.orm import relationship


tz = pytz.timezone("Africa/Lagos")


from .database import Base


class AbstractModel(Base):
    """Might switch to uuid soon, idk :)"""

    __abstract__ = True
    pkid = Column(Integer, primary_key=True)
    id = Column(String(255), default=uuid.uuid4, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())


class BioData(AbstractModel):
    __tablename__ = "bio_data"
    first_name = Column(String(255), default="")
    middle_name = Column(String(255), default="")
    email = Column(String(255),default="")
    location = Column(String(255),default="")
    last_name = Column(String(255), default="")
    date_of_birth = Column(Date, default=datetime.date)
    gender = Column(String(255), default="male")
    nationality = Column(String(255), default="")
    languages = Column(String(255), default="")
    interests = Column(Text, default="")
    headline = Column(Text, default="")
    skill_sets = relationship(
        "SkillSets",
        back_populates="biodata",
        cascade="all, delete-orphan",
        primaryjoin="BioData.id==SkillSets.biodata_id",
        foreign_keys="[SkillSets.biodata_id]",
    )
    soft_skills = relationship(
        "SoftSkills",
        back_populates="biodata",
        cascade="all, delete-orphan",
        primaryjoin="BioData.id==SoftSkills.biodata_id",
        foreign_keys="[SoftSkills.biodata_id]",
    )
    work_experience = relationship(
        "WorkExperience",
        back_populates="biodata",
        cascade="all, delete-orphan",
        primaryjoin="BioData.id==WorkExperience.biodata_id",
        foreign_keys="[WorkExperience.biodata_id]",
    )
    personal_projects = relationship(
        "PersonalProjects",
        back_populates="biodata",
        cascade="all, delete-orphan",
        primaryjoin="BioData.id==PersonalProjects.biodata_id",
        foreign_keys="[PersonalProjects.biodata_id]",
    )
    socials  = relationship(
        "Socials",
        back_populates="biodata",
        cascade="all, delete-orphan",
        primaryjoin="BioData.id==Socials.biodata_id",
        foreign_keys="[Socials.biodata_id]",
    )
    contact  = relationship(
        "Contact",
        back_populates="biodata",
        cascade="all, delete-orphan",
        primaryjoin="BioData.id==Contact.biodata_id",
        foreign_keys="[Contact.biodata_id]",
    )


class SkillSets(AbstractModel):
    __tablename__ = "skill_sets"
    biodata_id = Column(String(255), ForeignKey("bio_data.id"), nullable=False)
    skill_name = Column(String(255), default="")
    skill_level = Column(Integer, default=100)
    efficiency = Column(Integer, default=100)
    biodata = relationship("BioData", back_populates="skill_sets")



class SoftSkills(AbstractModel):
    __tablename__ = "soft_skills"
    biodata_id = Column(String(255), ForeignKey("bio_data.id"), nullable=False)
    skill_name = Column(String(255), default="")
    skill_description = Column(Text, default="")
    skill_level = Column(Integer, default=100)
    biodata = relationship("BioData", back_populates="soft_skills")

    
class WorkExperience(AbstractModel):
    __tablename__ = "work_experience"
    biodata_id = Column(String(255), ForeignKey("bio_data.id"), nullable=False)
    start_date = Column(Date, default=datetime.date)
    end_date = Column(Date, default=datetime.date)
    company_name  = Column(String(255), default="")
    company_location =  Column(String(255), default="")
    responsibility  = Column(Text, default="")
    biodata = relationship("BioData", back_populates="work_experience")



class PersonalProjects(AbstractModel):
    __tablename__ = "personal_projects"
    biodata_id = Column(String(255), ForeignKey("bio_data.id"), nullable=False)
    project_name = Column(String(255), default="")
    project_description = Column(Text,default="")
    project_url = Column(String(255), default="")
    image_url = Column(String(255), default="")
    biodata = relationship("BioData", back_populates="personal_projects")

class Socials(AbstractModel):
    __tablename__ = "socials"
    biodata_id = Column(String(255), ForeignKey("bio_data.id"), nullable=False)
    name = Column(String(255), default="")
    url = Column(String(255), default="")
    biodata = relationship("BioData", back_populates="socials")



class Contact(AbstractModel):
    __tablename__ = "contact"
    biodata_id = Column(String(255), ForeignKey("bio_data.id"), nullable=False)
    name = Column(String(255), default="")
    subject = Column(String(255), default="")
    email = Column(String(255), default="")
    message = Column(Text,default="")
    biodata = relationship("BioData", back_populates="contact")