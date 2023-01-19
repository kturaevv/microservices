from fastapi import FastAPI
import logging, sys

app = FastAPI()

FORMAT = '%(asctime)s - %(levelname)s: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)]
)

@app.get("/")
async def healthcheck():
    logging.info("API triggered.")
    return {"Status":"OK"}
