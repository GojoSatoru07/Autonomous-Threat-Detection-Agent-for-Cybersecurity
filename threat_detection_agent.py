import csv
from collections import defaultdict
from datetime import datetime, timedelta

LOG_FILE = "traffic_log.csv"
ALERT_LOG = "alerts.csv"

# Rule: Too many connections from the same IP in a short time
THRESHOLD = 10  # suspicious if more than 10 packets
TIME_WINDOW = 10  # in seconds

def read_traffic():
    with open(LOG_FILE, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)

def detect_port_scan(traffic):
    ip_activity = defaultdict(list)

    for row in traffic:
        src_ip = row["Source IP"]
        timestamp = datetime.strptime(row["Timestamp"], "%Y-%m-%d %H:%M:%S")
        ip_activity[src_ip].append(timestamp)

    flagged_ips = []
    for ip, times in ip_activity.items():
        times.sort()
        for i in range(len(times)):
            window = times[i:i+THRESHOLD]
            if len(window) == THRESHOLD and (window[-1] - window[0]).seconds <= TIME_WINDOW:
                flagged_ips.append(ip)
                break

    return flagged_ips

def log_alerts(flagged_ips):
    with open(ALERT_LOG, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Suspicious IP", "Reason"])
        for ip in flagged_ips:
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ip, "Port scan or DoS pattern"])

def main():
    print("Analyzing traffic log...")
    traffic = read_traffic()
    flagged_ips = detect_port_scan(traffic)

    if flagged_ips:
        print(f"⚠️  Detected suspicious IPs: {flagged_ips}")
        log_alerts(flagged_ips)
    else:
        print("✅ No suspicious activity detected.")

if __name__ == "__main__":
    main()
