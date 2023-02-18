from typing import Union
from fastapi import FastAPI
from database.models.buzzsprout import Buzzsprout
from database.models.podcast import Podcast
from database.database import db


app = FastAPI()


@app.get("/podcasts")
def podcasts():
    return db.query(Podcast).all()


@app.get("/buzzsprout/all")
def podcasts():
    return db.query(Buzzsprout).all()
