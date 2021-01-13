#!/usr/bin/python
from os import system
# clear the screen
system('clear')
#colours
red = "\033[91;1m"
green = "\033[92;1m"
yellow = "\033[93;1m"
blue = "\033[94;1m"

# banner 

print(red  + '    ___       __            __  __           __             ')
print(blue + '   /   | ____/ /   __      / / / /___ ______/ /_  ___  _____')
print(blue + '  / /| |/ __  / | / /_____/ /_/ / __ `/ ___/ __ \/ _ \/ ___/')
print(blue + ' / ___ / /_/ /| |/ /_____/ __  / /_/ (__  ) / / /  __/ /    ')
print(blue + '/_/  |_\__,_/ |___/     /_/ /_/\__,_/____/_/ /_/\___/_/' + yellow + ' 1.0')
print(red  + '<<════════════════════════════════════════════════════>>')
print(red  + '<<════════════════> Made By HackerDj <════════════════>>')
print("")
# Option manu
print(green + ' [1] Hash Code Generator ')
print("")
print(green + ' [2] Md5 BruteForce')
print("")
print(green + ' [3] Sha1 BruteForce')
print("")
print(green + ' [4] Sha224 BruteForce')
print("")
print(green + ' [5] Sha256 BruteForce')
print("")
print(green + ' [6] Sha512 BruteForce')
print("")
print(red +   ' [7] Exit')

# take input from user
print(blue + "")

task = input("Adv-Hasher=> ")
print('')

# brain

if task == '1':
    system('cd .p && python3 hasher.py')
elif task == '2':
    system('cd .p && python3 md5_brute.py')
elif task == '3':
    system('cd .p && python3 sha1_brute.py')
elif task == '4':
    system('cd .p && python3 sha224_brute.py')
elif task == '5':
    system('cd .p && python3 sha256_brute.py')
elif task == '6':
    system('cd .p && python3 sha512_brute.py')
elif task == '7':
    exit()
else:
    print(red + '[-] Option Invaled ! ')

