# -*- coding: utf-8 -*- 
import paho.mqtt.client as mqtt
 
def on_connect(client, userdata, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("isyjp/msg1st")
 
def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.tls_set("/etc/ssl/certs/ca-certificates.crt")
 
client.username_pw_set("eylfzska", "qLgkVNLRbpD6")
client.connect("m12.cloudmqtt.com", 25313)
 
client.loop_forever()