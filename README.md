### Run app
python -m uvicorn main:app --host localhost --port 8000 --reload

### Initializing migrations
python -m alembic init -t async migrations

### Run migrations
python -m alembic revision --autogenerate -m "init"

### Apply migrations
python -m alembic upgrade head 
