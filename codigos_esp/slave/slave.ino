#include <esp_now.h>
#include <WiFi.h>

// Broadcast
uint8_t broadcastAddress[] = {
  0xFF, 0xFF, 0xFF,
  0xFF, 0xFF, 0xFF
};

esp_now_peer_info_t peerInfo;

// Callback chamada quando o envio termina
void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status)
{
  Serial.print("Status do envio: ");

  if (status == ESP_NOW_SEND_SUCCESS)
  {
    Serial.println("SUCESSO");
  }
  else
  {
    Serial.println("FALHA");
  }
}

void setup()
{
  Serial.begin(115200);

  WiFi.mode(WIFI_STA);

  delay(1000);

  Serial.println("SLAVE");

  Serial.print("MAC: ");
  Serial.println(WiFi.macAddress());

  if (esp_now_init() != ESP_OK)
  {
    Serial.println("Erro ao inicializar ESP-NOW");
    return;
  }

  esp_now_register_send_cb(OnDataSent);

  memcpy(peerInfo.peer_addr, broadcastAddress, 6);
  peerInfo.channel = 0;
  peerInfo.encrypt = false;

  if (esp_now_add_peer(&peerInfo) != ESP_OK)
  {
    Serial.println("Erro ao adicionar peer");
    return;
  }

  Serial.println("ESP transmissora pronta.");
}

void loop()
{
    if (Serial.available() > 0)
    {
        String cmd = Serial.readStringUntil('\n');

        cmd.trim();

        // Responde à identificação solicitada pelo Python
        if (cmd == "WHOAREYOU")
        {
            Serial.println("SLAVE");
            return;
        }

        // Qualquer outra mensagem é tratada como AMI
        String dadosAMI = cmd;

        if (dadosAMI.length() == 0)
        {
            return;
        }

        Serial.println("=================================");
        Serial.println("ENVIANDO PACOTE");

        Serial.print("Tamanho: ");
        Serial.println(dadosAMI.length());

      bool sucesso = true;

      const int CHUNK_SIZE = 200;

      // envia o inicio
      esp_now_send(
          broadcastAddress,
          (uint8_t*)"START",
          5
      );

      delay(20);

      // envia os fragmentos
      for (
          int i = 0;
          i < dadosAMI.length();
          i += CHUNK_SIZE
      )
      {
          unsigned int fim = i + CHUNK_SIZE;

          if (fim > dadosAMI.length())
          {
              fim = dadosAMI.length();
          }

          String parte =
              dadosAMI.substring(i, fim);

          esp_err_t result = esp_now_send(
              broadcastAddress,
              (uint8_t*)parte.c_str(),
              parte.length()
          );

          if (result != ESP_OK)
          {
              sucesso = false;
          }

          delay(20);
      }

      // envia o fim
      esp_now_send(
          broadcastAddress,
          (uint8_t*)"END",
          3
      );

      if (sucesso)
      {
          Serial.println("Pacotes enviados");
      }
      else
      {
          Serial.println("Erro em algum fragmento");
      }
    }
  }