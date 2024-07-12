import subprocess
from colorama import Fore, Style, init
import re
import sys

init(autoreset=True)

def dns_query(record_type, target):
    result = subprocess.run(["host", "-t", record_type, target], capture_output=True, text=True).stdout
    return result

def clean_target(target):
    target = re.sub(r'^https?://', '', target)
    target = target.strip('/')
    return target

def write_to_file(filename, content, mode='a'):
    with open(filename, mode) as file:
        file.write(content)

#print(Fore.RED + ''' /$$$$$$  /$$$$$$  /$$$$$$$$                     /$$      
#|_  $$_/ /$$__  $$| $$_____/                    | $$      
#  | $$  | $$  \__/| $$        /$$$$$$$ /$$   /$$| $$$$$$$ 
#  | $$  | $$      | $$$$$    /$$_____/| $$  | $$| $$__  $$
#  | $$  | $$      | $$__/   |  $$$$$$ | $$  | $$| $$  \ $$
#  | $$  | $$    $$| $$       \____  $$| $$  | $$| $$  | $$
# /$$$$$$|  $$$$$$/| $$$$$$$$ /$$$$$$$/|  $$$$$$/| $$$$$$$/
#|______/ \______/ |________/|_______/  \______/ |_______/''' + Style.RESET_ALL + "v1.0")
#print("We're all mad here...")
print()

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Error! URL not received!" + Style.RESET_ALL)
        sys.exit(1)

    target = sys.argv[1].strip()
    target = clean_target(target)
    print("\nBasic Consult:\n")
    
    with open('target.txt', 'a') as file:
        file.write(f"\n\nBasic Consult for {target}:\n\n")
    
        mx = dns_query("mx", target)
        print(" MX\n")
        print(mx)
        file.write("MX Records:\n" + mx + "\n")

        cname = dns_query("cname", target)
        print(" CNAME\n")
        print(cname)
        file.write("CNAME Records:\n" + cname + "\n")

        ns = dns_query("ns", target)
        print(" NS\n")
        print(ns)
        file.write("NS Records:\n" + ns + "\n")
    
        print("Trying Zone Transfer\n")
        file.write("Zone Transfer Attempts:\n")
        ns_servers = [line.split()[-1] for line in ns.splitlines() if "name server" in line]

        for server in ns_servers:
            server = server.strip('.')
            zone_transfer = subprocess.run(["host", "-l", "-a", target, server], capture_output=True, text=True).stdout
            print(zone_transfer)
            file.write(zone_transfer + "\n")

    option = input("Start Subdomain Bruteforce? (C)=Common (B)=Big (S)=Stop  ")

    if option.upper() == 'C':
        wordlist = 'commonsub.txt'
    elif option.upper() == 'B':
        wordlist = 'sub.txt'
    else:
        print(Fore.RED + "Stopping the code." + Style.RESET_ALL)
        return

    try:
        with open(wordlist, 'r') as file:
            with open('target.txt', 'a') as target_file:
                target_file.write("\nSubdomain Bruteforce Results:\n")
                for word in file:
                    word = word.strip()
                    result = subprocess.run(["host", f"{word}.{target}"], capture_output=True, text=True).stdout
                    if "NXDOMAIN" not in result:
                        print(result)
                        target_file.write(result + "\n")
    except FileNotFoundError:
        print(Fore.RED + f"Wordlist file '{wordlist}' not found." + Style.RESET_ALL)
        with open('target.txt', 'a') as target_file:
            target_file.write(f"Wordlist file '{wordlist}' not found.\n")

if __name__ == "__main__":
    main()

