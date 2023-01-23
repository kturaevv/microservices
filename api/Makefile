up:
	docker container rm api || echo ""
	docker build -t api -f api.Dockerfile .
	docker run -d -p 8000:8000 --name api --env-file=../.env.compose api
down:
	docker container stop api
in:
	docker exec -it api sh