from fastapi import FastAPI
from .database import engine
from . import models
from .routers import seller


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(seller.router)


@app.get("/")
def root():
    return {"message": "Hello World"}