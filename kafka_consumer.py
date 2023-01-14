from kafka import KafkaConsumer

consumer = KafkaConsumer('my-topic', bootstrap_servers=['my-cluster-kafka-bootstrap:9092'], auto_offset_reset='earliest' )

i = 0
for message in consumer:
    message = message.value
    print(message)
    i = i+1

print(" "+i)
