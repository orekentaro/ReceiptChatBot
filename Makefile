run:
	docker-compose up

lint: black flake8 isort mypy

mypy:
	docker-compose exec api poetry run mypy .

flake8:
	docker-compose exec api poetry run pflake8 .

black:
	docker-compose exec api poetry run black .

isort:
	docker-compose exec api poetry run isort .

test:
	docker-compose exec api pytest 