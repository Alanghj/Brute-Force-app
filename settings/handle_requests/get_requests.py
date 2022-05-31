from settings.handle_requests.response_checker import response_checker
import requests


def get_requests(password_payload):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Origin': 'http://157.245.46.136:32097',
        'Connection': 'keep-alive',
        'Referer': 'http://157.245.46.136:32097/login',
        'Upgrade-Insecure-Requests': '1',
    }

    data = f"username=''&password={password_payload}"
    response = requests.post('http://157.245.46.136:32097/login', headers=headers, data=data, verify=False)
    print(response.text)
    output = response_checker(response, password_payload)
    
    return output