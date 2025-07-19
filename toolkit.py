import socket
import requests

def scan_ports(target, ports):
    print(f"Scanning {target} for open ports...")
    open_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((target, port))
                if result == 0:
                    open_ports.append(port)
        except Exception:
            pass
    return open_ports

def check_http(target):
    try:
        response = requests.get(f"http://{target}", timeout=3)
        print(f"HTTP Status for {target}: {response.status_code}")
    except Exception as e:
        print(f"HTTP check failed for {target}: {e}")

if __name__ == "__main__":
    target = input("Enter target (e.g., 192.168.1.1 or example.com): ").strip()
    ports = [21, 22, 23, 80, 443, 8080]
    open_ports = scan_ports(target, ports)
    print("Open Ports:", open_ports)
    check_http(target)