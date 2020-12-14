#! /usr/bin/env bash

# Let the DB start
python3 pre_start.py

# Run migrations
PYTHONPATH=. alembic revision --autogenerate 
PYTHONPATH=. alembic upgrade head

