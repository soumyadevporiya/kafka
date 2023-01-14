from kafka import KafkaConsumer
from google.cloud import storage
consumer = KafkaConsumer('my-topic', bootstrap_servers=['my-cluster-kafka-bootstrap:9092'], auto_offset_reset='earliest' )

client = storage.Client()

bucket = client.bucket("soumyabucket")




i = 0

for message in consumer:
    message = message.value
    bucket.blob('first_dist00000.txt').upload_from_string(message, 'text/csv')
    i = i+1

#print(" "+i)
