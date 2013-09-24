# socket server program by ravi kishore dodda
import socket


class MyServer():
    def __init__(self):
        self.data_client=""
        pass
    
    def get(self,conn,addr):
        pass
        print "getting data from client"
        conn.send("I supports addition")
        self.data_client=conn.recv(1024)
        if not self.data_client:
            exit(1)
            
    def add(self,conn,addr):
        pass
        print self.data_client
        data = self.data_client.split()
        return int(data[0])+int(data[1])
        
    def post(self,conn,addr,result):
        conn.send("addition "+str(result))
        conn.close()
    
    
if __name__ == '__main__':
    HOST = ''        
    PORT = 50007              # non-privileged port
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind((HOST, PORT))
    soc.listen(5)
    print "server started......"
    while True:
        conn, addr = soc.accept()
        print 'Connected by', addr
        request=MyServer()
        request.get(conn,addr)
        result=request.add(conn,addr)
        request.post(conn,addr,result)
    soc.close()