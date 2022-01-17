import os
print('install libraries...')
os.system('pip install geocoder')
os.system('cls||clear')
os.system('pip install colorama')
os.system('cls||clear')
os.system('pip install cryptocode')
os.system('cls||clear')
os.system('pip install threading')
os.system('cls||clear')
os.system('pip install telebot')
os.system('cls||clear')
print('all librares install')
os.system('cls||clear')
import scanp
import ipi
import crypto
from colorama import Fore
print('╔═══╗╔╗─╔╗╔═══╗╔╗─╔╗ 1 for CryptoPy\n║╔═╗║║║─║║║╔═╗║║║─║║ 2 For pyIPinfo\n║║─╚╝║╚═╝║║║║║║║╚═╝║ 3 for scanP\n║║─╔╗╚══╗║║║║║║╚══╗║\n║╚═╝║───║║║╚═╝║───║║\n╚═══╝───╚╝╚═══╝───╚╝\n')
mode = input('Selct mode\ninput exit for exit\n>>')
if mode == '3':
    scanp.sc()
elif mode == '1':
    crypto.crypto()
elif mode == '2':
    ipi.pii()
elif mode == 'exit':
    quit()
else:
    print(Fore.LIGHTRED_EX+'[•] Unknown command')
    
