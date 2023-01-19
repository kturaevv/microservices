up:
	docker container rm api || echo ""
	docker build -t api -f celery.Dockerfile .
	docker run -d --name api --env-file=../.env.compose api
	winpty docker exec -it api sh
down:
	docker container stop api