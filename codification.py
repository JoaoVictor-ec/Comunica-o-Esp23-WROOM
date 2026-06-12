#cifra de cesar que soma a cada letra da mensagem +25 usando o padrão da tabela ascii estendida.
def codification_cifra_cesar(mesage):
    key = 25
    result = ""

    for caracter in mesage:
        result += chr((ord(caracter) + key) % 256)#o módulo garante que pra valores que passam de 255 continue usando a conversão da ascii corretamente.

    return result

#decoficação da cifra
def decodification_cifra_cesar(message):
    key = 25
    result = ""

    for caracter in message:
        result += chr((ord(caracter) - key) % 256)

    return result

#####################################################################################################################################################

#função que transforma de string pra binário 8bits.
def word_to_bin(mesage):
    data = mesage.encode('latin-1')#coverte para bytes do padrão latin-1
    binary = ""
    for byte in data:
        binary += format(byte, '08b')#converte os bytes extraidos em data para bits, fazendo substrings de 8 bits. Concatena elas pra saida.

    return binary

#função que pega um binário e transforma em string
def bin_to_word(binary):

    mesage = bytearray()

    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        mesage.append(int(byte, 2))

    return mesage.decode('latin-1')


####################################################################################################################################################

#AMI - Alternate Mark Inversion significa que para o binário 0 --> 0V e para o 1 --> alterna entre +V e -V

#Bits:  1 0 1 1 0 0 1
#AMI:  + 0 - + 0 0 -

# o fato de ser pseudoternário significa que simplismente inverte a lógica 1 → 0V e 0 → alterna entre +V e -V
#codificação usando as regras acima
def codification_AmiPseudoternario(bits):
    bin_cod = []
    last_signal = -1

    for bit in bits:
        if bit == '1':
            bin_cod.append(0)
        else:#se for 0 ele vai ver qual o ultimo sinal e inverter
            last_signal *= -1
            bin_cod.append(last_signal)

    return bin_cod

#decodificação usando as regras acima
def decodification_AmiPseudoternario(bin_cod):
    bits = ""

    for cod in bin_cod:
        if cod == (-1) or cod == (1):
            bits += '0'
        else:
            bits += '1'

    return bits
#######################################################################################################################################################