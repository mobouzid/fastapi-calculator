import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        r = await ac.get("/")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

@pytest.mark.asyncio
async def test_add():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        r = await ac.post("/calc/add", json={"a": 2, "b": 3})
    assert r.status_code == 200
    assert r.json()["result"] == 5

@pytest.mark.asyncio
async def test_subtract():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        r = await ac.post("/calc/subtract", json={"a": 5, "b": 3})
    assert r.status_code == 200
    assert r.json()["result"] == 2

@pytest.mark.asyncio
async def test_multiply():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        r = await ac.post("/calc/multiply", json={"a": 4, "b": 3})
    assert r.status_code == 200
    assert r.json()["result"] == 12

@pytest.mark.asyncio
async def test_divide():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        r = await ac.post("/calc/divide", json={"a": 10, "b": 2})
    assert r.status_code == 200
    assert r.json()["result"] == 5

@pytest.mark.asyncio
async def test_divide_by_zero():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        r = await ac.post("/calc/divide", json={"a": 1, "b": 0})
    assert r.status_code == 400
    assert "Division by zero" in r.text
