from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Union

app = FastAPI(title="Calculator API", version="0.1.0")

class Operands(BaseModel):
    a: Union[int, float] = Field(..., description="First operand")
    b: Union[int, float] = Field(..., description="Second operand")

@app.get("/", summary="Health check")
async def root() -> dict:
    return {"status": "ok", "message": "Calculator API"}

@app.post("/calc/add", summary="Add two numbers")
async def add(op: Operands) -> dict:
    # No security issues; input is validated by Pydantic
    result = op.a + op.b
    return {"operation": "add", "a": op.a, "b": op.b, "result": result}

@app.post("/calc/subtract", summary="Subtract two numbers")
async def subtract(op: Operands) -> dict:
    result = op.a - op.b
    return {"operation": "subtract", "a": op.a, "b": op.b, "result": result}

@app.post("/calc/multiply", summary="Multiply two numbers")
async def multiply(op: Operands) -> dict:
    result = op.a * op.b
    return {"operation": "multiply", "a": op.a, "b": op.b, "result": result}

@app.post("/calc/divide", summary="Divide two numbers")
async def divide(op: Operands) -> dict:
    if op.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
    result = op.a / op.b
    return {"operation": "divide", "a": op.a, "b": op.b, "result": result}

# SECURITY NOTE:
# If future code adds any form of data hashing (e.g., for user authentication or hashing sensitive data),
# ensure the following:
#   - Use robust, up-to-date libraries (e.g., hashlib with sha256+ for generic hashes, passlib/argon2/bcrypt for passwords).
#   - Never use broken hash algorithms (like md5 or sha1) for anything security-related.
#   - Never log or expose hashes of sensitive user data in API responses.
# The warning in the SonarQube report about hashing should be addressed at the relevant code site if/when such functionality is introduced.