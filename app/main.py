from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field
from typing import Union
import logging
from fastapi.responses import JSONResponse

app = FastAPI(title="Calculator API", version="0.1.0")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("calculator_app")

class Operands(BaseModel):
    a: Union[int, float] = Field(..., description="First operand")
    b: Union[int, float] = Field(..., description="Second operand")

@app.get("/", summary="Health check")
async def root():
    return {"status": "ok", "message": "Calculator API"}

@app.post("/calc/add", summary="Add two numbers")
async def add(op: Operands):
    try:
        result = op.a + op.b
        return {"operation": "add", "a": op.a, "b": op.b, "result": result}
    except Exception as e:
        logger.error(f"Add error: {e}")
        raise HTTPException(status_code=500, detail="Error performing addition")

@app.post("/calc/subtract", summary="Subtract two numbers")
async def subtract(op: Operands):
    try:
        result = op.a - op.b
        return {"operation": "subtract", "a": op.a, "b": op.b, "result": result}
    except Exception as e:
        logger.error(f"Subtract error: {e}")
        raise HTTPException(status_code=500, detail="Error performing subtraction")

@app.post("/calc/multiply", summary="Multiply two numbers")
async def multiply(op: Operands):
    try:
        result = op.a * op.b
        return {"operation": "multiply", "a": op.a, "b": op.b, "result": result}
    except Exception as e:
        logger.error(f"Multiply error: {e}")
        raise HTTPException(status_code=500, detail="Error performing multiplication")

@app.post("/calc/divide", summary="Divide two numbers")
async def divide(op: Operands):
    try:
        if op.b == 0:
            raise HTTPException(status_code=400, detail="Division by zero")
        result = op.a / op.b
        return {"operation": "divide", "a": op.a, "b": op.b, "result": result}
    except HTTPException as exc:
        raise exc
    except Exception as e:
        logger.error(f"Divide error: {e}")
        raise HTTPException(status_code=500, detail="Error performing division")

# Defensive placeholder for crypto-hashing as per SonarQube warning
# Please replace this with secure hashing (e.g., hashlib.pbkdf2_hmac for passwords) and avoid using insecure hashes like md5, sha1
# def hash_data_safely(data: str) -> str:
#     import hashlib
#     # Example: return hashlib.sha256(data.encode()).hexdigest()  # Only for non-passwords
#     pass

# Global error handler for uncaught exceptions
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}")
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})
