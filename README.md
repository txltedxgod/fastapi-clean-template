# fastapi-clean-template

[![Python CI](https://github.com/txltedxgod/fastapi-clean-template/actions/workflows/ci.yml/badge.svg)](https://github.com/txltedxgod/fastapi-clean-template/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLAlchemy 2.0](https://img.shields.io/badge/SQLAlchemy-2.0_Async-D71E00.svg)](https://www.sqlalchemy.org/)


Enterprise-grade production FastAPI boilerplate with Clean Architecture, Domain-Driven Design (DDD), and async services.

## Architecture & Design

Built with modern Python 3.11 asynchronous patterns, strict Pydantic v2 schemas, and standard 12-factor application conventions.

### Directory Layout

```
├── src/
│   ├── api/v1/         # Versioned REST controllers
│   ├── core/           # Settings, structured logging & domain exceptions
│   ├── schemas/        # Request / Response validation schemas
│   ├── services/       # Core business logic and storage state machines
│   └── main.py         # Application lifespan & middleware integration
├── tests/
│   ├── conftest.py     # Shared fixtures and mock clients
│   └── test_service.py # Automated pytest test cases
├── Dockerfile          # Multi-stage production container
├── Makefile            # Standard developer commands (lint, test, run)
└── pyproject.toml      # Tooling configuration (Ruff, mypy, pytest)
```

## Quick Start

```bash
make install
make test
make run
```

## Production Container

```bash
docker compose up -d --build
```

## License
MIT License