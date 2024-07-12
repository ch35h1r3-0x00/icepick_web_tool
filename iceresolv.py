import socket
import sys
from urllib.parse import urlparse
from colorama import Fore, Style

#print(Fore.RED + ''' /$$$$$$  /$$$$$$  /$$$$$$$$                                         /$$           
#|_  $$_/ /$$__  $$| $$_____/                                        | $$           
#  | $$  | $$  \__/| $$        /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$ | $$ /$$    /$$
#  | $$  | $$      | $$$$$    /$$__  $$ /$$__  $$ /$$_____/ /$$__  $$| $$|  $$  /$$/
#  | $$  | $$      | $$__/   | $$  \__/| $$$$$$$$|  $$$$$$ | $$  \ $$| $$ \  $$/$$/ 
#  | $$  | $$    $$| $$      | $$      | $$_____/ \____  $$| $$  | $$| $$  \  $$$/  
# /$$$$$$|  $$$$$$/| $$$$$$$$| $$      |  $$$$$$$ /$$$$$$$/|  $$$$$$/| $$   \  $/   
#|______/ \______/ |________/|__/       \_______/|_______/  \______/ |__/    \_/''' + Style.RESET_ALL + "v1.0")
#print("We're all mad here...")
print()

if len(sys.argv) != 2:
    print(Fore.RED + "Error! URL not received!" + Style.RESET_ALL)
    sys.exit(1)

host = sys.argv[1].strip()

parsed_url = urlparse(host)
hostname = parsed_url.hostname

if hostname:
    try:
        target_ip = socket.gethostbyname(hostname)
        print("Target IP:", target_ip)
        
        with open('tempip.txt', 'w') as file:
            file.write(target_ip)
        
        with open('target.txt', 'a') as file:
            file.write("\nTarget IP: " + target_ip)
    except socket.gaierror as e:
        print("Error during resolver hostname:", e)
else:
    print(Fore.RED + "Invalid URL" + Style.RESET_ALL)
print()

