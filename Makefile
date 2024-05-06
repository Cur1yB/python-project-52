install:
	poetry install

migrate:
	poetry run python manage.py migrate

collectstatic:
	poetry run python manage.py collectstatic --noinput

deploy: install migrate collectstatic

run:
	python3 manage.py runserver