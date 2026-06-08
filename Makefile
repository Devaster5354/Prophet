.PHONY: build run test lint docker-build

docker-build:
	docker build -t prophet:local .

run:
	docker-compose up --build

test:
	pytest -q

lint:
	flake8 .
