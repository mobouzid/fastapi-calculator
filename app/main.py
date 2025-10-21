from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Union

app = FastAPI(title="Calculator API", version="0.1.0")

class Operands(BaseModel):
    """
    Pydantic model for request payloads containing two operands.
    Enforced to be numbers (int or float), double-checked in validators if extended in future.
    """
    a: Union[int, float] = Field(..., description="First operand")
    b: Union[int, float] = Field(..., description="Second operand")

@app.get("/", summary="Health check")
async def root():
    """
    Health check endpoint to confirm API status.
    """
    return {"status": "ok", "message": "Calculator API"}

@app.post("/calc/add", summary="Add two numbers")
async def add(op: Operands):
    """
    Adds two numbers. Safe for numbers, auto-validates type.
    """
    result = op.a + op.b
    return {"operation": "add", "a": op.a, "b": op.b, "result": result}

@app.post("/calc/subtract", summary="Subtract two numbers")
async def subtract(op: Operands):
    """
    Subtracts the second number from the first.
    """
    result = op.a - op.b
    return {"operation": "subtract", "a": op.a, "b": op.b, "result": result}

@app.post("/calc/multiply", summary="Multiply two numbers")
async def multiply(op: Operands):
    """
    Multiplies two numbers.
    """
    result = op.a * op.b
    return {"operation": "multiply", "a": op.a, "b": op.b, "result": result}

@app.post("/calc/divide", summary="Divide two numbers")
async def divide(op: Operands):
    """
    Divides the first number by the second. Returns 400 error if dividing by zero.
    Handles float division as default in Python3.
    """
    if op.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero")
    result = op.a / op.b
    return {"operation": "divide", "a": op.a, "b": op.b, "result": result}

# Note: No hashing operations are present. If there is a need for cryptographic operations in future developments,
# use hashlib or appropriate libraries following current best security practices (as SonarQube S4790 suggests).
