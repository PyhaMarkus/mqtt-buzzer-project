#!/usr/bin/python
#-*- coding: utf-8 -*-

# Import libraries
import time
import sys
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import smtplib

# Define GPIO pins for the LED and the buzzer
ledPin = 23
buzzerPin = 18 #GPIO18 is PWM capable

# Initialize GPIO pins as output
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(buzzerPin, GPIO.OUT)

# When a connection to MQTT-broker is successful
def on_connect(client, userdata, flags, rc):
	print("Connected with result code"+str(rc))
	client.subscribe("support/#") # Subscribe to topic

# When a message is received
def on_message(client, userdata, msg):

	#global sender_ID
	if msg.payload == "buttonState is HIGH - Location1":
		sender_ID = "location1"
		print("Location1: The button has been pressed!\nSounding the alarm...") 
		GPIO.output(ledPin,GPIO.HIGH) # Turn on the LED
		buzzer = GPIO.PWM(buzzerPin, 440) # Turn on the buzzer
		buzzer.start(10) # Buzzer volume 10%
		time.sleep(1.0)
		buzzer.stop() # Turn off the buzzer
		time.sleep(4.0)
		GPIO.output(ledPin,GPIO.LOW) # Turn off the LED

	elif msg.payload == "buttonState is HIGH - Location2":
		sender_ID = "location2"
		print("Location2: The button has been pressed!\nSounding the alarm...")
		GPIO.output(ledPin,GPIO.HIGH) # Turn on the LED
		buzzer = GPIO.PWM(buzzerPin, 440) # Turn on the buzzer
		buzzer.start(10) # Buzzer volume 10%
		time.sleep(1.0)
		buzzer.stop() # Turn off the buzzer
		time.sleep(4.0)
		GPIO.output(ledPin,GPIO.LOW) # Turn off the LED

        # GMAIL message contents
        TO = 'example.email@gmail.com'
        SUBJECT = 'Button Alert!'
        TEXT = "The button has been pressed in: %s!" % sender_ID 

        # GMAIL user setup
        gmail_sender = 'sender.email@gmail.com'
        gmail_passwd = 'sender_gmail_password'

        # GMAIL authentication
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(gmail_sender, gmail_passwd)

        # GMAIL message structure
        BODY = "\r\n".join([
                "TO: %s" % TO,
                "FROM: %s" % gmail_sender ,
                "Subject: %s" % SUBJECT ,
                "",
                TEXT
                ])

	# Send the mail
	server.sendmail(gmail_sender, [TO], BODY)

# MQTT information
client = mqtt.Client()
client.connect("127.0.0.1",1883,60)
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()

