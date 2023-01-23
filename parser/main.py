import requests, time, logging, sys, secrets, os
from send_msg import send_to_qu, logger

from models import BorderCapture, init_db

def fetch_and_save():
    response = requests.get("https://i.imgur.com/ExdKOOz.png")
    
    # temporary fix to unique name
    file = open(os.getcwd() + "/data/" + str(time.time()) + ".png", "wb")
    file.write(response.content)
    file.close()

    model = BorderCapture.create(
        image_path=file.name,
    )
    logger.info("Record created.")
    return str(model.id)

if __name__ == "__main__":
    logger.info("Initing Database...")
    init_db()
    logger.info("Database Have been initialized! ")

    while True:
        logger.info("Fetching image ...")
        id = fetch_and_save()
        logger.info("Sending to queue ...")
        send_to_qu(id)
        logger.info("Done!")

        time.sleep(10)