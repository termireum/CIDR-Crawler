import ipaddress

cidr_example = ipaddress.ip_network('192.168.0.0/24')
for ip in cidr_example:
    print(ip)
