import serial
import time

# port configuration
device = ''  # example '/dev/ttyUSB0'
baudrate = 9600

port = serial.Serial(device, baudrate)

# read data from the serial port
while True:
    if port.isOpen():
        data = port.readline().decode('utf-8').rstrip()
        print(data)
        print('\n')
        time.sleep(500)
    
    else:
        print('Serial port is not open, check your device!')