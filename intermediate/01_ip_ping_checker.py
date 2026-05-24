import subprocess

file_path = input("Enter path to IP file: ")

try:
    with open(file_path, "r") as file:
        ips = file.readlines()
        ips = [ip.strip() for ip in ips]
except FileNotFoundError:
    print("File not found. Please check the path.")
    exit()

for ip in ips:
    result = subprocess.run(
        ["ping", "-c", "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if result.returncode == 0:
        print(f"{ip} is UP")
    else:
        print(f"{ip} is DOWN")