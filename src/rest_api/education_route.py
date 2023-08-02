import sys

sys.path.append("./")
from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session
from helpers.education_help import (
    create_education,update_education,get_all_educations,get_education,delete_education
)
from connections.database import get_db
from rest_api.rest_schema import EducationIn,EducationOut,EducationUpdate,  AllEducation


router = APIRouter(prefix="/api/v1/education", tags=[" Education Routes"])


@router.post("/")
async def create_education_route(
    body: EducationIn, response: Response, db: Session = Depends(get_db)
):
    result = create_education(body, db)
    response.status_code = result["code"]
    return result


@router.get("/", response_model=list[AllEducation])
async def get_all_education_routes(response: Response, db: Session = Depends(get_db)):
    result = get_all_educations(db)
    response.status_code = result["code"]
    if result["code"] == 200:
        return result["data"]

    else:
        raise HTTPException(
            404, {"code": 404, "status": "error", "message": "No education Found"}
        )


@router.get("/{education_id}", response_model=EducationOut)
async def get_education_route(
    education_id: str, response: Response, db: Session = Depends(get_db)
):
    result = get_education(education_id, db)
    response.status_code = result["code"]
    if result["code"] == 200:
        return result["data"]
    else:
        raise HTTPException(
            404, {"code": 404, "status": "error", "message": "education does not exist"}
        )


@router.patch("/{education_id}")
async def update_education_route(
    education_id: str,
    body: EducationUpdate,
    response: Response,
    db: Session = Depends(get_db),
):
    result = update_education(education_id, body, db)
    response.status_code = result["code"]
    return result


@router.delete("/{education_id}", response_description="deleted successfuly")
async def delete_education_route(
    education_id: str, response: Response, db: Session = Depends(get_db)
):
    result = delete_education(education_id, db)
    response.status_code = result["code"]
