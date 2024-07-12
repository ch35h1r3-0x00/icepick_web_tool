import subprocess
from colorama import init, Fore, Style
import argparse

init()

def run_nmap_scan(target, ports, scan_types):
    command = ["nmap", "-v", "-oN", "target.txt", "--append-output"] + scan_types + ["-p", ports, target]
    subprocess.run(command)

#print(Fore.RED + ''' /$$$$$$  /$$$$$$  /$$$$$$$$                                        
#|_  $$_/ /$$__  $$| $$_____/                                        
#  | $$  | $$  \__/| $$        /$$$$$$$  /$$$$$$$  /$$$$$$  /$$$$$$$ 
#  | $$  | $$      | $$$$$    /$$_____/ /$$_____/ |____  $$| $$__  $$
#  | $$  | $$      | $$__/   |  $$$$$$ | $$        /$$$$$$$| $$  \ $$
#  | $$  | $$    $$| $$       \____  $$| $$       /$$__  $$| $$  | $$
# /$$$$$$|  $$$$$$/| $$$$$$$$ /$$$$$$$/|  $$$$$$$|  $$$$$$$| $$  | $$
#|______/ \______/ |________/|_______/  \_______/ \_______/|__/  |__/ ''' + Style.RESET_ALL + "v1.0")
#print("We're all mad here...")
print()

def main():
    parser = argparse.ArgumentParser(description="ICE - Nmap Scanner")
    parser.add_argument("target", help="Target for the scan")
    args = parser.parse_args()

    target = args.target.replace("https://", "").replace("http://", "")

    print('''\nChoose scan type:\n
1- 10000 TCP ports
2- 10000 TCP ports + Operational System + Service Version
3- All TCP ports
4- 1000 UDP ports
5- 1000 UDP ports + Operational System + Service Version
6- All UDP ports
7- All open ports
8- AGGRESSIVE''')

    option = int(input("Choose an option (1-8): "))

    scan_types = []
    if option == 1:
        scan_types = ["-sT", "--top-ports=10000"]
    elif option == 2:
        scan_types = ["-sT", "-sV", "-O", "--top-ports=10000"]
    elif option == 3:
        scan_types = ["-sT", "-p-"]
    elif option == 4:
        scan_types = ["-sU", "--top-ports=1000"]
    elif option == 5:
        scan_types = ["-sU", "-sV", "-O", "--top-ports=1000"]
    elif option == 6:
        scan_types = ["-sU", "-p-"]
    elif option == 7:
        scan_types = ["-sS", "-p-", "--open"]
    elif option == 8:
        scan_types = ["-sS", "-O", "-sV", "-p-", "--script=vuln"]

    if "-p-" in scan_types:
        ports = "-"
    elif "--top-ports" in scan_types:
        ports = "1-10000"
    else:
        ports = "1-1000"

    run_nmap_scan(target, ports, scan_types)

if __name__ == "__main__":
    main()

