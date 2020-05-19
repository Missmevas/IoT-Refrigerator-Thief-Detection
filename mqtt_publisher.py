import paho.mqtt.client as mqtt

# This is the Publisher

client = mqtt.Client()
client.username_pw_set("dorota","dorota") # authentification
client.connect("ec2-3-10-103-212.eu-west-2.compute.amazonaws.com",8883,60) 
#connect with EC2 instance through encrypted port 8883

msg = input("Enter your message:")
client.publish("message", msg); # publish the message typed by the user

client.disconnect(); #disconnect from server