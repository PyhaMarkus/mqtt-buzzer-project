// Include libraries:
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// WLAN information:
const char* ssid = "your_network_ssid";
const char* password = "your_password";

// MQTT-broker information:
const char* mqttServer = "192.168.43.223";
const int mqttPort = 1883; // Change this to whatever port you're using for MQTT. 1883 by default.

// Define GPIO pins
const int buttonPin = 12;
const int ledPin = 4;

int buttonState = 0; // default button status

// Allows establishing a connection to the MQTT-broker
WiFiClient espClient;
PubSubClient client(espClient);

// Setup starts here:
void setup() {
  // Initialize LED pin as output
  pinMode(ledPin, OUTPUT);

  // Initialize button pin as input:
  pinMode(buttonPin, INPUT);

  // Initialize a serial connection for outputs
  Serial.begin(115200);
  
  // Connect to the WiFi network
  WiFi.begin(ssid, password);
  // While WiFi is not connected,
  while (WiFi.status() != WL_CONNECTED) {
 
    delay(1000);
    Serial.println("Connecting to WiFi...");
    
  }

  // When WiFi has connected, output IP-address
  Serial.println(WiFi.localIP());

  // Specify the Ip-address and port of the MQTT-broker
  client.setServer(mqttServer, mqttPort);

}

// Loop function runs over and over again
void loop() {
  // Read the state of the button:
  buttonState = digitalRead(buttonPin);

    // If WiFi has been connected to and the button has been pressed,
    if (WiFi.status() == WL_CONNECTED && buttonState == HIGH) {

      Serial.println("We're connected to WiFi/MQTT-broker and the buttonState is HIGH!");

      // While MQTT-broker has not been connected to,
      while (!client.connected()) {
        Serial.println("Connecting to MQTT-broker...");

        // If connection has been successful,
        if (client.connect("ESP8266Client")) {
 
          Serial.println("Connected to MQTT-broker and the button has been pressed!");  

        // If not,
        } else {
 
            Serial.print("failed with state ");
            Serial.print(client.state());
            delay(2000);
 
          }
      }

      // Publish a message with the topic and contents of:
      client.publish("support/button1", "buttonState is HIGH - Button 1");

      // Turn the LED on for 3 seconds.
      digitalWrite(ledPin, HIGH);
      delay(3000);
      digitalWrite(ledPin, LOW);

      // If the WiFi has been connected to but the button has not been pressed,
    } else if (WiFi.status() == WL_CONNECTED && buttonState == LOW) {
     
      Serial.println("We're connected to WiFi and buttonState is LOW!");
      
      // If neither of the above arguments is True, then...
    } else {

      Serial.println("We're NOT connected to WiFi!");
      
      }  
}
