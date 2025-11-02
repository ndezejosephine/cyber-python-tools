import socket
import sys
from datetime import datetime

print("=== SIMPLE PORT SCANNER ===")

#Get the target
target = input("Enter IP or hostname(e.g. 192.168.2.2 or example.com): ").strip()
if not target:
    print("No target provided.")
    sys.exit(1)  

try:
    resolved_ip = socket.gethostbyname(target)
except socket.gaierror:
    print(f"ERROR: cannot resolve host '{target}'. Check spelling or network.")
    sys.exit(1)


#List of ports to scan
ports = [22, 80, 443]
open_ports = []
results = []

print(f"Scanning {resolved_ip} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n") 
#Scan each port
for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    #socket.setttimeout(1)
    try:
        result = sock.connect_ex((resolved_ip, port))
    except Exception as e:
        print(f"Error for scanning {port}: {e}")
        result = 1
    finally:
        if result == 0:
            service = {22:"SSH", 80:"HTTP", 443:"HTTPS"}.get(port, "Unknown")
            status = f"{port}: OPEN --> {service}"
            open_ports.append(port)
        else:
            status = f"{port}: CLOSED"
        
        print(status)
        results.append(status)
        sock.close()

#Final Summary
print("\n" + "="*50)
print("SCAN COMPLETE")
print(f"Target : {resolved_ip}")
print(f"Open ports {len(open_ports)} --> {open_ports}")
print("="*50)

#Save Report
with open("scan_report.txt", "w") as f:
    f.write("PORTS SCAN REPORT")
    f.write(f"Target : {resolved_ip}\n")
    f.write(f"Ports scanned : {ports}\n")
    f.write(f"Time: {datetime.now()}\n")
    f.write(f"Open ports: {open_ports}\n")

    for line in results:
        f.write(line +"\n")
print("Report saved to: scan_report.txt")
