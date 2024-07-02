from pymavlink import mavutil

class Pixhawk:
    
    def __init__(self, port="/dev/ttyACM0", baudrate=115200):
        self.ROV = mavutil.mavlink_connection(port, baud=baudrate)
        self.ROV.wait_heartbeat()
        self.Rov.set_mode(0)   #Set STABILIZE mode as default 
        
    def heartbeat(self):
        while True : 
            self.ROV.heartbeat_send(mavutil.mavlink.MAV_TYPE_GCS, mavutil.mavlink.MAV_AUTOPILOT_INVALID,mavutil.mavlink.MAV_MODE_FLAG_TEST_ENABLED ,0, 0)
            print('heartbeat')
        
    def set_gribber_light_pwm(self, servo_n, microseconds):
        self.ROV.mav.command_long_send(
            self.ROV.target_system,
            self.ROV.target_component,
            mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
            0,
            servo_n + 8,
            microseconds,
            0, 0, 0, 0, 0
        )

    def set_direction_channel_pwm(self, channel_id, pwm=1500):
        if channel_id < 1 or channel_id > 9:
            print("Channel does not exist.")
            return

        rc_channel_values = [65535 for _ in range(9)]
        rc_channel_values[channel_id - 1] = pwm
        self.ROV.mav.rc_channels_override_send(
            self.ROV.target_system,
            self.ROV.target_component,
            *rc_channel_values
        )
        
    def arm(self):
        self.ROV.arducopter_arm()
        
    def disarm(self):   
        self.ROV.arducopter_disarm()

    def Set_Flight_Mode(self,mode):
        if mode not in self.ROV.mode_mapping():
            print('Unknown mode : {}'.format(mode))
            print('Try:', list(self.ROV.mode_mapping().keys()))
             
        mode_id = self.ROV.mode_mapping()[mode]
        
        self.Rov.set_mode(mode_id)