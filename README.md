# Kafka Ecosystem with Docker Compose & Python Examples

A local development setup for Apache Kafka with management UIs and Python client examples. This project demonstrates a Kafka ecosystem using Docker Compose, including producers, consumers, and multiple Kafka web interfaces.

## Features

- **Single-node Kafka cluster** with Zookeeper  
- **Kafka Web UIs**:  
  - AKHQ (http://localhost:8081)  
  - Kouncil (http://localhost:8082)  
  - Provectus Kafka UI (http://localhost:8083)  
- **Python Examples**:  
  - Topic creation with auto-incrementing names  
  - Basic producer/consumer implementation  
  - Prototype pattern producer with auto-cloning  
- **Dockerized Environment** with pre-configured services  

## Prerequisites

- Docker & Docker Compose installed  
- Basic understanding of Kafka concepts  

## Getting Started

1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/yourusername/kafka-ecosystem-demo.git  
   cd kafka-ecosystem-demo  
   ```  

2. **Start the stack**:  
   ```bash  
   docker-compose up -d  
   ```  

3. **Access services**:  
   - Kafka Broker: `localhost:9092`  
   - AKHQ UI: http://localhost:8081  
   - Kouncil UI: http://localhost:8082  
   - Provectus Kafka UI: http://localhost:8083  

## Python Scripts Overview

### `create_topic.py`  
- Creates `my_topic` with 3 partitions  
- Auto-increments topic name if exists (e.g., `my_topic_2`)  
- Runs automatically in Docker via `create-topic` service  

### `producer_prototype.py`  
- Demonstrates Prototype pattern  
- Creates new producer clone every 5 seconds  
- Sends messages continuously to `my_topic`  

### `producer.py`  
- Simple producer sending messages every second  
- Includes delivery reports  

### `consumer.py`  
- Consumer listening to `my_topic`  
- Prints messages with partition information  

## UI Tools Features

1. **AKHQ**:  
   - Topic management  
   - Message browsing  
   - Consumer group monitoring  

2. **Kouncil**:  
   - Real-time message viewing  
   - Schema registry integration  
   - Topic configuration inspection  

3. **Provectus Kafka UI**:  
   - Cluster health monitoring  
   - Message search & filtering  
   - Consumer lag analysis  

## Customization

1. **Environment Variables**:  
   ```yaml  
   environment:  
     KAFKA_BOOTSTRAP_SERVERS: kafka:9092  
     KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092  
   ```  

2. **Topic Configuration**:  
   Modify in `create_topic.py`:  
   ```python  
   NewTopic(new_topic_name, num_partitions=3, replication_factor=1)  
   ```  

3. **Producer Settings**:  
   Adjust message interval in `producer*.py`:  
   ```python  
   time.sleep(1)  # Change sleep duration  
   ```  

## Troubleshooting

1. **Port Conflicts**:  
   - Check for existing services on ports 2181, 9092, 8081-8083  

2. **Docker Logs**:  
   ```bash  
   docker-compose logs -f [service_name]  
   ```  

3. **Topic Creation Issues**:  
   - Wait 30-60 seconds after Kafka starts before creating topics  

## License

MIT License - see [LICENSE](LICENSE) file for details  

## Contributing

1. Fork the repository  
2. Create feature branch  
3. Submit a Pull Request  

