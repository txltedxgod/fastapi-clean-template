"""Pytest configuration and isolated FastAPI client fixtures."""

from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

from src.api.v1.router import repo
from src.main import app


@pytest.fixture(autouse=True)
def reset_repo() -> Iterator[None]:
    """Reset the in-memory repository before each test."""
    repo._db.clear()
    yield
    repo._db.clear()


@pytest.fixture
def client() -> TestClient:
    """Return a FastAPI TestClient."""
    return TestClient(app)
