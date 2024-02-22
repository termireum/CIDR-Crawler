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

    # Add arguments
    parser.add_argument('-c', '--cidr', help='CIDR to crawl', required=True)
    parser.add_argument('-o', '--output', help='Name of file to save the list of IPs', required=True)
    parser.add_argument('-p', '--ports', help='Comma-separated list of ports to scan (optional)', type=str)

    # Parse arguments
    args = parser.parse_args()

    # Crawl IP list from CIDR
    cidr = args.cidr
    ip_list = list(ipaddress.IPv4Network(cidr))

    # Get the output directory and ensure it exists
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save IP list to file
    save_ip_list(args.output, ip_list)
    print(f"List of IPs saved to file: {args.output}")

if __name__ == "__main__":
    main()
