from bs4 import BeautifulSoup
import requests
from colorama import Fore, Style
import ipaddress
import socket

#print(Fore.RED + ''' /$$$$$$  /$$$$$$  /$$$$$$$$       /$$                    
#|_  $$_/ /$$__  $$| $$_____/      | $$                    
#  | $$  | $$  \__/| $$        /$$$$$$$ /$$$$$$$   /$$$$$$$
#  | $$  | $$      | $$$$$    /$$__  $$| $$__  $$ /$$_____/
#  | $$  | $$      | $$__/   | $$  | $$| $$  \ $$|  $$$$$$ 
#  | $$  | $$    $$| $$      | $$  | $$| $$  | $$ \____  $$
# /$$$$$$|  $$$$$$/| $$$$$$$$|  $$$$$$$| $$  | $$ /$$$$$$$/
#|______/ \______/ |________/ \_______/|__/  |__/|_______/''' + Style.RESET_ALL + "v1.0")
#print("We're all mad here...")
print()

target_ip = input(Fore.YELLOW + "|||[Give me a target:]|||" + Style.RESET_ALL).strip()
print()

def find_info_in_pre_tag(pre_tags, search_term):
    for pre_tag in pre_tags:
        if search_term in pre_tag.text:
            for line in pre_tag.text.split('\n'):
                if search_term in line:
                    return line.strip()
    return None

def consult_whois(target_ip):
    url = f"https://www.whois.com/whois/{target_ip}"
    resp = requests.get(url)
    if resp.status_code == 200:
        bs = BeautifulSoup(resp.text, "html.parser")
        pre_tags = bs.find_all("pre")
        
        cidr_info = find_info_in_pre_tag(pre_tags, "CIDR:")
        if cidr_info:
            print(Fore.BLUE + cidr_info + Style.RESET_ALL)
            print()
            return cidr_info.split(":")[1].strip()  
        
        inetnum_info = find_info_in_pre_tag(pre_tags, "inetnum:")
        if inetnum_info:
            print(Fore.BLUE + inetnum_info + Style.RESET_ALL)
            print()
            return inetnum_info.split(":")[1].strip()  
        
        print("No information found in WHOIS.")
        return None
    else:
        print(f"WHOIS request failed. Status code: {resp.status_code}")
        return None

range_cidr = consult_whois(target_ip)
if range_cidr:
    ip_list = [str(ip) for ip in ipaddress.IPv4Network(range_cidr)]
    
    hostnames = []
    for ip in ip_list:
        try:
            hostname = socket.gethostbyaddr(ip)
            print(Fore.GREEN + f"Found hostname for IP {ip}: {hostname}" + Style.RESET_ALL)
            hostnames.append(hostname)
        except Exception:
            pass  
    
    for hostname in hostnames:
        print(Fore.BLUE + str(hostname) + Style.RESET_ALL)
else:
    print("No information found.")

