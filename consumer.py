# consumer.py

from confluent_kafka import Consumer
import time
import os

bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')

consumer = Consumer({
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['my_topic'])

while True:
    msg = consumer.poll(1.0)
    if msg:
        print(
            f"Received: {msg.value().decode()} [Partition {msg.partition()}]")
    time.sleep(1)
