from scapy.all import ARP, Ether, srp

network = input("Enter network (e.g. 192.168.1.0/24): ")

arp_request = ARP(pdst=network)
broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = broadcast / arp_request

answered, unanswered = srp(
    packet,
    timeout=2,
    verbose=False
)

print(f"Found {len(answered)} devices.")

for sent, received in answered:
    print(f"IP: {received.psrc}")
    print(f"MAC: {received.hwsrc}")
    print()

