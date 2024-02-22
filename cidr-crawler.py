import argparse
import ipaddress
import os

def save_ip_list(output_file, ip_list):
    with open(output_file, 'w') as file:
        for ip in ip_list:
            file.write(str(ip) + '\n')

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='CIDR IP Range Crawler')
    parser.add_argument('-c', '--cidr', help='CIDR to crawl', required=True)
    parser.add_argument('-o', '--output', help='Name of the file to save the list of IPs', required=True)
    args = parser.parse_args()

    # Crawl list of IPs from CIDR
    cidr = args.cidr
    ip_list = list(ipaddress.IPv4Network(cidr))

    # Get the output directory and ensure it exists
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the list of IPs into a file
    save_ip_list(args.output, ip_list)
    print(f"List of IPs has been saved to file: {args.output}")

if __name__ == "__main__":
    main()

