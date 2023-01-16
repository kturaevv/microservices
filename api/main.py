from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def healthcheck():
    print("HELLO FROM API")
    return {"Status":"OK"}
