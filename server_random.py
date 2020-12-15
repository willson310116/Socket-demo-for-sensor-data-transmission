import socket
import traceback
import time
import random

class SocketServer():
    def __init__(self, host="127.0.0.1", port=8080):
        self.host = host
        self.port = port
        self.sock = None
    
    def initialize(self):
        # AF_INET : IPV4
        # SOCK_STREAM: TCP
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def listen(self):
        try:
            # () -> tuple (any, any) -> (int, str)
            self.sock.bind((self.host, self.port))
            # time out
            # self.sock.settimeout(2)  
            print(f"listen on {self.host}, {self.port}")
            self.sock.listen(1) # wait blocking -> sleep
            (conn, address) = self.sock.accept()
            """
               listen : 8080
               client -> server 44468 -> 8080
               44468
            """
            print(f"Succesfully from {address}")
            return conn
        except:
            traceback.print_exc()

    def send_text(self, conn, text):
        #send non-blocking
        """
        byte 0x121245 
        str "1234"
        utf-8 
        0~128 0xff -> utf-8
        """
        print(message)
        conn.send(text.encode('utf-8')) # bytes

        """
        1. send
        2. send_all 6000000 / (4096 | 1024)
        """

    def recv_text(self, conn):
        msg = conn.recv(4096)
        return msg

    def close_conn(self,conn):
        conn.close()

    def close_socket(self):
        self.sock.close()
    


if __name__ == "__main__":
    
    socket_server = SocketServer("127.0.0.1", 9999)
    """ 1024 up"""
    socket_server.initialize()
    conn = socket_server.listen() #from  (conn, address) = self.sock.accept()
    while True:
        # message = input("What do you want to send: ")
        x = input("r for random data/ q for quit: ")
        if x == "r":
            message = ""
            for i in range(15):
                message += str(round(random.uniform(1,10),2))
                message += ","

            message = message[:-1]
            socket_server.send_text(conn, message)
            msg = socket_server.recv_text(conn)
            print(msg)
            # time.sleep(1)
            # print(message)
            
        if x == "q":
            print("quit")
            #socket.SHUT_RDWR
            '''
            conn.close()
            socket.SHUT_RDWR
            socket.close()
            '''
            message = "q"
            socket_server.send_text(conn, message)
            msg = socket_server.recv_text(conn)
            print(msg)
            socket_server.close_conn(conn)
            break

        # socket_server.send_text(conn, message)
        # msg = socket_server.recv_text(conn)
        # print(msg)
        # # time.sleep(1)
            
    
    socket_server.close_socket()
            
            