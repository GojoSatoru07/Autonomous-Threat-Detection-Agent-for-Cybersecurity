from scapy.all import sniff, IP, TCP
import csv
from datetime import datetime

LOG_FILE = "traffic_log.csv"

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet.proto
        time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(LOG_FILE, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([time_str, ip_src, ip_dst, proto])
        print(f"[{time_str}] {ip_src} → {ip_dst} (proto={proto})")

def setup_csv():
    with open(LOG_FILE, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Timestamp", "Source IP", "Destination IP", "Protocol"])

if __name__ == "__main__":
    setup_csv()
    print("Starting packet capture (press Ctrl+C to stop)...")
    sniff(prn=packet_callback, store=0)
