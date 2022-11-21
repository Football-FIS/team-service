SELF_DIR := $(dir $(lastword $(MAKEFILE_LIST)))
export APP_ENV := $(shell grep APP_ENV $(SELF_DIR).env | awk -F '=' '{print $$NF}')

start:
	docker compose up -d --build

start-logs:
	docker compose up --build

stop:
	docker compose stop

status:
	docker compose ps
