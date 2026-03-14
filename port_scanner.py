print("=== Python Port Scanner ===")
import socket

target = input("Enter IP address or hostname: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

for port in range(start_port, end_port + 1):
    print(f"Checking port {port}...")
    try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is open")

    s.close()

except socket.error:
    print("Could not connect to host")

    if result == 0:
        print(f"Port {port} is open")

    s.close()
