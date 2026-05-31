import json

def load_rules():
    with open("config/rules.json") as f:
        return json.load(f)

def is_blocked(packet, rules):
    if packet["ip"] in rules["blocked_ips"]:
        return True
    if packet["port"] in rules["blocked_ports"]:
        return True
    return False
