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

