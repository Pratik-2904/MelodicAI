from fastapi import FastAPI
from models.base import Base
from database import engine
from routes import auth, songs


app = FastAPI()

app.include_router(
    router=auth.router, prefix="/auth"
)  # this binds the router with the application that we have defined at the auth

app.include_router(
    router=songs.router, prefix = '/songs'
)

Base.metadata.create_all(engine)
