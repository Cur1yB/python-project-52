dev:
	uv run python manage.py runserver

makemigr:
	uv run python manage.py makemigrations

migrate:
	uv run python manage.py migrate

test:
	uv run python manage.py test

.PHONY: install
install:
	uv sync

.PHONY: collectstatic
collectstatic:
	uv run python manage.py collectstatic --noinput

.PHONY: build
build:
	./build.sh