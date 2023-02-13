import requests


class Handle_requests():
    def __init__(self, url_path:str):
        self.path = url_path


    def get_credentials(self, user_payload:None, password_payload:str):
        data = {"username": user_payload, "password": password_payload} #change this

        if user_payload is None or password_payload == '': 
            data = {"username": user_payload, "password": password_payload} #change this

        response = requests.post(self.path, data=data, verify=False)
        print(response)
        output = response_checker(response, user_payload, password_payload)

        return output


    def response_checker(self, response, user_payload, password_payload):
        if response.status_code != 200:
            return print(f"~~VALID~~: USER: {user_payload}, PASSWORD: {password_payload}")
            
        return print(f"~~Invalid~~: USER: {user_payload}, PASSWORD: {password_payload}")