from sqlalchemy.orm import Session

from src.tasks.dtos import taskshchema
from src.tasks.models import taskmodel


def create_task(body: taskshchema, db: Session):
    
    data=body.model_dump()
    new_task=taskmodel(title=data["title"],description=data["description"],is_completed=data["is_completed"])
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return {"status": "task created successfully", "data": new_task}



def get_tasks(db: Session):
    tasks = db.query(taskmodel).all()
    return {"status": "success", "data": tasks}