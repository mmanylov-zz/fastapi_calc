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
    number1: int
    number2: int

    @validator('number1')
    def positive_integer(cls, v):
        if v <= 0:
            raise ValueError('value must be a positive integer')
        return v

    @validator('number2')
    def non_negative_integer(cls, v):
        if v < 0:
            raise ValueError('value must be a non-negative integer')
        return v


class Response(BaseModel):
    result: int


@app.post('/', status_code=200, response_model=Response)
async def add_movie(payload: Numbers):
    numbers = payload.dict()
    result = numbers['number1'] + numbers['number2']
    return {'result': result}
