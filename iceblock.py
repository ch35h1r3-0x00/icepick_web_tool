import socket
import sys
import subprocess
from colorama import Fore, Style

#print(Fore.RED + ''' /$$$$$$  /$$$$$$  /$$$$$$$$ /$$       /$$                     /$$      
#|_  $$_/ /$$__  $$| $$_____/| $$      | $$                    | $$      
#  | $$  | $$  \__/| $$      | $$$$$$$ | $$  /$$$$$$   /$$$$$$$| $$   /$$
#  | $$  | $$      | $$$$$   | $$__  $$| $$ /$$__  $$ /$$_____/| $$  /$$/
#  | $$  | $$      | $$__/   | $$  \ $$| $$| $$  \ $$| $$      | $$$$$$/ 
#  | $$  | $$    $$| $$      | $$  | $$| $$| $$  | $$| $$      | $$_  $$ 
# /$$$$$$|  $$$$$$/| $$$$$$$$| $$$$$$$/| $$|  $$$$$$/|  $$$$$$$| $$ \  $$
#|______/ \______/ |________/|_______/ |__/ \______/  \_______/|__/  \__/''' + Style.RESET_ALL + "v1.0")
#print("We're all mad here...")
print()

if len(sys.argv) != 2:
    print(Fore.RED + "Error! IP not received!" + Style.RESET_ALL)
    sys.exit(1)

target_ip = sys.argv[1].strip()
print()

def find_info_in_output(output, search_term):
    for line in output.split('\n'):
        if search_term in line:
            return line.strip()
    return None

def write_to_file(filename, content, mode='a'):
    with open(filename, mode) as file:
        file.write(content)

def consult_whois(target_ip):
    try:
        result = subprocess.run(['whois', target_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            output = result.stdout
            cidr_info = find_info_in_output(output, "CIDR:")
            inetnum_info = find_info_in_output(output, "inetnum:")
            
            if cidr_info:
                print(cidr_info)
                print()
                write_to_file('target.txt', "\n\n" + cidr_info)
            else:
                print("No CIDR information found.")
            
            if inetnum_info:
                print(inetnum_info)
                print()
                write_to_file('target.txt', "\n\n" + inetnum_info + "\n")
            else:
                print("No inetnum information found.")
            
            return cidr_info or inetnum_info
        else:
            print(f"WHOIS command failed: {result.stderr}")
            return None
    except Exception as e:
        print(f"An error occurred while running WHOIS: {e}")
        return None

whois_info = consult_whois(target_ip)
if not whois_info:
    print("No information found.")

