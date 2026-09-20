# Simple Port Scanner - By GHOST_IN_SHELL
# For Educational Purposes Only
import socket

target = input("Enter IP (ex: 8.8.8.8): ")
ports = [21, 22, 23, 25, 53, 80, 443, 8080]

print(f"\n[+] Scanning {target}...")
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    if s.connect_ex((target, port)) == 0:
        print(f"[OPEN] Port {port} is open")
    s.close()
print("[+] Done!")
