# producer.py

import time
import os
from confluent_kafka import Producer


class KafkaProducer:
    def __init__(self, bootstrap_servers):
        self.producer = Producer({'bootstrap.servers': bootstrap_servers})

    def delivery_report(self, err, msg):
        if err:
            print(f'Failed: {err}')
        else:
            print(f'Delivered to {msg.topic()} [Partition {msg.partition()}]')

    def produce_message(self, topic, message):
        self.producer.produce(topic, value=message,
                              callback=self.delivery_report)
        self.producer.poll(0)


def main():
    bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
    kafka_producer = KafkaProducer(bootstrap_servers)

    while True:
        message = f"Message @ {time.strftime('%X')}"
        kafka_producer.produce_message('my_topic', message)
        time.sleep(1)


if __name__ == "__main__":
    main()
