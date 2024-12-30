import sys
import requests
import keys

def send_message(message):
    web_url = keys.WebhookURL
    data = {
        "content": message,
    }

    try:
        response = requests.post(web_url, json=data)
        if response.status_code == 200 or response.status_code == 204:
            print("Message sent successfully.")
        else:
            print("Message failed to send. code:" + str(response.status_code) +", Response: "+ response.text)
    except Exception as e:
        print(f"an exception occurred: {e}")

print(send_message(sys.argv[1]))