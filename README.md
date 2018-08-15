# MQTT Buzzer Project

Send MQTT messages by pressing a button on a NodeMCU ESP-12E. When a message is then received by the Raspberry Pi, a buzzer plays a sound.

Pressing the button on the ESP-12E publishes an MQTT message which is then received by an MQTT broker running on the Raspberry Pi 3. The MQT-client also installed on the Pi, then subscribes to that topic. When the message contents match the expected string, the passive buzzer attached to the Pi makes a sound and a red LED lights up. Addittionally, the Pi also sends me an email after receiving a message from the ESP-12E.

The amount of ESP-12Es and buttons can easily be increased with small additions to the source code.

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

---

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
![alt text](https://github.com/PyhaMarkus/mqtt-buzzer-project/blob/master/pictures/buzzerproject.jpg "img")
---

### Libraries used for the button:
* ESP8266WiFi.h
* PubSubClient.h

---

### Libraries used for the buzzer:
* time
* sys
* paho.mqtt.client
* RPi.GPIO
* smtplib

---

### Installation for the Raspberry Pi:

**Installing MQTT-broker and client**

```
sudo apt-get update
sudo apt-get install mosquitto
sudo apt-get install mosquitto-clients # not required but useful for testing purposes
wget https://files.pythonhosted.org/packages/2a/5f/cf14b8f9f8ed1891cda893a2a7d1d6fa23de2a9fb4832f05cef02b79d01f/paho-mqtt-1.3.1.tar.gz
tar -xzvf paho-mqtt-1.3.1.tar.gz
cd paho-mqtt-1.3.1
sudo python setup.py install
```
**Installing the python code from this repository**

```
sudo apt-get install git
git-clone https://github.com/PyhaMarkus/mqtt-buzzer-project.git
cd mqtt-buzzer-project
nano mqtt_buzzer.py # change the MQTT and email information to match yours
```
**Running the python code**

```
cd mqttbuzzer-project
python mqtt_buzzer.py
```
