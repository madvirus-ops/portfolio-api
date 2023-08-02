import sys

sys.path.append("./")
from connections.models import Education,tz
from sqlalchemy.orm import Session
from connections.database import get_db
from rest_api.rest_schema import EducationIn,EducationUpdate
from datetime import datetime


# helper
def function_name():
    try:
        pass
    except Exception as e:
        print(e.args)
        return {"code": 400, "status": "error", "message": e.args}


def create_education(details: EducationIn, db: Session):
    try:
        create = Education(**details.model_dump())
        db.add(create)
        db.commit()
        db.refresh(create)
        return {
                "code": 201,
                "status": "success",
                "message": "Education created successfully",
                "id": create.id,
            }

    except Exception as e:
        print(e.args)
        return {"code": 400, "status": "error", "message": e.args}


def get_education(education_id: str, db: Session):
    try:
        fetch = db.query(Education).filter(Education.id == education_id).first()
        if fetch is None:
            return {
                "code": 404,
                "status": "error",
                "message": "Education Not Found",
            }
        return {"code": 200, "data": fetch}
    except Exception as e:
        print(e.args)
        return {"code": 400, "status": "error", "message": e.args}

def get_all_educations(db:Session):
    try:
        fetch = db.query(Education).all()
        if fetch is None:
            return {
                "code": 404,
                "status": "error",
                "message": "Education Not Found",
            }
        return {"code": 200, "data": fetch}
    except Exception as e:
        print(e.args)
        return {"code": 400, "status": "error", "message": e.args}
    

def update_education(education_id: str,details: EducationUpdate, db: Session):
    try:
        fetch = db.query(Education).filter(Education.id == education_id).first()
        if fetch is None:
            return {
                "code": 404,
                "status": "error",
                "message": "Education Not Found",
            }
        fetch.updated_at = datetime.now(tz)
        db.commit()
        hero_data = details.model_dump(exclude_unset=True)
        for key, value in hero_data.items():
            setattr(fetch, key, value)
        db.add(fetch)
        db.commit()
        return {"code":200,"status":"success","message":f"{education_id} updated"}
    except Exception as e:
        print(e.args)
        return {"code": 400, "status": "error", "message": e.args}
    

def delete_education(education_id: str, db: Session):
    try:
        fetch = db.query(Education).filter(Education.id == education_id).first()
        if fetch is None:
            return {
                "code": 404,
                "status": "error",
                "message": "Education Not Found",
            }
        db.delete(fetch)
        db.commit()
        return {"code": 200, "data": fetch,"message":f"{education_id} deleted"}
    except Exception as e:
        print(e.args)
        return {"code": 400, "status": "error", "message": e.args}