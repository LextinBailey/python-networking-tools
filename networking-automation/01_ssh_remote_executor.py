import paramiko

host = input("Enter target IP: ")
username = input("Enter username: ")
password = input("Enter password: ")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Lab Environment Only

client.connect(
    hostname=host,
    username=username,
    password=password
)

stdin, stdout, stderr = client.exec_command("uptime")

output = stdout.read().decode()

print("\nCommand Output:")
print(output)

client.close()