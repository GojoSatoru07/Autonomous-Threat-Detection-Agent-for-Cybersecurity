from scapy.all import IP, TCP, send
import time

def simulate_normal_traffic():
    print("Sending normal web traffic to 192.168.1.1:80")
    pkt = IP(dst="192.168.1.1") / TCP(dport=80, flags="S")
    send(pkt, verbose=False)
    print("Normal traffic sent.")

def simulate_port_scan():
    print("Simulating port scan on 8.8.8.8")
    for port in range(20, 1025, 100):
        pkt = IP(dst="8.8.8.8") / TCP(dport=port, flags="S")
        send(pkt, verbose=False)
        time.sleep(0.1)
    print("Port scan simulation completed.")

if __name__ == "__main__":
    print("1. Simulate Normal Traffic")
    print("2. Simulate Port Scan (Malicious)")
    choice = input("Select option (1/2): ").strip()

    if choice == "1":
        simulate_normal_traffic()
    elif choice == "2":
        simulate_port_scan()
    else:
        print("Invalid option.")
