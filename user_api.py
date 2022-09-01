import uvicorn
from fastapi import FastAPI. HTTPException
from schemas import User


app = FastAPI(title = "User API")


