# MQTT Buzzer Project
Send MQTT messages by pressing a button on an ESP-12E. When a message is received, a buzzer plays a sound.

Pressing the button on the ESP-12E publishes an MQTT message which is then received by an MQTT broker running on the Raspberry Pi 3. The MQT-client also installed on the Pi, then subscribes to that topic. When the message contents match the expected string, the passive buzzer attached to the Pi makes a sound and a red LED lights up. Addittionally, the Pi also sends an email after receiving a message from the ESP-12E. The amount of buttons is scalable.

---

![alt text](https://github.com/PyhaMarkus/mqtt-buzzer-project/blob/master/pictures/buzzerproject_bb.png "sketch")

---

### Parts used for the button:
| Quantity | Part name                             |
| -------- |:-------------:                        |
| 1        | NodeMCU ESP-12E (esp8266)             |
| 1        | Large button                          |
| 1        | Red LED                               |
| 1        | 10K potentiometer                     |
| 1        | 220 ohm resistor                      |
| 2        | Small breadboard                      |
| A lot    | Jumper wire                           |

### Parts used for the buzzer:
| Quantity | Part name                             |
| -------- |:-------------:                        |
| 1        | Raspberry Pi 3 Model B                |
| 1        | Passive buzzer                        |
| 1        | RED LED                               |
| 1        | 100 ohm resistor                      |
| 1        | 220 ohm resistor                      |
| 2        | LED                                   |
| 1        | A small breadboard                    |
| A lot    | Jumper wire                           |

---

### Libraries used for the button:
*ESP8266WiFi.h
*PubSubClient.h

### Libraries used for the buzzer:
*time
*sys
*paho.mqtt.client
*RPi.GPIO
*smtplib

---
