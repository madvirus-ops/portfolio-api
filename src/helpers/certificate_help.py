import sys

sys.path.append("./")
from connections.models import ProfessionCertificate as Certificate,tz
from sqlalchemy.orm import Session
from connections.database import get_db
from rest_api.rest_schema import CertificateIn,CertificateUpdate
from datetime import datetime


# helper
def function_name():
    try:
        pass
    except Exception as e:
        print(e.args)
        return {"code": 400, "status": "error", "message": e.args}


def create_Certificate(details: CertificateIn, db: Session):
    try:
        create = Certificate(**details.model_dump())
        db.add(create)
        db.commit()
        db.refresh(create)
        return {
                "code": 201,
                "status": "success",
                "message": "Certificate created successfully",
                "id": create.id,
            }

    except Exception as e:
        print(e.args)
        return {"code": 400, "status": "error", "message": e.args}


def get_Certificate(certificate_id: str, db: Session):
    try:
        fetch = db.query(Certificate).filter(Certificate.id == certificate_id).first()
        if fetch is None:
            return {
                "code": 404,
                "status": "error",
                "message": "Certificate Not Found",
            }
        return {"code": 200, "data": fetch}
    except Exception as e:
        print(e.args)
        return {"code": 400, "status": "error", "message": e.args}

def get_all_Certificates(db:Session):
    try:
        fetch = db.query(Certificate).all()
        if fetch is None:
            return {
                "code": 404,
                "status": "error",
                "message": "Certificate Not Found",
            }
        return {"code": 200, "data": fetch}
    except Exception as e:
        print(e.args)
        return {"code": 400, "status": "error", "message": e.args}
    

def update_certificate(certificate_id: str,details: CertificateUpdate, db: Session):
    try:
        fetch = db.query(Certificate).filter(Certificate.id == certificate_id).first()
        if fetch is None:
            return {
                "code": 404,
                "status": "error",
                "message": "Certificate Not Found",
            }
        fetch.updated_at = datetime.now(tz)
        db.commit()
        hero_data = details.model_dump(exclude_unset=True)
        for key, value in hero_data.items():
            setattr(fetch, key, value)
        db.add(fetch)
        db.commit()
        return {"code":200,"status":"success","message":f"{certificate_id} updated"}
    except Exception as e:
        print(e.args)
        return {"code": 400, "status": "error", "message": e.args}
    

def delete_certificate(certificate_id: str, db: Session):
    try:
        fetch = db.query(Certificate).filter(Certificate.id == certificate_id).first()
        if fetch is None:
            return {
                "code": 404,
                "status": "error",
                "message": "Certificate Not Found",
            }
        db.delete(fetch)
        db.commit()
        return {"code": 200, "data": fetch,"message":f"{certificate_id} deleted"}
    except Exception as e:
        print(e.args)
        return {"code": 400, "status": "error", "message": e.args}