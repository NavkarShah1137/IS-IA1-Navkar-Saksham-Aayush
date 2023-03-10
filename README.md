# IS-IA1-Navkar-Saksham-Aayush
IS IA1 Navkar , Saksham , Aayush  

**Group No** : 1  
**Names of Students :** Navkar Shah , Aayush Durgule , Saksham Raina  
**Student Roll Numbers :** 16010120189 , 16010120203 , 16010120204  
**Name of Tool for Implementation :** Nmap (Network Mapper)  
**Brief Information about the Tool :** Nmap is a network exploration tool and security scanner that is used to discover hosts and services on a computer network and to security audit the network.  
**List of features / functionalities proposed to be implemented :** Host Discovery , Port Scanning , Version Detection , OS Detection , Network Mapping. 

Nmap Download Link:  https://nmap.org/download.html.  
Python Nmap Library:  pip install python-nmap.  

Nmap (“Network Mapper”) is an open source tool for network exploration and security auditing. It was designed to rapidly scan large networks, although it works fine against single hosts. Nmap uses raw IP packets in novel ways to determine what hosts are available on the network, what services (application name and version) those hosts are offering, what operating systems (and OS versions) they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics. While Nmap is commonly used for security audits, many systems and network administrators find it useful for routine tasks such as network inventory, managing service upgrade schedules, and monitoring host or service uptime.  

The output from Nmap is a list of scanned targets, with supplemental information on each depending on the options used. Key among that information is the “interesting ports table”. That table lists the port number and protocol, service name, and state. The state is either open, filtered, closed, or unfiltered. Open means that an application on the target machine is listening for connections/packets on that port. Filtered means that a firewall, filter, or other network obstacle is blocking the port so that Nmap cannot tell whether it is open or closed. Closed ports have no application listening on them, though they could open up at any time. Ports are classified as unfiltered when they are responsive to Nmap's probes, but Nmap cannot determine whether they are open or closed. Nmap reports the state combinations open|filtered and closed|filtered when it cannot determine which of the two states describe a port. The port table may also include software version details when version detection has been requested. When an IP protocol scan is requested (-sO), Nmap provides information on supported IP protocols rather than listening ports.  

In addition to the interesting ports table, Nmap can provide further information on targets, including reverse DNS names, operating system guesses, device types, and MAC addresses.  
