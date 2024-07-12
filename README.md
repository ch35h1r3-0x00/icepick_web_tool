
$$$$$$\  $$$$$$\  $$$$$$$$\           $$\           $$\       
\_$$  _|$$  __$$\ $$  _____|          \__|          $$ |      
  $$ |  $$ /  \__|$$ |       $$$$$$\  $$\  $$$$$$$\ $$ |  $$\ 
  $$ |  $$ |      $$$$$\    $$  __$$\ $$ |$$  _____|$$ | $$  |
  $$ |  $$ |      $$  __|   $$ /  $$ |$$ |$$ /      $$$$$$  / 
  $$ |  $$ |  $$\ $$ |      $$ |  $$ |$$ |$$ |      $$  _$$<  
$$$$$$\ \$$$$$$  |$$$$$$$$\ $$$$$$$  |$$ |\$$$$$$$\ $$ | \$$\ 
\______| \______/ \________|$$  ____/ \__| \_______|\__|  \__|
                            $$ |                              
                            $$ |                              
                            \__|

Icepick Web Tool is a basic set of tools for web recon and scanning.
The tool has 6 wordlists (default and common), which can be changed according to the user's needs.
When starting, the code asks for a URL and follows the order below for its activities:
	
-banner grab
-resolver
-netblock
-subdomain bruteforce
-directories bruteforce
-php bruteforce
-nmap scan

Usage Mode:
sudo python3 icepick.py

***the url must be entered in the format:
http://example.com/
or
https://example.com/
no "www"

The tool has 7 scripts that can be used independently, with the exception of iceban.py which does not ask for arguments as it works with interactive input.
Usage Mode:
python3 scriptname.py argument
To use the tool with a more extensive wordlist in icedir.py and icephp.py we can comment the line containing  --common and uncomment the next line in the code:

#icedir = execute_subprocess(["python3", path_icedir, "--common", tempurl])
#uncomment the botton line for largest wordlist
icedir = execute_subprocess(["python3", path_icedir, tempurl])

In the icescan.py code, nmap parameters can be changed or added in the sections below:

if option == 1:
        scan_types = ["-sT", "--top-ports=10000"]
        output_suffix = "nmapTCP10000"
    elif option == 2:
        scan_types = ["-sT", "-sV", "-O", "--top-ports=10000"]
        output_suffix = "nmapTCP10000_full"
    elif option == 3:
        scan_types = ["-sT", "-p-"]
        output_suffix = "nmapTCP_all"
    elif option == 4:
        scan_types = ["-sU", "--top-ports=1000"]
        output_suffix = "nmapUDP1000"
    elif option == 5:
        scan_types = ["-sU", "-sV", "-O", "--top-ports=1000"]
        output_suffix = "nmapUDP1000_full"
    elif option == 6:
        scan_types = ["-sU", "-p-"]
        output_suffix = "nmapUDP_all"
    elif option == 7:
        scan_types = ["-sS", "-p-", "--open"]
        output_suffix = "nmap_all"
    elif option == 8:
        scan_types = ["-sS", "-O", "-sV", "-p-", "--script=vuln"]
        output_suffix = "nmap_aggressive"

Obs: The code will always create 3 files:
tempurl.txt: contains the url used by icepick.py.
tempip.txt: contains the IP used by icepick.py.
target.txt: contains the information obtained during execution.
