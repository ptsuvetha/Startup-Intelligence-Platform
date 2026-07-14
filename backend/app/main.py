from fastapi import FastAPI

from app.databases.database import Base, engine
from app.routers.user_router import router as user_router


from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_router)
@app.get("/")
def home():
    return {
        "message": "Startup Intelligence Platform API"
    }