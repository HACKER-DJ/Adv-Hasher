#!/usr/bin/python

#colours
red = "\033[91;1m"
green = "\033[92;1m"
yellow = "\033[93;1m"
blue = "\033[94;1m"

import hashlib

hashvalue = input('Enter a string to hash: ')

hashobj1 = hashlib.md5()
hashobj1.update(hashvalue.encode())
print(red + 'md5  =>> ' + hashobj1.hexdigest())

hashobj2 = hashlib.sha1()
hashobj2.update(hashvalue.encode())
print(green + 'sha1 =>> ' + hashobj2.hexdigest())

hashobj3 = hashlib.sha224()
hashobj3.update(hashvalue.encode())
print(blue + 'sha224 =>> ' + hashobj3.hexdigest())


hashobj4 = hashlib.sha256()
hashobj4.update(hashvalue.encode())
print(green + 'sha256 =>> ' + hashobj4.hexdigest())


hashobj5 = hashlib.sha512()
hashobj5.update(hashvalue.encode())
print(blue + 'sha512 =>> ' + hashobj5.hexdigest())

