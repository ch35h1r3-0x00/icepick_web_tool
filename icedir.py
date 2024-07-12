import argparse
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, init
from datetime import datetime

init(autoreset=True)

def read_payload(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def try_payload(url, payload, out_file):
    full_url = url + payload
    try:
        response = requests.get(full_url, timeout=5)
        if response.status_code in [200, 302, 401]:
            result = f"{full_url} - {response.status_code}"
            print(result)
            with open(out_file, 'a') as out_file_append:
                out_file_append.write(result + '\n')
    except Exception:
        pass

def brute_force(url, payloads, out_file, max_workers=50):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(try_payload, url, payload, out_file) for payload in payloads]
        for future in as_completed(futures):
            future.result()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ICEdir - Directory Enumerator")
    parser.add_argument("url", help="Target URL")
    parser.add_argument("--common", action="store_true", help="Use common directory wordlist")
    args = parser.parse_args()

#    print(Fore.RED + ''' /$$$$$$  /$$$$$$  /$$$$$$$$       /$$ /$$          
#|_  $$_/ /$$__  $$| $$_____/      | $$|__/          
#  | $$  | $$  \__/| $$        /$$$$$$$ /$$  /$$$$$$ 
#  | $$  | $$      | $$$$$    /$$__  $$| $$ /$$__  $$
#  | $$  | $$      | $$__/   | $$  | $$| $$| $$  \__/
#  | $$  | $$    $$| $$      | $$  | $$| $$| $$      
# /$$$$$$|  $$$$$$/| $$$$$$$$|  $$$$$$$| $$| $$      
#|______/ \______/ |________/ \_______/|__/|__/''' + Style.RESET_ALL + "v1.0")
#    print("We're all mad here...")
    print()
    
    url = args.url.strip()
    print()

    output_file = 'target.txt'

    start_time = datetime.now()

    with open(output_file, 'a') as out_file:       
        out_file.write('\nDirectories:\n')

    if args.common:
        payload_list = read_payload('1000commondir.txt')
    else:
        payload_list = read_payload('dir.txt')

    brute_force(url, payload_list, output_file)

    end_time = datetime.now()

