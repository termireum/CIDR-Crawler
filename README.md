# CIDR-Crawler
CIDR-Crawler is script used to generate a list of IP addresses within a network based on CIDR (Classless Inter-Domain Routing) notation. The script utilizes Python's built-in ipaddress module to parse network addresses and print each IP address included within the network.

**How to use?**

**usage:** cidr.py [-h] -c CIDR -o OUTPUT

**Example:** python3 cidr-crawler.py -c 192.168.0.0/24 -o custom_filename.txt

**CIDR IP Range Crawler**

optional arguments:
  -h, --help            show this help message and exit
  -c CIDR, --cidr CIDR  CIDR to crawl
  -o OUTPUT, --output OUTPUT
                        Name of file to save the list of IPs

**Example command to run the script while scanning for open ports within a specific CIDR range**

Example: python3 cidr.py -c 192.168.0.0/24 -o ip_list.txt -p 80,443,22

In this example:

-c 192.168.0.0/24 specifies the CIDR range to be scanned.

-o ip_list.txt specifies the filename to save the list of IP addresses.

-p 80,443,22 specifies the ports to be scanned, in this case, 80 (HTTP), 443 (HTTPS), and 22 (SSH). You can add or remove these ports as needed, separating them by commas if specifying more than one port.

**Disclaimer**

_This script is provided as-is, without any warranty or guarantee of any kind. The author shall not be held liable for any damages or losses resulting from the use of this script. Use it at your own risk. The information provided by this script is for educational purposes only. The author does not guarantee the accuracy or completeness of the information provided. By using this script, you agree to hold the author harmless from any claims or damages arising from its use. Please use this script responsibly and only on systems that you have permission to access._
