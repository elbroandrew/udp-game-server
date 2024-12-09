import socket


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # dgram is UDP
udp_socket.bind(("127.0.0.1", 5001))


while True:

    print("waiting for data...")
    msg, addr = udp_socket.recvfrom(1024)
    msg = bytes.decode(msg)
    print('Server UDP msg received: ', msg)
    
    q = input("SHUT DOWN THE SERVER ?  y//n: ")
    if q == 'y':
        break

udp_socket.sendto(b"SESSION TERMINATED", addr)

udp_socket.close()