import requests, time, logging, sys
from send_msg import send_to_qu, logger

def fetch_and_save():
    response = requests.get("https://i.imgur.com/ExdKOOz.png")
    file = open("./data/sample_image.png", "wb")
    file.write(response.content)
    file.close()
    return file.name

if __name__ == "__main__":
    
    while True:
        logger.info("Fetching image ...")
        name = fetch_and_save()
        logger.info("Sending to queue ...")
        send_to_qu(name)
        logger.info("Done!")

        time.sleep(5)