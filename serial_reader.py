from platform import system as check_os
from time import sleep, time
import requests
import serial

COM = '/dev/ttyACM0'
if check_os() == 'Windows':
    COM = 'COM3'
BAUD = 9600

ser = serial.Serial(COM, BAUD, timeout=.1)

print('Waiting for device')
sleep(3)
print(ser.name)

while True:
    val = str(ser.readline().decode().strip('\r\n'))
    valA = val.split("/")
    if val != '':
        data = {
            'time': time(),
            'temperature': val
        }
        requests.post('http://localhost/celsius/post', data)
