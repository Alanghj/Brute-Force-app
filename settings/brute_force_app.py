from settings.handle_requests.get_requests import get_requests 
import threading
import time


def brute_app():
    start = time.perf_counter()
    list_of_threads = []


    with open('wordlist/10_millions_passwords.txt', "r", encoding='UTF-8') as passwords:
        for password in passwords:
            new_thread = threading.Thread(target=get_requests, args=[password])
            new_thread.start() 

            list_of_threads.append(new_thread)

        for thread in list_of_threads:
            thread.join()

    finish = time.perf_counter()

    print(f'\n\nFinished in {round(finish - start, 2)} second(s)\n')