from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests

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