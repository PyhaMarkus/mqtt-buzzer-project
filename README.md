# MQTT Buzzer Project
Send MQTT messages by pressing a button on an ESP-12E. When a message is received, a buzzer plays a sound.

Pressing the button on the ESP-12E publishes an MQTT message which is then received by an MQTT broker running on the Raspberry Pi 3. The MQT-client also installed on the Pi, then subscribes to that topic. When the message contents match the expected string, the passive buzzer attached to the Pi makes a sound and a red LED lights up. Addittionally, the Pi also sends an email after receiving a message from the ESP-12E. The amount of buttons is scalable.

![alt text](https://github.com/PyhaMarkus/mqtt-buzzer-project/blob/master/pictures/buzzerproject_bb.png "sketch")
