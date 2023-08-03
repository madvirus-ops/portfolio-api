import sys

sys.path.append("./")
from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session
from helpers.certificate_help import (
    create_certificate,get_all_certificates,get_certificate,update_certificate,delete_certificate
)
from connections.database import get_db
from rest_api.rest_schema import CertificateIn,CertificateOut,CertificateUpdate,AllCertificates


router = APIRouter(prefix="/api/v1/certificate", tags=[" certificate Routes"])


@router.post("/")
async def create_certificate_route(
    body: CertificateIn, response: Response, db: Session = Depends(get_db)
):
    result = create_certificate(body, db)
    response.status_code = result["code"]
    return result


@router.get("/", response_model=list[AllCertificates])
async def get_all_certificate_routes(response: Response, db: Session = Depends(get_db)):
    result = get_all_certificates(db)
    response.status_code = result["code"]
    if result["code"] == 200:
        return result["data"]

    else:
        raise HTTPException(
            404, {"code": 404, "status": "error", "message": "No certificate Found"}
        )


@router.get("/{certificate_id}", response_model=CertificateOut)
async def get_certificate_route(
    certificate_id: str, response: Response, db: Session = Depends(get_db)
):
    result = get_certificate(certificate_id, db)
    response.status_code = result["code"]
    if result["code"] == 200:
        return result["data"]
    else:
        raise HTTPException(
            404, {"code": 404, "status": "error", "message": "certificate does not exist"}
        )


@router.patch("/{certificate_id}")
async def update_certificate_route(
    certificate_id: str,
    body: CertificateUpdate,
    response: Response,
    db: Session = Depends(get_db),
):
    result = update_certificate(certificate_id, body, db)
    response.status_code = result["code"]
    return result


@router.delete("/{certificate_id}", response_description="deleted successfuly")
async def delete_certificate_route(
    certificate_id: str, response: Response, db: Session = Depends(get_db)
):
    result = delete_certificate(certificate_id, db)
    response.status_code = result["code"]
