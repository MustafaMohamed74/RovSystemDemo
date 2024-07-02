import socket 

class UnderWaterSoket : 
    def __init__(self , ip= '192.168.33.14', port= 5535):
       
        self.client_socket = socket.socket()
        
        try:
            self.client_socket.connect((ip , port))
            print("Connection Stablished")
            
        except Exception as e:
            print(f"Connection error: {e}")
    def recive(self):
       return  self.client_socket.recv(26).decode().split()
   

