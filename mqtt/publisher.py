from paho.mqtt import publish

def main():
	size = 1030000
	largeString = "ten_bytess" * size
	msgs = [("mqtt/paho/test", largeString, 2 , False)]
			#{'topic': "mqtt/paho/test", 'payload': largeString, 'qos': 1}]
	       # {'topic': "mqtt/paho/test", 'payload': "world"},
                #{'topic': "mqtt/paho/private", 'payload': "secret"}]

	publish.multiple(msgs, hostname="localhost")

if __name__ == "__main__":
	main()
