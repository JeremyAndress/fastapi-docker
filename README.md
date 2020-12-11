# [FastAPI Docker :rocket:](https://github.com/JeremyAndress/fastapi-docker)

![Test](https://github.com/JeremyAndress/fastapi-docker/workflows/Test/badge.svg?branch=master) [![license](https://img.shields.io/github/license/peaceiris/actions-gh-pages.svg)](LICENSE) 

## Features :sparkles:
- [FastAPI](https://fastapi.tiangolo.com/) framework.
- Interactive API documentation
- Full Docker integration.
- Docker Compose integration.
- Production ready Python web server using Uvicorn.
- Secure password hashing by default.
- JWT token authentication.
- SQLAlchemy models
- CORS (Cross Origin Resource Sharing).
- Small utility to paginate SqlAlchemy queries.

## Quick Start :seedling:

### Run FastAPI Docker :zap:  Local Development

1. `git clone https://github.com/JeremyAndress/fastapi-docker.git`
2. Create .env files `cp .env.example .env`

> You should now have a directory structure like:

``` sh
.
├── compose
│   ├── local
│   ├── production
│   └── stage
├── nginx
│   └── site.conf
├── requirements
│   ├── local.txt
│   └── production.txt
├── sql
│   ├── rol.sql
│   └── user.sql
├── src
│   ├── api
│   ├── core
│   ├── db
│   ├── logs
│   ├── models
│   ├── schemas
│   ├── test
│   ├── utils
│   └── main.py
├── CHANGELOG.md
├── .env
├── .env.example
├── .gitignore
├── local.yml
├── production.yml
├── README.md
└── stage.yml
```
3. `docker-compose -f local.yml build`
4. `docker-compose -f local.yml up -d`
5. That's just all, api server is listen at https://localhost:8030/docs now

You will see the automatic interactive API documentation (provided by Swagger UI):
![Swagger UI](screenshots/ui.png)

## Testing  :rotating_light:

```python
    pytest -s -v src/test
```