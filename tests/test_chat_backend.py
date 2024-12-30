import requests
import allure
from utils.payload_generation import generate_payload
from request.requests_chat import ChatAPI


url = "https://chat.autofaq.ai/api/webhooks/widget/6c24eb52-b1ab-4d78-8463-8556d4ee04b3/messages"
session_id = 'bc536a64-b32f-4a17-8e9b-8f637bc397ab'


api = ChatAPI(url, session_id)


@allure.feature('request_send_msg')
def test_status_code_200():

    "проверяeт что при отправке сообщения возвращается статус 200"

    payload = generate_payload("some text") 
    response = api.send_post_request(payload)
    assert response.status_code == 200, f"Expected status 200, but got {response.status_code}"


@allure.feature('request_send_msg')
def test_text_in_request_and_response():

    "проверяет что text в запросе и в ответе совпадает"

    payload = generate_payload("some text")
    response = api.send_post_request(payload)
    response_data = response.json()  
    request_text = "some text" 
    response_text = response_data.get('text')
    assert request_text == response_text, f"Expected text '{request_text}', but got '{response_text}'"

@allure.feature('request_send_msg')
def test_request_with_text():

    "проверяет что запрос с пустым text возвращает статус 200"

    payload = generate_payload(text="") 
    response = api.send_post_request(payload)
    assert response.status_code == 200, f"Expected status 200 for missing text, but got {response.status_code}"
    
@allure.feature('request_send_msg')
def test_request_without_text():

    "проверяет что запрос без параметра text возвращает статус 500"

    payload = generate_payload() 
    response = api.send_post_request(payload)
    assert response.status_code == 500, f"Expected status 50o0 for missing text, but got {response.status_code}"