import sys

sys.path.append("./")
from connections.models import BioData
from sqlalchemy.orm import Session
from connections.database import get_db
from rest_api.rest_schema import BioDataIn


# helper
def function_name():
    try:
        pass
    except Exception as e:
        print(e.args)
        return {"code": 400, "status": "error", "message": e.args}


def create_biodata(details: BioData, db: Session):
    try:
        new = db.query(BioData).filter(BioData.email == details.email).first()
        if new is None:
            create = BioData(**details.dict())
            db.add(create)
            db.commit()
            db.refresh(create)
            return {
                "code": 201,
                "status": "success",
                "message": "Biodata created successfully",
                "id": create.id,
            }
        return {
            "code": 400,
            "status": "error",
            "message": f"biodata with details already exist, update with id `{new.id}`",
        }
    except Exception as e:
        print(e.args)
        return {"code": 400, "status": "error", "message": e.args}


def get_biodata(biodata_id: str, db: Session):
    try:
        fetch = db.query(BioData).filter(BioData.id == biodata_id).first()
        if fetch is None:
            return {
                "code": 404,
                "status": "error",
                "message": "Biodata Not Found",
            }
        return {"code": 200, "data": fetch}
    except Exception as e:
        print(e.args)
        return {"code": 400, "status": "error", "message": e.args}

def get_all_biodatas(db:Session):
    try:
        fetch = db.query(BioData).all()
        if fetch is None:
            return {
                "code": 404,
                "status": "error",
                "message": "Biodata Not Found",
            }
        return {"code": 200, "data": fetch}
    except Exception as e:
        print(e.args)
        return {"code": 400, "status": "error", "message": e.args}