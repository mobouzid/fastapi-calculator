from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from typing import Union
import math
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Calculator API", version="0.1.0")

class Operands(BaseModel):
    a: Union[int, float] = Field(..., description="First operand")
    b: Union[int, float] = Field(..., description="Second operand")

    @validator('a', 'b')
    def check_finite_number(cls, v, field):
        if not isinstance(v, (int, float)) or isinstance(v, bool):
            raise ValueError(f"{field.name} must be a number")
        if not math.isfinite(float(v)):
            raise ValueError(f"{field.name} must be a finite number (not NaN or infinity)")
        return v

@app.get("/", summary="Health check")
async def root():
    return {"status": "ok", "message": "Calculator API"}

@app.post("/calc/add", summary="Add two numbers")
async def add(op: Operands):
    result = op.a + op.b
    return {"operation": "add", "a": op.a, "b": op.b, "result": result}

@app.post("/calc/subtract", summary="Subtract two numbers")
async def subtract(op: Operands):
    result = op.a - op.b
    return {"operation": "subtract", "a": op.a, "b": op.b, "result": result}

@app.post("/calc/multiply", summary="Multiply two numbers")
async def multiply(op: Operands):
    result = op.a * op.b
    return {"operation": "multiply", "a": op.a, "b": op.b, "result": result}

@app.post("/calc/divide", summary="Divide two numbers")
async def divide(op: Operands):
    try:
        if op.b == 0:
            logger.error(f"Division by zero attempted: a={op.a}, b={op.b}")
            raise HTTPException(status_code=400, detail="Division by zero")
        result = op.a / op.b
        return {"operation": "divide", "a": op.a, "b": op.b, "result": result}
    except Exception as e:
        logger.error(f"Exception in divide: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while dividing numbers.")

# Note regarding SonarQube rule python:S4790: No actual hashing is performed in this code, so there is no direct risk tied to 'Make sure that hashing data is safe here.' If hashing functionality is ever introduced, ensure to use safe and secure hash functions and never hash passwords or secrets using insecure algorithms.
