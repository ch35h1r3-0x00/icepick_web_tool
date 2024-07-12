import socket
from colorama import Fore, Style
import ssl

def print_banner():
    # print(Fore.RED + ''' /$$$$$$  /$$$$$$  /$$$$$$$$ /$$                          
    #|_  $$_/ /$$__  $$| $$_____/| $$                          
    #  | $$  | $$  \__/| $$      | $$$$$$$   /$$$$$$  /$$$$$$$ 
    #  | $$  | $$      | $$$$$   | $$__  $$ |____  $$| $$__  $$
    #  | $$  | $$      | $$__/   | $$  \ $$  /$$$$$$$| $$  \ $$
    #  | $$  | $$    $$| $$      | $$  | $$ /$$__  $$| $$  | $$
    # /$$$$$$|  $$$$$$/| $$$$$$$$| $$$$$$$/|  $$$$$$$| $$  | $$
    #|______/ \______/ |________/|_______/  \_______/|__/  |__/''' + Style.RESET_ALL + "v1.0")
    # print("We're all mad here...")
    print()

def print_banner():
    print()

def sanitize_host(host):
    if host.endswith("/"):
        host = host[:-1]
    return host

def write_to_file(url):
    with open('tempurl.txt', 'w') as file:
        file.write(url)

def write_output_to_file(host, output):
    with open(f"target.txt", 'w') as file:
        file.write(output)

def http_request(host):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, 80))

    request = ("HEAD / HTTP/1.1\r\nHost:%s\r\n\r\n" % host).encode('utf-8')
    sock.send(request)

    banner = sock.recv(1024)
    sock.close()
    output = banner.decode('utf-8')
    print()
    print(output)
    tempurl = "http://" + host + "/"
    write_to_file(tempurl)
    write_output_to_file(host, output)

def https_request(host):
    context = ssl.create_default_context()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockSSL = context.wrap_socket(sock, server_hostname=host)

    sockSSL.connect((host, 443))

    request = ("HEAD / HTTP/1.1\r\nHost:%s\r\n\r\n" % host).encode('utf-8')
    sockSSL.send(request)

    banner = sockSSL.recv(1024)
    sockSSL.close()
    output = banner.decode('utf-8')
    print()
    print(output)
    tempurl = "https://" + host + "/"
    write_to_file(tempurl)
    write_output_to_file(host, output)

def main():
    print_banner()
    host = input(Fore.RED + "Give me a target:" + Style.RESET_ALL).strip()
    if host.startswith("http://"):
        host = sanitize_host(host[len("http://"):])
        http_request(host)
    elif host.startswith("https://"):
        host = sanitize_host(host[len("https://"):])
        https_request(host)
    else:
        print(Fore.RED + "Invalid URL format. Please start with http:// or https://." + Style.RESET_ALL)
        return

if __name__ == "__main__":
    main()

