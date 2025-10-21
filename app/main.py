from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Union

app = FastAPI(title="Calculator API", version="0.1.0")

class Operands(BaseModel):
    a: Union[int, float] = Field(..., description="First operand")
    b: Union[int, float] = Field(..., description="Second operand")

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
    if op.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero")
    result = op.a / op.b
    return {"operation": "divide", "a": op.a, "b": op.b, "result": result}
