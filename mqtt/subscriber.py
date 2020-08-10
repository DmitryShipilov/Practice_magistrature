import paho.mqtt.client as client

def on_connect(client, userdata, flags, rc):
	print("Conneted with resul code: %s " % rc)
	client.subscribe("mqtt/paho/test")
	client.subscribe("mqtt/paho/private")

def on_message(client, userdata, msg):
	print("new message!")
	print("%s: %s \n" % (msg.topic, msg.payload))

def main():
	subscriber = client.Client()
	subscriber.on_connect = on_connect
	subscriber.on_message = on_message

	subscriber.connect("localhost")
	subscriber.loop_forever()

if __name__ == "__main__":
	main()
