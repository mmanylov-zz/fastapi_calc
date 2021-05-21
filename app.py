from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ValidationError, validator

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Numbers(BaseModel):
    x: int
    y: int

    @validator('x')
    def positive_integer(cls, v):
        if v <= 0:
            raise ValueError('value must be a positive integer')
        return v

    @validator('y')
    def non_negative_integer(cls, v):
        if v < 0:
            raise ValueError('value must be a non-negative integer')
        return v


@app.post('/', status_code=200)
async def add_movie(payload: Numbers):
    numbers = payload.dict()
    result = numbers['x'] + numbers['y']
    return {'result': result}
