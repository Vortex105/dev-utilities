import socket
import threading

# port_numbers = [22, 80, 443, 8080]


# def checkPort():
#     for port in port_numbers:
#         newSocket = socket.socket()
#         newSocket.settimeout(1)
#         try:
#             newSocket.connect(("google.com", port))
#             print(f"Port {port} is open")
#             newSocket.close()
#         except Exception as e:
#             print(f"Port {port} is closed")
#             print(e)


# checkPort()

# host = input("Enter the host to check: ")
# start_port = int(input("Enter the starting port number: "))
# end_port = int(input("Enter the ending port number: "))


# def check_ports(host, start_port, end_port):
#     for port in range(start_port, end_port + 1):
#         newSocket = socket.socket()
#         newSocket.settimeout(1)
#         try:
#             newSocket.connect((host, port))
#             print(f"Port {port} is open")
#             newSocket.close()
#         except Exception as e:
#             print(f"Port {port} is closed")
#             # Uncomment the next line to see the exception details
#             # print(e)


# check_ports(host, start_port, end_port)


# Version 2


def get_scan_details():
    host = input("Enter the host to check: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))
    return host, start_port, end_port


def check_port(host, port):
    newSocket = socket.socket()
    newSocket.settimeout(1)
    try:
        newSocket.connect((host, port))
        print(f"Port {port} is open")
    except Exception as e:
        print(f"Port {port} is closed")
        # Uncomment the next line to see the exception details
        # print(e)
    finally:
        newSocket.close()


def scan_ports(host, start_port, end_port):
    threads = []

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=check_port, args=(host, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def main():
    host, start_port, end_port = get_scan_details()
    scan_ports(host, start_port, end_port)


main()
