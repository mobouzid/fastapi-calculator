# FastAPI Calculator

A tiny FastAPI application that exposes simple calculator endpoints: add, subtract, multiply, divide. Includes input validation, error handling, comprehensive tests, and clear documentation.

## Requirements
- Python 3.8+

## Project Structure
```
├── app/
│   ├── __init__.py
│   └── main.py          # FastAPI application
├── tests/
│   └── test_main.py     # Comprehensive test suite
├── requirements.txt     # Python dependencies
├── example_client.py    # Example usage client
└── README.md           # This file
```

## Quick Start

### 1. Clone and Setup
```powershell
# Clone the repository
git clone <your-repo-url>
cd <repo-name>

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows PowerShell
# OR: source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Tests
```powershell
pytest tests/ -v
```

### 3. Start Server
```powershell
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive docs**: http://localhost:8000/docs
- **Alternative docs**: http://localhost:8000/redoc

## API Endpoints

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| GET | `/` | Health check | None |
| POST | `/calc/add` | Addition | `{"a": number, "b": number}` |
| POST | `/calc/subtract` | Subtraction | `{"a": number, "b": number}` |
| POST | `/calc/multiply` | Multiplication | `{"a": number, "b": number}` |
| POST | `/calc/divide` | Division | `{"a": number, "b": number}` |

### Example Usage

**PowerShell:**
```powershell
# Addition: 5 + 3
Invoke-RestMethod -Uri "http://localhost:8000/calc/add" -Method POST -ContentType "application/json" -Body '{"a": 5, "b": 3}'

# Division: 15 ÷ 3
Invoke-RestMethod -Uri "http://localhost:8000/calc/divide" -Method POST -ContentType "application/json" -Body '{"a": 15, "b": 3}'
```

**Python:**
```python
import requests

response = requests.post("http://localhost:8000/calc/add", json={"a": 5, "b": 3})
print(response.json())  # {"operation": "add", "a": 5, "b": 3, "result": 8}
```

### Response Format
```json
{
    "operation": "add",
    "a": 5,
    "b": 3,
    "result": 8
}
```

### Error Handling
- Division by zero returns HTTP 400 with error message
- Invalid input data returns HTTP 422 with validation errors

## Development

### Running Tests
```powershell
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=app
```

### Example Client
Run the included example client to test all endpoints:
```powershell
python example_client.py
```
