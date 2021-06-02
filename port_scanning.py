from socket import *
import threading
import argparse


def scan_TCP_port(ip, port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        sock.connect((ip, port))
        print(f"TCP Port: {port} Open")
    except:
        print(f"TCP Port: {port} CLOSED")


def scan_UDP_port(ip, port):
    try:
        connect_sock = socket(AF_INET, SOCK_STREAM)
        connect_sock.connect((ip, port))
        print(f"UDP Port: {port} Open")
    except:
        print(f"UDP Port: {port} CLOSED")


def check(ip, ports, is_udp):
    for port in ports:
        if not is_udp:
            thread = threading.Thread(target=scan_TCP_port, args=(ip, int(port)))
        else:
            thread = threading.Thread(target=scan_UDP_port, args=(ip, int(port)))
        thread.start()


def main():
    print("Welcome To Port Scanner!\n")
    try:
        parser = argparse.ArgumentParser("Ports Scanner")
        parser.add_argument("-a", "--address", type=str, help="Enter the ip address to scan")
        parser.add_argument("-p", "--port", type=str, help="Enter The ports to scan")
        parser.add_argument("-u", "--udp", action="store_true")
        args = parser.parse_args()
        ip = args.address
        port = args.port.split(',')
        is_udp = args.udp
        check(ip, port, is_udp)
    except:
        print("format error\n example: python scan.py -a 127.0.0.1 -p 21,22,80")


if __name__ == "__main__":
    main()
