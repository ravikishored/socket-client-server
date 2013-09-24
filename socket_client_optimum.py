# socket client by ravi ksihore dodda
import socket
import re

def client(sock):
    pass
    print "###################"
    print  sock.recv(1024)
    print "###################"
    print "please provide two parameters"
    print "example : 2 3"
    #data=""
    data=raw_input(">")
    match=re.search( r'^\d+\s+\d+', data) # checking at client side for providing exact info
    
    if(match):
        sock.sendall(data)
        data_server = sock.recv(1024)
        print 'Received',data_server
    else:
        print "please provide valid data"
        print "example : + 2 3"
        #continue
    
if __name__ == '__main__':
    HOST = 'localhost'    
    PORT = 50007          # same port as used by the server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    client(sock)
    sock.close()
    