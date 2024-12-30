# import sys
# import http.client
#
# def send(message):
#     webhookurl = "https://discord.com/api/webhooks/1323292248628265042/ii0-TUjd8o2-IwQBLdDffHuLi19oYU6ho1_VOuCFVkin0cTHKFaYbSWeDpfFVEHhec36"
#     formdata = "------:::BOUNDARY:::\r\nContent-Disposition: form-data; name=\"content\"\r\n\r\n" + message + "\r\n------:::BOUNDARY:::--"
#
#     connection = http.client.HTTPSConnection("discordapp.com")
#     connection.request("POST", webhookurl, formdata, {"Content-Type": "multipart/form-data; boundary=----:::BOUNDARY:::", "cache-control": "no-cache"})
#     response = connection.getresponse()
#     result = response.read()
#
#     return result.decode("utf-8")
# print(send(sys.argv[0]))
#
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