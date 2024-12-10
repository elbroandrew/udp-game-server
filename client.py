import socket
import sys
import pygame
import select


class Game:
    def __init__(self):
        
        pygame.init()

        W,H = 800,600

        self.screen = pygame.display.set_mode((W,H))
        self.clock = pygame.time.Clock()
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    def run(self):
        
        self.udp_socket.sendto(b'Client message', ('127.0.0.1', 5001))
        self.udp_socket.setblocking(False)
        inputs, outputs = [self.udp_socket], [self.udp_socket]
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.udp_socket.close()
                    pygame.quit()
                    sys.exit()
                    
            rlist, wlist, exlist = select.select(inputs, outputs, inputs)
            for s in rlist:
                if s is self.udp_socket:
                    msg, server = self.udp_socket.recvfrom(1024)
                    if msg:
                        msg = bytes.decode(msg)
                        print("CLIENT RECIEVED MSG: ", msg)
                    else:
                        print("SERVER CLOSED THE CONNECTION")
                        sys.exit(1)
                    

            self.screen.fill((0, 0, 0))
            pygame.display.flip()
            self.clock.tick(60)
            
            
            
            
    # def client_handle(self):
    #     msg, server = self.udp_socket.recvfrom(1024)
    #     msg = bytes.decode(msg)
    #     print("CLIENT RECIEVED MSG: ", msg)




if __name__ == "__main__":
    try:
        Game().run()
    except socket.error:
        sys.exit(1)