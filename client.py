import socket, sys


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = input("TEXT FOR SERVER: ")
    msg = str.encode(msg) # to bytes
    
    udp_socket.sendto(msg, ('127.0.0.1', 5001))  # same as UDP server socket

    udp_socket.settimeout(20)

    msg, server = udp_socket.recvfrom(1024)
    msg = bytes.decode(msg)
    print("CLIENT RECIEVED MSG: ", msg)

    udp_socket.close()
    
if __name__ == "__main__":
    try:
        main()
    except socket.timeout:
        sys.exit(1)