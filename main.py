import tls_client
from itertools import cycle
import random
import threading

webhooks = open("webhooks.txt", "r", encoding="utf-8").read().splitlines()
proxies = open('proxies.txt', "r", encoding="utf-8").read().splitlines()

def whspammer():
    session = tls_client.Session(client_identifier="chrome115", random_tls_extension_order=True)
    spam = input("Message » ")

    sessId = str(random.randint(500,10000))
    proxy = "http://" + random.choice(proxies).replace('sessionid', sessId)

    session.proxies = {
        "http": proxy,
        "https": proxy
    }

    random_names=["bhop3", "albaner"]

    avatars = cycle(["https://media.discordapp.net/attachments/1059643853046554697/1060478546885214279/tool_design.png", "https://cdn.discordapp.com/attachments/1059643853046554697/1060480692556931122/IMG_6554.png"])

    def ehook(webhook):
        einfo={
            'username': random.choice(random_names),
            'content': spam,
            "avatar_url": next(avatars)
        }

        webhook = random.choice(webhooks)
        
        r = session.post(webhook, json=einfo)

        if r.status_code == 200 or 204:
            print("Webhook » {spam} sent")
        else:
            print("Webhook » {spam} can't sent")

    while True:
        threading.Thread(target=ehook, args=(webhooks,)).start()

whspammer()