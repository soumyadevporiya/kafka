from kafka import KafkaConsumer
from google.cloud import storage
consumer = KafkaConsumer('my-topic', bootstrap_servers=['my-cluster-kafka-bootstrap:9092'], auto_offset_reset='earliest' )

#consumer = KafkaConsumer('admintome-test', bootstrap_servers=['kafka-service:9092'], auto_offset_reset='earliest' )

client = storage.Client()

bucket = client.bucket("soumyabucket")

i = 0

for message in consumer:
    i = i + 1
    message = message.value
    s = bucket.blob('first_dist00000.txt').download_as_string()
    s1 = bytes(s, 'utf-8')
    s2 = message
    s3 = bytes("Message No: ", 'utf-8')
    s4 = bytes(str(i), 'utf-8')
    s5 = s1 + s2 + s3 + s4
    bucket.blob('first_dist00000.txt').upload_from_string(s5, 'text/csv')

#print(" "+i)
