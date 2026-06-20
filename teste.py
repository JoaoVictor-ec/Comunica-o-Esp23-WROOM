import serial
import time

esp = serial.Serial("/dev/ttyUSB0", 115200, timeout=2)

time.sleep(2)

while True:
    line = esp.readline().decode(errors="ignore").strip()

    print(repr(line))