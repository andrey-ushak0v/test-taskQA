import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import pytest
import json



class ChatAPI:

    def __init__(self, url, session_id):
        self.url = url
        self.session_id = session_id
        
    def send_post_request(self, payload):
        multipart_data = MultipartEncoder(
            fields={'payload': payload}
        )
        headers = {
            'Content-Type': multipart_data.content_type,
            'session-id': self.session_id
        }
        response = requests.post(self.url, headers=headers, data=multipart_data)
        return response



url = "https://chat.autofaq.ai/api/webhooks/widget/6c24eb52-b1ab-4d78-8463-8556d4ee04b3/messages"
session_id = 'bc536a64-b32f-4a17-8e9b-8f637bc397ab'


def generate_payload(text="some text"):
    return json.dumps({
        "id": "5cc704bc-5c1f-4726-be18-2fc6fb55fa81",
        "ts": 1735417556973,
        "text": text
    })


api = ChatAPI(url, session_id)


def test_status_code_200():
    payload = generate_payload("some text") 
    response = api.send_post_request(payload)
    assert response.status_code == 200, f"Expected status 200, but got {response.status_code}"



def test_text_in_request_and_response():
    payload = generate_payload("some text")
    response = api.send_post_request(payload)
    response_data = response.json()  
    request_text = "some text" 
    response_text = response_data.get('text')
    assert request_text == response_text, f"Expected text '{request_text}', but got '{response_text}'"

def test_request_without_text():
    payload = generate_payload(text="") 
    response = api.send_post_request(payload)
    assert response.status_code == 200, f"Expected status 400 for missing text, but got {response.status_code}"
    
    