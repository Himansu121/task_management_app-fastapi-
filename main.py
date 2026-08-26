from fastapi import FastAPI
from src.utils.db import base, engine

base.metadata.create_all(engine)



app = FastAPI(title="this is my task management application")
