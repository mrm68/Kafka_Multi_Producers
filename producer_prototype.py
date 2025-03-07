# producer_prototype.py

from abc import ABC, abstractmethod
from confluent_kafka import Producer
from threading import Thread
import time
import os


class IProducer_Prototype(ABC):
    @abstractmethod
    def produce_message(self, topic, message):
        pass

    @abstractmethod
    def delivery_report(self, err, msg):
        pass

    @abstractmethod
    def clone_and_start(self, producers):
        pass


class Producer_Prototype(IProducer_Prototype):
    def __init__(self, bootstrap_servers, producers):
        self.bootstrap_servers = bootstrap_servers
        self.producers = producers
        self.thread = Thread(target=self.start_producing)
        self.thread.start()

    def delivery_report(self, err, msg):
        report_actions = {
            True: lambda: print(f'Failed: {err}'),
            False: lambda: print(f'Delivered to {msg.topic()}"\
                                 f" [Partition {msg.partition()}]')
        }
        report_actions[err is not None]()

    def produce_message(self, topic, message):
        producer = Producer({'bootstrap.servers': self.bootstrap_servers})
        producer.produce(topic, value=message, callback=self.delivery_report)
        producer.poll(0)
        # Ensure all messages are delivered before terminating
        producer.flush()

    def start_producing(self):
        while True:
            message = f"Message @{time.strftime('%X')} from {id(self)}"
            self.produce_message('my_topic', message)
            time.sleep(1)
            if int(time.time()) % 5 == 0:
                self.clone_and_start(self.producers)

    def clone_and_start(self, producers):
        new_producer = Producer_Prototype(self.bootstrap_servers, producers)
        producers.append(new_producer)
        print(f"* Cloned a producer. Total producers: {len(producers)}")


def main():
    bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
    producers = []
    kafka_producer = Producer_Prototype(bootstrap_servers, producers)
    producers.append(kafka_producer)


if __name__ == "__main__":
    main()
