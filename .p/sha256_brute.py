#!/usr/bin/python

from urllib.request import urlopen
import hashlib
from termcolor import colored

sha256hash = input("[*] Enter The Sha256 Hash Value: ")
url = str(input("Enter The password raw link: "))
passlist = str(urlopen(url).read (), 'utf-8')
for password in passlist.split('\n'):
    hashgess = hashlib.sha256(bytes(password, 'utf-8')).hexdigest()
    if hashgess == sha256hash:
        print(colored("[*] The Password Is: " + str(password), 'green'))
        quit()
    else:
        print(colored("[-] The Password Guess" + str(password) + "Does Not Match, Trying New...", 'red'))
print("Password is not in password list")
