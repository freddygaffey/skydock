from pymavlink import mavutil

# Connect to the flight controller (STM32H743)
master = mavutil.mavlink_connection('/dev/ttyACM1', baud=115200)

try:
    # Wait for heartbeat confirmation
    print("Waiting for connection...")
    master.wait_heartbeat()
    
    print("Connected successfully!")
    
    while True:
        msg = master.recv_msg()
        
        if msg is not None:
            print(f"\nReceived: {msg}")
            
                
except KeyboardInterrupt:
    print("\nDisconnected cleanly")

