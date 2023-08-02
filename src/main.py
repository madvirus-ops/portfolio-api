from fastapi import FastAPI
from settings import settings
from rest_api.biodata import router as rest_router


app = FastAPI(title=settings.APP_TITLE,debug=settings.DEBUG,description=settings.APP_DESCRIPTION)


def include_all_router(app:FastAPI):
    app.include_router(rest_router)


include_all_router(app=app)