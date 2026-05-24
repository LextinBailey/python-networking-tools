import socket

target = input("Enter target IP: ")

start_port = int(input("Start port: "))
end_port = int(input("End port: "))

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is closed")
    
    sock.close()