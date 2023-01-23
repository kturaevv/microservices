from fastapi import FastAPI, Body, Depends, UploadFile, File, HTTPException

app = FastAPI()

@app.get("/")
async def healthcheck():
    return {"Status":"OK"}

@app.post("/cars_on_border")
async def post_image(
        image_url: str = Body(None),
        image_binary: UploadFile = File(None),
        ):

    if image_binary is None and image_url is None:
        raise HTTPException(
            status_code = 422, 
            detail = {
                "field error":"At least one of the values should be provided",
                "values":{
                    'image_url': image_url,
                    'image_binary':image_binary
                    }
                }
        )
    return {"amount":5, "url":image_url}
