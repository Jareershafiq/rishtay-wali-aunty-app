import chainlit as cl
from time import sleep

from profiles import profiles  # yeh tumhara list of 20 profiles hai
import requests

# WhatsApp API config
INSTANCE_ID = "YOUR_INSTANCE_ID"
TOKEN = "YOUR_API_TOKEN"

def send_whatsapp(to, message):
    url = f"https://api.ultramsg.com/{INSTANCE_ID}/messages/chat"
    payload = {
        "token": TOKEN,
        "to": to,
        "body": message
    }
    try:
        res = requests.post(url, data=payload)
        print(res.json())
    except Exception as e:
        print("❌", e)

@cl.on_message
async def main(message: cl.Message):
    text = message.content.lower().strip()

    if "female" in text or "ladki" in text:
        gender = "female"
    elif "male" in text or "ladka" in text:
        gender = "male"
    else:
        await cl.Message(content="Beta kis gender ka rishta chahiye? (male/female)").send()
        return

    matches = [p for p in profiles if p["gender"] == gender]
    if not matches:
        await cl.Message(content="Koi rishta nahi mila beta.").send()
        return

    await cl.Message(content=f"👵 Aunty ke paas {len(matches)} rishtay hain:\n").send()

    for p in matches:
        line = f"{p['name']}, {p['age']} saal ka/ki, {p['profession']} from {p['city']}"
        await cl.Message(content="👤 " + line).send()
        # WhatsApp bhejna (optional — comment out if not working)
        # send_whatsapp(p["whatsapp"], f"Aunty ka paigham:\n{line}")
        sleep(0.5)
