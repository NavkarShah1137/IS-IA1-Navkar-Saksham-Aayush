import nmap

# Prompt user for IP address or subnet to scan
target = input("Enter IP address or subnet to scan: ")

# Create a new nmap scanner object
nm = nmap.PortScanner()

# Perform full host discovery scan on the specified IP address or subnet
nm.scan(hosts=target, arguments='-sS -sV -O')

# Print out the list of hosts that were found
for host in nm.all_hosts():
    print('Host found: %s (%s)' % (host, nm[host].hostname()))
