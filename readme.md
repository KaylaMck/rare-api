# Rare Server (Django)

A multi-user blogging platform API built with Django REST Framework.

## Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop/) (for PostgreSQL database)

## Getting Started

1. Run `docker compose up -d` to start the PostgreSQL database
2. Run `pipenv install` to install dependencies
3. Run `pipenv shell` to activate the virtual environment
4. Run `python manage.py migrate` to create the database tables
5. Run `python manage.py loaddata initial_data` to seed the database
6. Run `python manage.py runserver 8088` to start the server

The API runs on http://localhost:8088.

## Available Endpoints

| Method | URL         | Description       |
|--------|-------------|-------------------|
| POST   | /login      | Log in a user     |
| POST   | /register   | Register new user |

## Project Structure

- `rareproject/` — Django project configuration (settings, root URLs)
- `rareapi/` — Django app with models, views, and fixtures
- `manage.py` — Django management script
