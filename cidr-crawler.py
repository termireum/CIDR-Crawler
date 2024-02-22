import argparse
import ipaddress
import os
import socket

def save_ip_list(output_file, ip_list):
    with open(output_file, 'w') as file:
        for ip in ip_list:
            file.write(str(ip) + '\n')

def scan_ports(ip_list, ports):
    open_ports = {}
    for ip in ip_list:
        open_ports[ip] = []
        for port in ports:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.5)  # Set timeout untuk koneksi
                    result = s.connect_ex((str(ip), port))
                    if result == 0:
                        open_ports[ip].append(port)
            except Exception as e:
                print(f"Error scanning port {port} on {ip}: {e}")
    return open_ports

def main():
    # Buat parser argumen
    parser = argparse.ArgumentParser(description='CIDR IP Range Scanner')
    parser.add_argument('-c', '--cidr', help='CIDR untuk di-scan', required=True)
    parser.add_argument('-o', '--output', help='Nama file untuk menyimpan daftar IP', required=True)
    parser.add_argument('-p', '--ports', help='Port yang akan di-scan (pisahkan dengan koma)', required=True)
    args = parser.parse_args()

    # Crawl daftar IP dari CIDR
    cidr = args.cidr
    ip_list = list(ipaddress.IPv4Network(cidr))

    # Dapatkan direktori output dan pastikan itu ada
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Simpan daftar IP ke dalam file
    save_ip_list(args.output, ip_list)
    print(f"Daftar IP telah disimpan ke dalam file: {args.output}")

    # Scan port
    ports = [int(port.strip()) for port in args.ports.split(',')]
    open_ports = scan_ports(ip_list, ports)
    for ip, port_list in open_ports.items():
        if port_list:
            print(f"IP {ip} memiliki port terbuka: {', '.join(map(str, port_list))}")
        else:
            print(f"Tidak ada port terbuka pada IP {ip}")

if __name__ == "__main__":
    main()
