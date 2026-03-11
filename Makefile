dev:
	uv run python3 manage.py runserver

makemigr:
	uv run python3 manage.py makemigrations

migr:
	uv run python3 manage.py migrate

test_:
	uv run python3 manage.py test

.PHONY: install
install:
	@uv sync

.PHONY: build
build:
	./build.sh

.PHONY: collectstatic
collectstatic:
	@$(MANAGE) collectstatic --noinput