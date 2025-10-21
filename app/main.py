from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Union
from hashlib import sha256
import re
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Calculator API", version="0.1.0")

# CORS - secure configuration (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Operands(BaseModel):
    a: Union[int, float] = Field(..., description="First operand")
    b: Union[int, float] = Field(..., description="Second operand")

class DataToHash(BaseModel):
    data: str = Field(..., description="String data to hash, must be alphanumeric.")

@app.get("/", summary="Health check")
async def root() -> dict:
    """Health check endpoint."""
    return {"status": "ok", "message": "Calculator API"}

@app.post("/calc/add", summary="Add two numbers")
async def add(op: Operands) -> dict:
    """Return sum of two numbers."""
    result = op.a + op.b
    return {"operation": "add", "a": op.a, "b": op.b, "result": result}

@app.post("/calc/subtract", summary="Subtract two numbers")
async def subtract(op: Operands) -> dict:
    """Return difference of two numbers."""
    result = op.a - op.b
    return {"operation": "subtract", "a": op.a, "b": op.b, "result": result}

@app.post("/calc/multiply", summary="Multiply two numbers")
async def multiply(op: Operands) -> dict:
    """Return product of two numbers."""
    result = op.a * op.b
    return {"operation": "multiply", "a": op.a, "b": op.b, "result": result}

@app.post("/calc/divide", summary="Divide two numbers")
async def divide(op: Operands) -> dict:
    """Return quotient of two numbers or error if dividing by zero."""
    if op.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
    result = op.a / op.b
    return {"operation": "divide", "a": op.a, "b": op.b, "result": result}

@app.post("/calc/hash", summary="Hash provided data securely")
async def hash_data(item: DataToHash) -> dict:
    """Hash provided data using SHA-256. Demonstrates secure hashing for SonarQube S4790 compliance."""
    # Validate input: For demo, only allow reasonably safe strings
    if not re.match(r'^[\w\s-]{1,256}$', item.data):
        raise HTTPException(status_code=400, detail="Input contains invalid characters or is too long.")
    # Securely hash data
    hashed = sha256(item.data.encode('utf-8')).hexdigest()
    return {"original": item.data, "sha256": hashed}

# Note: Only expose /calc/hash if your API must provide such functionality.