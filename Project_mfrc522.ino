#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN 9 
#define SS_PIN 10 

MFRC522 mfrc522(SS_PIN, RST_PIN);
void setup() {
  Serial.begin(9600);  // Initialize serial communications with the PC
  while (!Serial)
    ;                  // Do nothing if no serial port is opened
  SPI.begin();         // Init SPI bus
  mfrc522.PCD_Init();  // Init MFRC522
  delay(4);
}

void loop() {
  if (mfrc522.PICC_IsNewCardPresent()) {
    // Read the card's UID
    String uid = getID();
    if (uid != "") {
      Serial.println(uid);
      delay(1000);
    }
  }
}

String getID() {
  if (!mfrc522.PICC_ReadCardSerial()) {  //Since a PICC placed get Serial and continue
    return "";
  }
  String hex_num = "";
  hex_num = String(mfrc522.uid.uidByte[0], HEX);
  hex_num += String(mfrc522.uid.uidByte[1], HEX);
  hex_num += String(mfrc522.uid.uidByte[2], HEX);
  hex_num += String(mfrc522.uid.uidByte[3], HEX);
  mfrc522.PICC_HaltA();  // Stop reading
  return hex_num;
}
