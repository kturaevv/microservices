import requests
from send_msg import send_to_qu

def fetch_and_save():
    response = requests.get("https://i.imgur.com/ExdKOOz.png")
    file = open("./data/sample_image.png", "wb")
    file.write(response.content)
    file.close()
    return file.name

if __name__ == "__main__":
    print("Fetching image ...")
    name = fetch_and_save()
    print("Sending to queue ...")
    send_to_qu(name)
    print("Done!")