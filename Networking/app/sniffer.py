from scapy.all import sniff, IP
import requests

# FastAPI endpoint where we send captured packets
API_URL = "http://127.0.0.1:8000/logs/"

# Function to send captured data to FastAPI
def send_to_api(source_ip, destination_ip, protocol, packet_size):
    data = {
        "source_ip": source_ip,
        "destination_ip": destination_ip,
        "protocol": protocol,
        "packet_size": packet_size
    }
    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            print("Packet logged successfully!")
        else:
            print("Failed to log packet:", response.text)
    except Exception as e:
        print("Error sending data:", e)

# Function to process captured packets
def process_packet(packet):
    if packet.haslayer(IP):  # Only process IP packets
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol = packet[IP].proto
        packet_size = len(packet)
        
        print(f"Captured: {source_ip} → {destination_ip} | Protocol: {protocol} | Size: {packet_size}")
        
        # Send data to FastAPI
        send_to_api(source_ip, destination_ip, str(protocol), packet_size)

# Function to start sniffing
def start_sniffing(interface="enp0s3"):
    print(f"🚀 Sniffing on {interface}... Press Ctrl+C to stop.")
    sniff(prn=process_packet, iface=interface, store=False)

if __name__ == "__main__":
    network_interface = input("Enter network interface (e.g., eth0, wlan0, lo): ")
    start_sniffing(network_interface)
