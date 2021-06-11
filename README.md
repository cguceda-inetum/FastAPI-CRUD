# FastAPI-CRUD
FastAPI CRUD Example

launch docker: docker compose up

debug: debug is enable launching debug.py instead main.app that changes .env => debug.env that changes from "db" to "localhost"

You'll find OpenAPI docs: localhost:8000/docs

Know issues:

web launch could fail because postgres is not already ready, please re-play from docker console to correct. This should not be a problem with production environments because database is already running in such cases.

![](screenshot.png)
