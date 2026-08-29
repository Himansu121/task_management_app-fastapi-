from fastapi import FastAPI
from src.utils.db import base, engine
from src.tasks.models import taskmodel
from src.tasks.router import task_routes
base.metadata.create_all(engine)



app = FastAPI(title="this is my task management application")
app.include_router(task_routes)