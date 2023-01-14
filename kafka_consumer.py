import json
from time import sleep
from typing import Optional

from bs4 import BeautifulSoup
from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer('my-topic', bootstrap_servers=['my-cluster-kafka-bootstrap:9092'], auto_offset_reset='earliest')

i = 0
for message in consumer:
    message = message.value
    print(message)
    i = i+1

print(" "+i)
