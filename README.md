# Enterprise Collaboration Workflow API

FastAPI backend for the Enterprise Collaboration Workflow project. The API is configured with SQLAlchemy, Alembic migrations, Pydantic settings, CORS support, and a MySQL database connection.

## Tech Stack

- FastAPI
- Uvicorn
- SQLAlchemy
- Alembic
- Pydantic Settings
- PyMySQL
- MySQL

## Project Structure

```text
fastapi_app/
  alembic/              Database migration files
  core/                 App configuration, database, logging, security, exceptions
  models/               SQLAlchemy models
  routes/               API route modules
  main.py               FastAPI application entrypoint
  requirements.txt      Python dependencies
  alembic.ini           Alembic configuration
```

## Setup

Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\activate
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the `fastapi_app` directory:

```env
PROJECT_NAME=ENTERPRISE COLLABORATION WORKFLOW
PROJECT_VERSION=1.0.0

HOST=127.0.0.1
PORT=8000

DATABASE_URL=mysql+pymysql://USER:PASSWORD@localhost:3306/ecwf_db

SECRET_KEY=change-this-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

LOG_LEVEL=INFO
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
```

Make sure the MySQL database exists before running migrations or starting the app.

## Run the API

From the `fastapi_app` directory:

```powershell
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

Open the API docs:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Available Endpoints

- `GET /` - API status message
- `GET /health` - Health check
- `GET /version` - Application name and version
- `GET /database/test` - Database connection check

## Database Migrations

Run Alembic commands from the `fastapi_app` directory.

Apply migrations:

```powershell
alembic upgrade head
```

Create a new migration:

```powershell
alembic revision --autogenerate -m "describe change"
```

## Development Notes

- Application settings are loaded from `.env` through `pydantic-settings`.
- CORS origins are read from `ALLOWED_ORIGINS` as a comma-separated list.
- The database URL uses the SQLAlchemy MySQL PyMySQL driver format.
