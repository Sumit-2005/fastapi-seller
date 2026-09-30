from fastapi import FastAPI
from .database import engine
from . import models
from .routers import seller
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["https://campus-cart-yuvraj.vercel.app/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

models.Base.metadata.create_all(bind=engine)

app.include_router(seller.router)


@app.get("/")
def root():
    return {"message": "Hello World"}