#include <esp_now.h>
#include <WiFi.h>

// Callback executada quando chega uma mensagem
void OnDataRecv(
    const esp_now_recv_info_t *info,
    const uint8_t *incomingData,
    int len)
{
    String dadosRecebidos = "";

    for (int i = 0; i < len; i++)
    {
        dadosRecebidos += (char)incomingData[i];
    }

    char macStr[18];

    snprintf(
        macStr,
        sizeof(macStr),
        "%02X:%02X:%02X:%02X:%02X:%02X",
        info->src_addr[0],
        info->src_addr[1],
        info->src_addr[2],
        info->src_addr[3],
        info->src_addr[4],
        info->src_addr[5]
    );

    Serial.print(macStr);
    Serial.print("|");

    Serial.println(dadosRecebidos);
}

void setup()
{
    Serial.begin(115200);

    WiFi.mode(WIFI_STA);

    delay(1000);

    Serial.println("MASTER");

    Serial.print("MAC: ");
    Serial.println(WiFi.macAddress());

    if (esp_now_init() != ESP_OK)
    {
        Serial.println("Erro ao inicializar ESP-NOW");
        return;
    }

    esp_now_register_recv_cb(OnDataRecv);

    Serial.println("ESP receptora pronta.");
}

void loop()
{
    if (Serial.available())
    {
        String cmd = Serial.readStringUntil('\n');

        cmd.trim();

        if (cmd == "WHOAREYOU")
        {
            Serial.println("MASTER");
        }
    }
}
