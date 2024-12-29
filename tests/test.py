import requests

url = "https://chat.autofaq.ai/api/webhooks/widget/6c24eb52-b1ab-4d78-8463-8556d4ee04b3/messages?ts=1735395158250"

#payload = {"id":"9a8e77dc-6b4a-475a-bc82-ed1b91f8e9a3",
#           "ts":1735315980868,
#           "text":"привет"
#           }


headers = {
    'Accept': 'application/json',
    #'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'session-id': 'bc536a64-b32f-4a17-8e9b-8f637bc397ab'
}
session = requests.session()
#response = requests.request("POST", url, headers=headers)
r = session.post(url=url ,headers=headers, json=payload)
print(r.text)