from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Union, Dict, Any

# If you ever need to hash data (like passwords), use a secure library, not hashlib/md5/sha1 directly.
# Example (future usage):
# from passlib.context import CryptContext
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# hashed = pwd_context.hash(plain_password)

app = FastAPI(title="Calculator API", version="0.1.0")

class Operands(BaseModel):
    a: Union[int, float] = Field(..., description="First operand")
    b: Union[int, float] = Field(..., description="Second operand")

@app.get("/", summary="Health check", response_model=Dict[str, Any])
async def root() -> Dict[str, Any]:
    return {"status": "ok", "message": "Calculator API"}

@app.post("/calc/add", summary="Add two numbers", response_model=Dict[str, Any])
async def add(op: Operands) -> Dict[str, Any]:
    result = op.a + op.b
    return {"operation": "add", "a": op.a, "b": op.b, "result": result}

@app.post("/calc/subtract", summary="Subtract two numbers", response_model=Dict[str, Any])
async def subtract(op: Operands) -> Dict[str, Any]:
    result = op.a - op.b
    return {"operation": "subtract", "a": op.a, "b": op.b, "result": result}

@app.post("/calc/multiply", summary="Multiply two numbers", response_model=Dict[str, Any])
async def multiply(op: Operands) -> Dict[str, Any]:
    result = op.a * op.b
    return {"operation": "multiply", "a": op.a, "b": op.b, "result": result}

@app.post("/calc/divide", summary="Divide two numbers", response_model=Dict[str, Any])
async def divide(op: Operands) -> Dict[str, Any]:
    if op.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero")
    result = op.a / op.b
    return {"operation": "divide", "a": op.a, "b": op.b, "result": result}

# Note: No actual hashing performed in operations. If implemented, use cryptographically secure algorithms as described above.