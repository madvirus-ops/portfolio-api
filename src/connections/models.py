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
        primaryjoin="BioData.id==SkillSets.id",
        foreign_keys="[SkillSets.id]",
    )


class SkillSets(AbstractModel):
    __tablename__ = "skill_sets"
    skill_name = Column(String(255), default="")
    skill_level = Column(Integer, default=100)
    efficiency = Column(Integer, default=100)
    biodata = relationship("BioData", back_populates="skill_sets")
