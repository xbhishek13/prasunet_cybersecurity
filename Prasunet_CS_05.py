from scapy.all import sniff
from scapy.layers.inet import IP

def packet_callback(packet):
    if IP in packet:  
        ip_layer = packet[IP]
        print(f"New Packet: {ip_layer.src} -> {ip_layer.dst} | Protocol: {ip_layer.proto}")

def start_sniffing(user_filter):
    print(f"Starting packet sniffer with filter: '{user_filter}'...")
    
    while True:
        try:
            count = int(input("Enter the number of packets you want to capture: "))
            break
        except ValueError:
            print("Please enter a valid integer for the packet count.")
    
    sniff(filter=user_filter, prn=packet_callback, count=count)

if __name__ == "__main__":
    user_filter = input("Enter your filter (e.g., 'ip', 'tcp', 'udp port 53', etc.): ")
    start_sniffing(user_filter)
