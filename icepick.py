import socket
from colorama import Fore, Style
import ssl
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import subprocess
import re
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import os
import ipaddress

def print_banner():
    print(Fore.RED + '''$$$$$$\  $$$$$$\  $$$$$$$$\           $$\           $$\       
\_$$  _|$$  __$$\ $$  _____|          \__|          $$ |      
  $$ |  $$ /  \__|$$ |       $$$$$$\  $$\  $$$$$$$\ $$ |  $$\ 
  $$ |  $$ |      $$$$$\    $$  __$$\ $$ |$$  _____|$$ | $$  |
  $$ |  $$ |      $$  __|   $$ /  $$ |$$ |$$ /      $$$$$$  / 
  $$ |  $$ |  $$\ $$ |      $$ |  $$ |$$ |$$ |      $$  _$$<  
$$$$$$\ \$$$$$$  |$$$$$$$$\ $$$$$$$  |$$ |\$$$$$$$\ $$ | \$$\ 
\______| \______/ \________|$$  ____/ \__| \_______|\__|  \__|
                            $$ |                              
                            $$ |                              
                            \__|''' + Style.RESET_ALL + "v1.0")
    print("We're all mad here...")
    print()
    
if __name__ == "__main__":
    print_banner()

def execute_subprocess(cmd):
    return subprocess.call(cmd)

def read_tempurl():
    with open('tempurl.txt', 'r') as file:
        return file.read().strip()

def read_tempip():
    with open('tempip.txt', 'r') as file:
        return file.read().strip()

# ICEBAN
print(Fore.RED + "Banner Grab" + Style.RESET_ALL)
path_iceban = os.path.join(os.path.dirname(__file__), 'iceban.py')

iceban = execute_subprocess(["python3", path_iceban])

if iceban == 0:
    print(Fore.RED + "Banner Grab complete." + Style.RESET_ALL)
    print()
else:
    print(Fore.RED + f"ERROR! {iceban}." + Style.RESET_ALL)

tempurl = read_tempurl()

# ICERESOLV
print(Fore.RED + "Resolver" + Style.RESET_ALL)

path_iceresolv = os.path.join(os.path.dirname(__file__), 'iceresolv.py')

iceresolv = execute_subprocess(["python3", path_iceresolv, tempurl])

if iceresolv == 0:
    print(Fore.RED + "Resolver complete." + Style.RESET_ALL)
    print()
else:
    print(Fore.RED + f"ERROR! {iceresolv}." + Style.RESET_ALL)


tempip = read_tempip()

# ICEBLOCK
print(Fore.RED + "Net Block Consult" + Style.RESET_ALL)

path_iceblock = os.path.join(os.path.dirname(__file__), 'iceblock.py')

iceblock = execute_subprocess(["python3", path_iceblock, tempip])

if iceblock == 0:
    print(Fore.RED + "Net Block Consult complete." + Style.RESET_ALL)
    print()
else:
    print(Fore.RED + f"ERROR! {iceblock}." + Style.RESET_ALL)

# ICESUB
print(Fore.RED + "Consult, Zone Transfer & Subdomain Bruteforce" + Style.RESET_ALL)

path_icesub = os.path.join(os.path.dirname(__file__), 'icesub.py')

icesub = execute_subprocess(["python3", path_icesub, tempurl])

if icesub == 0:
    print(Fore.RED + "Subdomain Bruteforce complete." + Style.RESET_ALL)
    print()
else:
    print(Fore.RED + f"ERROR! {icesub}." + Style.RESET_ALL)

# ICEDIR
print(Fore.RED + "Directories Bruteforce" + Style.RESET_ALL)

path_icedir = os.path.join(os.path.dirname(__file__), 'icedir.py')

icedir = execute_subprocess(["python3", path_icedir, "--common", tempurl])
#uncomment the botton line for largest wordlist
#icedir = execute_subprocess(["python3", path_icedir, tempurl])

if icedir == 0:
    print(Fore.RED + "Directories Bruteforce complete." + Style.RESET_ALL)
    print()
else:
    print(Fore.RED + f"ERROR! {icedir}." + Style.RESET_ALL)

# ICEPHP
print(Fore.RED + "PHP Bruteforce" + Style.RESET_ALL)

path_icephp = os.path.join(os.path.dirname(__file__), 'icephp.py')

icephp = execute_subprocess(["python3", path_icephp, "--common", tempurl])
#uncomment the botton line for largest wordlist
#icephp = execute_subprocess(["python3", path_icephp, tempurl])

if icephp == 0:
    print(Fore.RED + "PHP Bruteforce complete." + Style.RESET_ALL)
    print()
else:
    print(Fore.RED + f"ERROR! {icephp}." + Style.RESET_ALL)

# ICESCAN
print(Fore.RED + "Scan" + Style.RESET_ALL)

continue_scan = input("Start Nmap Scanning? Y/N: ")

if continue_scan.strip().lower() == 'y':
    path_icescan = os.path.join(os.path.dirname(__file__), 'icescan.py')

    icescan = execute_subprocess(["python3", path_icescan, tempip])

    if icescan == 0:
        print(Fore.RED + "Scan complete!" + Style.RESET_ALL)
        print()
    else:
        print(Fore.RED + f"ERROR! {icescan}." + Style.RESET_ALL)
else:
    print(Fore.RED + "Finished!" + Style.RESET_ALL)


