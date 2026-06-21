# Sistema de Comunicação de Dados com ESP-NOW

## Descrição do Projeto

Este projeto implementa um sistema completo de transmissão e recepção de mensagens utilizando o algoritmo de codificação de linha AMI Pseudoternário, criptografia por Cifra de César e comunicação sem fio através do protocolo ESP-NOW.

A arquitetura do sistema é composta por:

* 1 ESP32 Master (Receptora)
* 2 ESP32 Slave (Transmissoras)

O sistema realiza todo o ciclo de comunicação digital, desde a entrada da mensagem pelo usuário até sua reconstrução completa no dispositivo receptor.

O objetivo é demonstrar os conceitos de Comunicação de Dados, incluindo:

* Criptografia de mensagens;
* Conversão ASCII para binário;
* Codificação de linha AMI Pseudoternária;
* Transmissão em rede entre computadores distintos;
* Comunicação sem fio entre dispositivos utilizando ESP-NOW;
* Decodificação e reconstrução da mensagem original.

---

# Bibliotecas Utilizadas

## Python

### CustomTkinter

Biblioteca utilizada para o desenvolvimento da interface gráfica do sistema.

Principais funções:

* Criação de janelas;
* Botões;
* Campos de texto;
* Labels;
* Organização visual dos elementos da aplicação.

### PySerial

Responsável pela comunicação serial entre o computador e as placas ESP32.

Principais funções:

* Identificação automática das placas;
* Comunicação serial;
* Envio de mensagens;
* Recepção de mensagens.

### Matplotlib

Utilizada para geração dos gráficos dos sinais codificados.

Principais funções:

* Construção dos gráficos AMI;
* Visualização do sinal transmitido;
* Visualização do sinal recebido.

### Time

Utilizada para controle de temporização durante a inicialização e sincronização das portas seriais.

### Serial.tools.list_ports

Utilizada para localizar automaticamente as portas USB disponíveis no sistema.

---

## ESP32

### WiFi.h

Biblioteca utilizada para habilitar os recursos sem fio da ESP32.

### esp_now.h

Biblioteca responsável pela implementação do protocolo ESP-NOW.

Principais funções:

* Comunicação direta entre ESP32;
* Envio de pacotes;
* Recepção de pacotes;
* Identificação do endereço MAC de origem;
* Registro de callbacks de transmissão e recepção.

---

# Estrutura dos Arquivos

## main.py

Ponto de entrada da aplicação.

Responsável por iniciar o sistema e abrir o menu principal.

---

## interfaceCTK.py

Implementa a tela inicial do sistema.

Permite selecionar o modo de operação:

* Slave (Transmissor)
* Master (Receptor)

---

## slaveCTK.py

Interface gráfica utilizada pelo transmissor.

Responsável por:

* Receber a mensagem digitada pelo usuário;
* Aplicar a criptografia;
* Converter a mensagem para binário;
* Aplicar a codificação AMI Pseudoternária;
* Exibir os resultados intermediários;
* Exibir o gráfico do sinal;
* Enviar os dados para a ESP transmissora.

---

## masterCTK.py

Interface gráfica utilizada pelo receptor.

Responsável por:

* Receber os dados vindos da ESP receptora;
* Identificar o transmissor através do endereço MAC;
* Exibir o gráfico recebido;
* Aplicar a decodificação AMI;
* Reconstruir o binário;
* Reconstruir o texto cifrado;
* Aplicar a descriptografia;
* Exibir a mensagem original.

---

## codification.py

Implementa todas as etapas de codificação e decodificação.

Funções principais:

* Cifra de César;
* Decifra de César;
* Conversão texto para binário;
* Conversão binário para texto;
* Codificação AMI Pseudoternária;
* Decodificação AMI Pseudoternária.

---

## grafics.py

Responsável pela construção dos gráficos utilizados na transmissão e recepção.

Funções principais:

* Geração do gráfico de transmissão;
* Geração do gráfico de recepção.

---

## esp_funct.py

Responsável pela comunicação serial com as ESP32.

Funções principais:

* Identificação automática dos dispositivos;
* Envio dos dados codificados;
* Recepção dos dados recebidos via ESP-NOW;
* Gerenciamento das conexões seriais.

---

## master.ino

Firmware da ESP32 receptora.

Responsabilidades:

* Receber pacotes ESP-NOW;
* Identificar o endereço MAC do transmissor;
* Encaminhar os dados para o computador;
* Responder ao mecanismo de identificação automática.

---

## slave.ino

Firmware das ESP32 transmissoras.

Responsabilidades:

* Receber dados do computador;
* Transmitir os dados utilizando ESP-NOW;
* Responder ao mecanismo de identificação automática.

---

# Funcionamento do Sistema

## Processo de Transmissão

1. O usuário digita uma mensagem na interface Slave.
2. A mensagem é criptografada utilizando a Cifra de César.
3. O texto criptografado é convertido para binário utilizando a tabela ASCII.
4. O binário é convertido para AMI Pseudoternário.
5. O gráfico do sinal é exibido.
6. Os dados são enviados para a ESP transmissora.
7. A ESP transmissora envia os dados utilizando ESP-NOW.

## Processo de Recepção

1. A ESP receptora recebe o pacote ESP-NOW.
2. O endereço MAC do transmissor é identificado.
3. Os dados são enviados ao computador receptor.
4. O gráfico do sinal recebido é exibido.
5. O sinal AMI é decodificado.
6. O binário é reconstruído.
7. O texto criptografado é reconstruído.
8. A descriptografia é aplicada.
9. A mensagem original é exibida ao usuário.

---

# Comunicação ESP-NOW

A comunicação entre as ESP32 utiliza o protocolo ESP-NOW.

Características da implementação:

* Comunicação sem necessidade de roteador;
* Comunicação sem acesso à Internet;
* Comunicação direta entre dispositivos;
* Baixa latência;
* Baixo consumo energético;
* Identificação automática do dispositivo transmissor através do endereço MAC.

O envio ocorre por broadcast, permitindo que múltiplas ESP32 transmissoras possam encaminhar mensagens para a ESP32 receptora.

---

# Identificação Automática das ESP32

Para evitar problemas causados pela alteração dinâmica das portas USB no sistema operacional, foi implementado um mecanismo de descoberta automática.

Durante a inicialização:

1. O Python percorre todas as portas seriais disponíveis.
2. O comando WHOAREYOU é enviado.
3. Cada ESP responde sua função.
4. A aplicação associa automaticamente cada dispositivo ao seu papel.

Respostas possíveis:

MASTER

ou

SLAVE

Dessa forma não é necessário configurar manualmente nenhuma porta serial.

---

# Identificação do Dispositivo Transmissor

Quando a ESP receptora recebe um pacote ESP-NOW, o endereço MAC do transmissor é extraído automaticamente.

A informação é enviada ao computador juntamente com os dados recebidos.

Exemplo:

34:5F:45:AA:F1:AC|1,0,0,-1,0,1

O software exibe ao usuário qual dispositivo realizou a transmissão, permitindo a utilização de múltiplas ESP32 Slave em um mesmo sistema.

---

# Testes Realizados

Durante o desenvolvimento foram realizados os seguintes testes:

* Validação da criptografia e descriptografia;
* Conversão texto para binário e reconstrução;
* Codificação e decodificação AMI Pseudoternária;
* Comunicação serial entre computador e ESP32;
* Comunicação ESP-NOW entre dispositivos;
* Comunicação entre computadores distintos;
* Identificação automática das ESP32;
* Identificação do endereço MAC do transmissor;
* Recepção simultânea de múltiplos dispositivos Slave.

---

# Como Executar

## Requisitos

* Python 3.10 ou superior;
* Arduino IDE;
* 3 ESP32 Dev Module;
* Sistema Linux.

## Instalação das Dependências

```bash
pip install customtkinter pyserial matplotlib
```

## Gravação das ESP32

* Gravar master.ino na ESP receptora;
* Gravar slave.ino nas ESP transmissoras.

## Execução

Conecte as ESP32 ao computador.

Execute:

```bash
python3 main.py
```

Selecione:

* Slave para transmissão;
* Master para recepção.

---

# Ambiente de Desenvolvimento

Projeto desenvolvido e testado em:

* Sistema Operacional: Ubuntu 22.04 LTS
* Python 3.10
* Arduino IDE 1.8.19
* ESP32 Dev Module
* Memória RAM: 16 GB

---

# Autores

Projeto desenvolvido para a disciplina de Comunicação de Dados.
