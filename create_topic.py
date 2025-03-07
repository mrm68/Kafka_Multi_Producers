# create_topic.py

from confluent_kafka.admin import AdminClient, NewTopic
import os

# Kafka broker address
bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')

# Initialize AdminClient
admin = AdminClient({'bootstrap.servers': bootstrap_servers})


def topic_exists(topic_name):
    """Check if a topic already exists."""
    metadata = admin.list_topics(timeout=10)
    return topic_name in metadata.topics


def create_new_topic(base_name):
    """Create a new topic with an incremented index
       if the base name already exists."""
    index = 1
    while True:
        new_topic_name = f"{base_name}_{index}" if index > 1 else base_name
        if not topic_exists(new_topic_name):
            print(f"Creating topic: {new_topic_name}")
            topic = NewTopic(
                new_topic_name,
                num_partitions=3,
                replication_factor=1
            )
            futures = admin.create_topics([topic])
            for topic_name, future in futures.items():
                try:
                    future.result()  # Wait for the topic to be created
                    print(f"Topic '{topic_name}' created successfully!")
                except Exception as e:
                    print(f"Failed to create topic '{topic_name}': {e}")
            return new_topic_name
        index += 1


# Base topic name
base_topic_name = "my_topic"

# Create the topic (or a new one with an incremented index)
created_topic = create_new_topic(base_topic_name)
print(f"Using topic: {created_topic}")
