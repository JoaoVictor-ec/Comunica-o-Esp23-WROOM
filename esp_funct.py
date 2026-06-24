import serial
import time
from serial.tools import list_ports



def find_esp(device_type):

    ports = list_ports.comports()

    for port in ports:

        try:

            esp = serial.Serial(
                port.device,
                115200,
                timeout=1
            )

            time.sleep(2)

            esp.reset_input_buffer()

            esp.write(b"WHOAREYOU\n")

            time.sleep(0.2)

            response = (
                esp.readline()
                .decode(errors="ignore")
                .strip()
            )

            print(
                f"{port.device} respondeu: {response}"
            )

            if response == device_type:

                print(
                    f"{device_type} encontrada em {port.device}"
                )

                return esp

            esp.close()

        except Exception as e:

            print(e)

    return None
#funcao para enviar uma mensagem para o ESP e receber a resposta
def send_ami(esp, ami):

    if esp is None:
        return

    data = ",".join(map(str, ami))

    esp.write(
        (data + "\n").encode()
    )

#funcao para receber a resposta
def receive_ami(esp):

    if esp is None:
        return None

    if esp.in_waiting == 0:
        return None

    data = (
        esp.readline()
        .decode(errors="ignore")
        .strip()
    )

    if not data:
        return None

    try:

        mac, ami_data = data.split("|")

        ami = [
            int(x)
            for x in ami_data.split(",")
        ]

        return {
            "mac": mac,
            "ami": ami
        }

    except Exception as e:

        print(f"Erro ao processar AMI: {e}")
        print(f"Dado recebido: {data}")

        return None