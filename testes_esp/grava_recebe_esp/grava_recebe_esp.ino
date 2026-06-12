#include <esp_now.h>
#include <WiFi.h>

// Função que é ativada AUTOMATICAMENTE quando chega uma mensagem pelo ar
void OnDataRecv(const uint8_t * mac, const uint8_t *incomingData, int len) {
  // Converte os dados recebidos (bytes) de volta para uma String
  String dadosRecebidos = "";
  for (int i = 0; i < len; i++) {
    dadosRecebidos += (char)incomingData[i];
  }
  
  // Imprime no cabo USB para o Python do PC 2 ler
  Serial.println(dadosRecebidos);
}

void setup() {
  Serial.begin(115200);
  
  // Coloca a ESP em modo Wi-Fi Station
  WiFi.mode(WIFI_STA);

  // Inicializa o ESP-NOW (Fica em silêncio se der erro, para não poluir o Python)
  if (esp_now_init() == ESP_OK) {
    // Diz à ESP qual função chamar quando os dados chegarem
    esp_now_register_recv_cb(OnDataRecv);
  }
}

void loop() {
  // O loop fica completamente vazio! 
  // O ESP-NOW trabalha em "background" de forma automática.
}
