dev:
	uv run python3 manage.py runserver

makemigr:
	uv run python3 manage.py makemigrations

migr:
	uv run python3 manage.py migrate