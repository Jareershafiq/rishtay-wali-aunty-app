import streamlit as st
from time import sleep
from profiles import profiles  # Yeh tumhara list of 20 profiles hai
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
        st.write(res.json())
    except Exception as e:
        st.error(f"❌ Error sending WhatsApp message: {e}")

st.title("👵 Rishtay Wali Aunty App")

user_input = st.text_input("Beta, kis gender ka rishta chahiye? (male/female/ladka/ladki)")

if user_input:
    text = user_input.lower().strip()
    
    if "female" in text or "ladki" in text:
        gender = "female"
    elif "male" in text or "ladka" in text:
        gender = "male"
    else:
        st.warning("Beta kis gender ka rishta chahiye? (male/female)")
        st.stop()

    matches = [p for p in profiles if p["gender"] == gender]
    
    if not matches:
        st.info("Koi rishta nahi mila beta.")
    else:
        st.success(f"Aunty ke paas {len(matches)} rishtay hain:\n")

        for p in matches:
            line = f"{p['name']}, {p['age']} saal ka/ki, {p['profession']} from {p['city']}"
            st.write("👤 " + line)
            # WhatsApp bhejna (optional — uncomment to enable)
            # send_whatsapp(p["whatsapp"], f"Aunty ka paigham:\n{line}")
            sleep(0.5)
