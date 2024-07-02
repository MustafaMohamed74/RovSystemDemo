from UnderWater.SocketBackage.MySocket import UnderWaterSoket
from UnderWater.PixhawkBackage.Pixhawk import Pixhawk
import threading

client_socket = UnderWaterSoket('192.168.33.14', port=55555)

pix = Pixhawk("/dev/ttyACM0", baudrate=115200)

my_thread = threading.Thread(target=pix.heartbeat)
my_thread.start()

FlightModeFlag = 0 

while True:
    msg = client_socket.recive()
   
    print(msg)
    
    FlightModeFlag = msg[7] 
    if int(msg[7])!=FlightModeFlag :
      pix.Set_Flight_Mode(msg[7])
    
    if int(msg[6]) == 1 :
      pix.arm()
    else:
      pix.disarm()
    
    pix.set_direction_channel_pwm(5,int(msg[0]))
    pix.set_direction_channel_pwm(6,int(msg[1]))
    pix.set_direction_channel_pwm(3,int(msg[2]))
    pix.set_direction_channel_pwm(4,int(msg[3]))
    pix.set_gribber_light_pwm(5,int(msg[4])*20000)
    pix.set_gribber_light_pwm(4,int(msg[5])*20000)

    
  
   

client_socket.close()