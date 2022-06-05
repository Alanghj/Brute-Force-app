import requests


class Handle_requests():
    def __init__(self, url_path:str):
        self.path = url_path


    def get_credentials(self, user_payload:None, password_payload:str):
        self.user_payload = user_payload
        self.password_payload = password_payload
        self.data = {"username": self.user_payload, "password": self.password_payload} #change this

        if self.user_payload is None or self.password_payload == '': 
            self.data = {"username": self.user_payload, "password": self.password_payload} #change this

        self.response = requests.post(self.path, data=self.data, verify=False)
        print(self.response)
        self.output = self.response_checker(self.response, self.user_payload, self.password_payload)

        return self.output


    def response_checker(self, response, user_payload, password_payload):
        self.response = response
        self.user_payload = user_payload
        self.password_payload = password_payload

        if self.response.status_code != 200:
            return print(f"~~VALID~~: USER: {self.user_payload}, PASSWORD: {self.password_payload}")
            
        return print(f"~~Invalid~~: USER: {self.user_payload}, PASSWORD: {self.password_payload}")