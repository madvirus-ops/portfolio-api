import sys

sys.path.append("./")
from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session
from helpers.biodata_help import create_biodata, get_biodata,get_all_biodatas,update_biodata,delete_biodata
from connections.database import get_db
from rest_api.rest_schema import BioDataIn, BioDataOut,AllBioData,BioDataUpdate


router = APIRouter(prefix="/api/v1/biodata", tags=["Bio Data Router"])


@router.post("/")
async def create_biodata_route(
    body: BioDataIn, response: Response, db: Session = Depends(get_db)
):
    result = create_biodata(body, db)
    response.status_code = result["code"]
    return result

@router.get("/",response_model=list[AllBioData])
async def get_all_biodata_routes(response: Response, db: Session = Depends(get_db)):
    result = get_all_biodatas(db)
    response.status_code = result["code"]
    if result["code"] == 200:
        return result["data"]
    
    else:
        raise HTTPException(
            404, {"code": 404, "status": "error", "message": "No biodata Found"}
        )
    

@router.get("/{biodata_id}", response_model=BioDataOut)
async def get_biodata_route(
    biodata_id: str, response: Response, db: Session = Depends(get_db)
):
    result = get_biodata(biodata_id, db)
    response.status_code = result["code"]
    if result["code"] == 200:
        return result["data"]
    else:
        raise HTTPException(
            404, {"code": 404, "status": "error", "message": "biodata does not exist"}
        )
    
@router.patch("/{biodata_id}")
async def update_biodata_route(biodata_id: str, body: BioDataUpdate,response: Response, db: Session = Depends(get_db)):
    result = update_biodata(biodata_id,body,db)
    response.status_code = result["code"]
    return result

@router.delete("/{biodata_id}",response_description="deleted successfuly")
async def delete_biodata_route(biodata_id: str,response: Response, db: Session = Depends(get_db)):
    result = delete_biodata(biodata_id,db)
    response.status_code = result["code"]