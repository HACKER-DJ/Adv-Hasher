#!/usr/bin/python

from urllib.request import urlopen
import hashlib
from termcolor import colored

md5hash = input("[*] Enter The Md5 Hash Value: ")
url = str(input("Enter The password raw link: "))
passlist = str(urlopen(url).read (), 'utf-8')
for password in passlist.split('\n'):
    hashgess = hashlib.md5(bytes(password, 'utf-8')).hexdigest()
    if hashgess == md5hash:
        print(colored("[*] The Password Is: " + str(password), 'green'))
        quit()
    else:
        print(colored("[-] The Password Guess" + str(password) + "Does Not Match, Trying New...", 'red'))
print("Password is not in password list")
