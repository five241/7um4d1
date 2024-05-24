import socket
import threading

python_banner = '''
_______   ____  ___  _________  __  
|___  / | | |  \/  | /   |  _  \/  | 
   / /| | | | .  . |/ /| | | | |`| | 
  / / | | | | |\/| / /_| | | | | | | 
./ /  | |_| | |  | \___  | |/ / _| |_
\_/    \___/\_|  |_/   |_/___/  \___/
                                     
'''

# Menampilkan banner Python
print(python_banner)
import socket
from colorama import Fore, Style, init

init(autoreset=True)


def portscan(target, port):
  try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    sock.connect((target, port))
    print(f"[+] Port {port} terbuka")
    sock.close()
  except:
    pass

if __name__ == "__main__":
  target = input("Masukkan alamat IP target: ")
  ports = range(1, 9999)  # Ubah rentang port sesuai kebutuhan

  threads = []
  for port in ports:
    thread = threading.Thread(target=portscan, args=(target, port))
    threads.append(thread)
    thread.start()

  for thread in threads:
    thread.join()
