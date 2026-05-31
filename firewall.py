from rules_engine import load_rules, is_blocked

def monitor_traffic():
    test_packets = [
        {"ip": "192.168.1.10", "port": 80},
        {"ip": "8.8.8.8", "port": 22},
        {"ip": "1.1.1.1", "port": 443}
    ]

    rules = load_rules()

    for packet in test_packets:
        if is_blocked(packet, rules):
            print("BLOCKED:", packet)
        else:
            print("ALLOWED:", packet)

if __name__ == "__main__":
    monitor_traffic()
