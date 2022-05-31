def response_checker(response, password_payload):
    if '200' in response.text:
        print(f"!!![PASSWORD FOUND ~~ : ~~ {password_payload} ]")

    if '200' not in response.text:
        print(f"INCORRECT: ~~ {password_payload}")
