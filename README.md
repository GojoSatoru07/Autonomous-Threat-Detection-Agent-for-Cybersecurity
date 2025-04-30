# 🛡️ Autonomous Threat Detection Agent for Cybersecurity

An intelligent and lightweight cybersecurity agent designed to detect and respond to suspicious network activities in real-time. Built using Python and Scapy, the system can simulate, capture, and analyze network traffic to autonomously identify potential threats such as DoS attacks and port scanning.

---

## 📂 Project Structure


---

## ⚙️ Features

- 🧠 **Autonomous Threat Detection**: Identifies potential attacks without human intervention.
- 📊 **Real-time Packet Logging**: Captures key features of network packets.
- 🔍 **Rule-based Detection**: Flags suspicious patterns such as DoS or port scanning.
- 🚦 **Traffic Simulation**: Generates both benign and attack traffic for testing.
- 💾 **CSV Logging**: Stores all traffic and alerts in accessible `.csv` format.

---

## 🧪 Requirements

- Python 3.7+
- [Scapy](https://scapy.readthedocs.io/en/latest/)
- [Npcap](https://nmap.org/npcap/) (for packet capture on Windows)

Install dependencies:

```bash
pip install -r requirements.txt
Activate the virtual environment:

# Windows
.\threat-agent-env\Scripts\activate

Start Packet Logger (in one terminal):
python packet_logger.py

Simulate Traffic (in another terminal):
python traffic_simulator.py

Run Threat Detection Agent (in another terminal):
python threat_detection_agent.py

🔍 Detection Logic
The agent analyzes traffic_log.csv to identify:

📌 DoS-style Flooding: Excessive packets from a single IP in a short time.

🧭 Port Scanning: Access to multiple ports in a short duration.

Future rules (SYN flood, DNS tunneling, etc.) can be easily added.

🛠️ Customization
Adjust detection thresholds in threat_detection_agent.py.

Add new traffic patterns in traffic_simulator.py.

Extend the detection logic to include more complex or ML-based techniques.

🧠 Future Enhancements
✅ Machine learning-based anomaly detection

📈 Real-time web dashboard for live threat monitoring

📬 Email/SMS alerts using SMTP or Twilio

🧵 Multithreaded or asynchronous packet processing for scalability
