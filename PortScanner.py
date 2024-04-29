import pyfiglet
import sys
import socket
from datetime import datetime

def display_banner():
    """
    Display an ASCII art banner for the port scanner.
    """
    ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
    print(ascii_banner)

def scan_ports(target_ip):
    """
    Scan common ports on the specified IP address.

    Args:
        target_ip (str): The IP address to scan.

    Returns:
        None
    """
    print("_" * 50)
    print("Scanning Target: " + target_ip)
    print("Scanning Started At: " + str(datetime.now()))
    print("-" * 50)

    try:
        for port in range(1, 100):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port} is open")
                s.close()

    except KeyboardInterrupt:
        print("\nExiting Program !!!")
        sys.exit()

    except socket.gaierror:
        print("\nHostname Could Not Be Resolved !!!")
        sys.exit()

    except socket.error:
        print("\nServer not Responding !!!")
        sys.exit()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python portscanner.py <IP address>")
        sys.exit(1)

    target_ip = sys.argv[1]
    display_banner()
    scan_ports(target_ip)