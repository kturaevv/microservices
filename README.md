## Sample project with microservice architecture.
---



Start the project with:
```sh
make up
```

Send message to queue with:
```
# Update env variables if needed
export $(cat .env.compose)
make msg
```
