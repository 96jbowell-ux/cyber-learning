target = input("Enter an IP address: ")

print("Starting scan on", target)

for port in range(1, 10):
    if port == 80:
        print("Port 80 OPEN (possible web server)")
    elif port == 22:
        print("Port 22 might be an (SSH)")
    else:
        print("Checking", target, "port", port)

print("Scan complete.")