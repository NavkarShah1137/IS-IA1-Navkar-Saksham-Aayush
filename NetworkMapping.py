# Netwrok Mapping Nmap Python Code.  

import nmap

# Prompt user for subnet to scan
subnet = input("Enter subnet to scan: ")

# Create a new nmap scanner object
nm = nmap.PortScanner()

# Perform network mapping scan on the specified subnet
nm.scan(hosts=subnet, arguments='-sn')

# Print out the list of hosts that were found
for host in nm.all_hosts():
    print('Host found: %s (%s)' % (host, nm[host].hostname()))
