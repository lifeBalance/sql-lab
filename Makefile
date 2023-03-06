.PHONY:
dbUp:
	docker compose -f compose-postgres.yml up

.PHONY:
dbDown:
	docker compose -f compose-postgres.yml down