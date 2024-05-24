import os
import socket
from colorama import Fore, Style, init

init(autoreset=True)

python_banner = '''
_______   ____  ___  _________  __  
|___  / | | |  \/  | /   |  _  \/  | 
   / /| | | | .  . |/ /| | | | |`| | 
  / / | | | | |\/| / /_| | | | | | | 
./ /  | |_| | |  | \___  | |/ / _| |_
\_/    \___/\_|  |_/   |_/___/  \___/
                                     
'''

def check_ip(ip, port, output_file):
    try:
        socket.setdefaulttimeout(0.5)
        sock = socket.create_connection((ip, port))
        result = f"IP {ip} on port {port} is {Fore.GREEN}[VULN]{Style.RESET_ALL}"
        print(result)
        with open(output_file, "a") as out_file:
            out_file.write(result + "\n")
        sock.close()
    except (socket.timeout, socket.error):
        result = f"IP {ip} on port {port} is {Fore.RED}[NOT VULN]{Style.RESET_ALL}"
        print(result)

def main():
    filename = input("Enter input filename: ")  # Meminta nama file input dari pengguna
    output_file = input("Enter output filename: ")  # Meminta nama file output dari pengguna
    output_folder = "result"
    output_file = os.path.join(output_folder, output_file)  # Menyimpan output di dalam folder 'result'

    port = 80

    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        with open(filename, "r") as file:
            ip_list = file.read().splitlines()
            for ip in ip_list:
                check_ip(ip, port, output_file)
    except FileNotFoundError:
        print(f"File {filename} not found")

if __name__ == "__main__":
    print(python_banner)
    main()
