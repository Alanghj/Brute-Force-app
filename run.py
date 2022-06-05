#!/usr/bin/python
from settings.brute_force_app import Brute_force_app


URL_PATH = input('Write the url: ')
        

if __name__ == '__main__':
    brute_force = Brute_force_app(URL_PATH)
    brute_force.start_brute_force()