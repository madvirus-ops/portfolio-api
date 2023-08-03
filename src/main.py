from fastapi import FastAPI
from settings import settings
from rest_api.biodata_route import router as bio_router
from rest_api.education_route import router as edu_router
from rest_api.certificate_route import router as cert_router


app = FastAPI(
    title=settings.APP_TITLE,
    debug=settings.DEBUG,
    description=settings.APP_DESCRIPTION,
    version="1.0.0",
    terms_of_service="https://github.com/madvirus-ops/madvirus-ops",
)


def include_all_router(app: FastAPI):
    app.include_router(bio_router)
    app.include_router(edu_router)
    app.include_router(cert_router)


include_all_router(app=app)
