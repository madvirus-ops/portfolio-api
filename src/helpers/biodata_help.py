import sys

sys.path.append("./")
from connections.models import BioData,tz
from sqlalchemy.orm import Session
from connections.database import get_db
from rest_api.rest_schema import BioDataIn,BioDataUpdate
from datetime import datetime
from settings import settings




# helper
def function_name():
    try:
        pass
    except Exception as e:
        print(e.args)
        return {"code": 400, "status": "error", "message": e.args}


def create_biodata(details: BioDataIn, db: Session):
    try:
        new = db.query(BioData).filter(BioData.email == details.email).first()
        if new is None:
            create = BioData(**details.model_dump())
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
        settings.LOGGER.error(e.args)
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
        settings.LOGGER.error(e.args)
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
        settings.LOGGER.error(e.args)
        return {"code": 400, "status": "error", "message": e.args}
    

def update_biodata(biodata_id: str,details: BioDataUpdate, db: Session):
    try:
        fetch = db.query(BioData).filter(BioData.id == biodata_id).first()
        if fetch is None:
            return {
                "code": 404,
                "status": "error",
                "message": "Biodata Not Found",
            }
        fetch.updated_at = datetime.now(tz)
        hero_data = details.model_dump(exclude_unset=True)
        for key, value in hero_data.items():
            setattr(fetch, key, value)
        db.add(fetch)
        db.commit()
        settings.LOGGER.error(f"{biodata_id} updated")
        return {"code":200,"status":"success","message":f"{biodata_id} updated"}
    except Exception as e:
        print(e.args)
        settings.LOGGER.error(e.args)
        return {"code": 400, "status": "error", "message": e.args}
    

def delete_biodata(biodata_id: str, db: Session):
    try:
        fetch = db.query(BioData).filter(BioData.id == biodata_id).first()
        if fetch is None:
            return {
                "code": 404,
                "status": "error",
                "message": "Biodata Not Found",
            }
        db.delete(fetch)
        db.commit()
        settings.LOGGER.info(f"{biodata_id} deleted")
        return {"code": 200, "data": fetch,"message":f"{biodata_id} deleted"}
    except Exception as e:
        print(e.args)
        settings.LOGGER.error(e.args)
        return {"code": 400, "status": "error", "message": e.args}