# [FastApi Docker :rocket:](https://github.com/JeremyAndress/fastapi-docker)

## Features :sparkles:

- Full Docker integration.
- Docker Compose integration.
- Production ready Python web server using Uvicorn.
- Secure password hashing by default.
- JWT token authentication.
- SQLAlchemy models
- CORS (Cross Origin Resource Sharing).
- Small utility to paginate SqlAlchemy queries.

## Quick Start :seedling:

### Run Backend Local Development

    1. `git clone https://github.com/JeremyAndress/fastapi-docker.git`
    2. Create .env files `cp .env.example .env`
    3. `docker-compose -f local.yml build`
    4. `docker-compose -f local.yml up -d`
    5. That's just all, api server is listen at https://localhost:8030/docs now

## Testing  :rotating_light:

```python
    pytest -s -v src/test
```