HOME =: /bin/bash

up:
	docker compose --env-file=.env.compose up -d --build
down:
	docker compose down

# Send msg to queue
msg:
	@cd parser; python -m send_msg

# Run application locally, while deploying all other services
local:
	docker compose \
		-f application/docker-compose.yml \
		-f docker-compose.yml \
		-f docker-compose.local.yml --env-file=application/.env.local up -d --build
local-down:
	docker compose \
		-f application/docker-compose.yml \
		-f docker-compose.yml \
		-f docker-compose.local.yml down
