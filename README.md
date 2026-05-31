# PyShield-Firewall
A lightweight, extensible firewall written in Python for learning, research, and security experimentation.
🔥 PyShield Firewall

A lightweight, extensible firewall written in Python for learning, research, and security experimentation.

✨ Features

- IP blocking / allow lists
- Port filtering
- Rule-based engine (JSON)
- Logging system
- Modular architecture

🧠 Use Cases

- Local host firewall
- Network monitoring lab
- Security research
- Educational tool

📁 Project Structure

pyshield-firewall/
│── src/
│   ├── firewall.py
│   ├── rules_engine.py
│   ├── packet_inspector.py
│
│── config/
│   └── rules.json
│
│── logs/
│
│── README.md
│── requirements.txt

⚙️ Installation

git clone https://github.com/vegasdude/pyshield-firewall.git
cd pyshield-firewall
pip install -r requirements.txt

▶️ Run

python src/firewall.py

🛡 Example Rules

{
  "blocked_ips": ["192.168.1.10"],
  "blocked_ports": [22, 23]
}

🔮 Future Features

- Web dashboard
- AI anomaly detection
- Docker deployment
- Real packet capture (Scapy)

⚠️ Disclaimer

This project is for educational use only.
