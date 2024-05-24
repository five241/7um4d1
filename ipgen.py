import random

def generate_ip_tail():
  """Generate IP ekor / nilai akhir secara urut dari 1 hingga 500."""
  for ip_tail in range(1, 501):
    yield ip_tail

def main():
  ip_awal = input("Masukkan IP awal (misalnya, 192.168.1.): ")
  filename = input("Masukkan nama file untuk menyimpan hasil: ")

  with open(filename, "w") as f:
    for ip_tail in generate_ip_tail():
      full_ip = f"{ip_awal}.{ip_tail}"
      f.write(f"{full_ip}\n")

  print(f"Hasil disimpan di file {filename}")

if __name__ == "__main__":
  main()
