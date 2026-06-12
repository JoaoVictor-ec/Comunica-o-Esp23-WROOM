import serial
import time

PORT = "/dev/ttyUSB0"#porta usb
BAUDRATE = 115200#rate de tranferencia de bits da esp

#estabelece conexão com a esp
def connect_esp():
    esp = serial.Serial(PORT, BAUDRATE)

    # espera a ESP inicializar
    time.sleep(2)

    # limpa lixo da serial
    esp.reset_input_buffer()

    return esp

#manda a codificação ami invertida
def send_ami(esp, ami):

    data = ",".join(map(str, ami))

    esp.write((data + "\n").encode())

#recebe a codificação ami invertida
def receive_ami(esp):

    data = esp.readline().decode().strip()

    if not data:
        return None

    ami = [int(x) for x in data.split(",")]

    return ami