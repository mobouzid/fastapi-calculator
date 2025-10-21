from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field, root_validator, ValidationError
from typing import Union

app = FastAPI(title="Calculator API", version="0.1.0")

class Operands(BaseModel):
    a: Union[int, float] = Field(..., description="First operand")
    b: Union[int, float] = Field(..., description="Second operand")

    @root_validator
    def check_types(cls, values):
        a, b = values.get('a'), values.get('b')
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both operands must be numeric (int or float).")
        return values

@app.get("/", summary="Health check")
async def root():
    return {"status": "ok", "message": "Calculator API"}

@app.post("/calc/add", summary="Add two numbers")
async def add(op: Operands):
    try:
        result = op.a + op.b
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"Addition error: {ex}")
    return {"operation": "add", "a": op.a, "b": op.b, "result": result}

@app.post("/calc/subtract", summary="Subtract two numbers")
async def subtract(op: Operands):
    try:
        result = op.a - op.b
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"Subtraction error: {ex}")
    return {"operation": "subtract", "a": op.a, "b": op.b, "result": result}

@app.post("/calc/multiply", summary="Multiply two numbers")
async def multiply(op: Operands):
    try:
        result = op.a * op.b
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"Multiplication error: {ex}")
    return {"operation": "multiply", "a": op.a, "b": op.b, "result": result}

@app.post("/calc/divide", summary="Divide two numbers")
async def divide(op: Operands):
    if op.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero")
    try:
        result = op.a / op.b
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"Division error: {ex}")
    return {"operation": "divide", "a": op.a, "b": op.b, "result": result}

@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return HTTPException(status_code=422, detail=str(exc))
