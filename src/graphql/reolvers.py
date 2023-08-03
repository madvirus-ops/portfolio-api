from connections.database import get_db
from sqlalchemy.orm import  Session
from connections.models import *


def certificates_resolver(biodata_id):
    try:
        db:Session = get_db()
        result = db.query(ProfessionCertificate).filter(ProfessionCertificate.biodata_id == biodata_id).first()
        return result
    except Exception as e:
        print(e.args)
