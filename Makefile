start:
	poetry run uvicorn main:app --reload

migrate:
	poetry run python3 migrate.py