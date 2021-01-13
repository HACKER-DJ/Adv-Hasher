#!/usr/bin/python

from urllib.request import urlopen
import hashlib
from termcolor import colored

sha512hash = input("[*] Enter The Sha512 Hash Value: ")
url = str(input("Enter The password raw link: "))
passlist = str(urlopen(url).read (), 'utf-8')
for password in passlist.split('\n'):
    hashgess = hashlib.sha512(bytes(password, 'utf-8')).hexdigest()
    if hashgess == sha512hash:
        print(colored("[*] The Password Is: " + str(password), 'green'))
        quit()
    else:
        print(colored("[-] The Password Guess" + str(password) + "Does Not Match, Trying New...", 'red'))
print("Password is not in password list")
