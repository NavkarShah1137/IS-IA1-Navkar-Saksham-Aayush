import nmap

# Prompt user for IP address to scan
ip_address = input("Enter IP address to scan: ")

# Create a new nmap scanner object
nm = nmap.PortScanner()

# Perform OS detection scan on the specified IP address
nm.scan(hosts=ip_address, arguments='-O')

# Print out the OS information for the host
if ip_address in nm.all_hosts():
    if 'osmatch' in nm[ip_address]:
        os_match = nm[ip_address]['osmatch']
        for os in os_match:
            print('OS Name : %s\tAccuracy : %s' % (os['name'], os['accuracy']))
    else:
        print('OS information not found')
else:
    print('Host not found')
