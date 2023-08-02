import sys
sys.path.append("./")
from fastapi import APIRouter,Depends,Response,status
from sqlalchemy.orm import Session
from ..helpers.biodata import create_biodata
from ..connections.database import get_db
from .rest_schema import BioDataIn


router = APIRouter(prefix="/api/v1/biodata",tags=['Bio Data Router'])



@router.post("/")
async def create_biodata_route(body:BioDataIn,response:Response,db:Session = Depends(get_db)):
    result = create_biodata(body,db)
    response.status_code = result['code']
    return result

