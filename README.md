# Live Location Sharing with Kafka and Django Channels

This project is a real-time location-sharing platform built using **Django**, **Django Channels**, and **Kafka-Python**. It allows users to share their live location along with their details, and other users can view this information in real-time.

## Features

- **Real-Time Location Sharing**: Users can share their current location in real-time.
- **Kafka Integration**: Efficient message streaming and handling with Kafka.
- **WebSocket Support**: Django Channels enables live updates through WebSocket connections.
- **User Details Sharing**: Share additional user information along with the location.
- **Scalable Architecture**: Kafka ensures high scalability and fault tolerance.

## Tech Stack

- **Backend**: Django, Django Channels
- **Message Broker**: Kafka (with Kafka-Python)
- **Frontend**: HTML, CSS, JavaScript (for WebSocket integration)
- **Database**: SQLite (can be replaced with PostgreSQL or any other database)

## Installation

### Prerequisites

- Python (3.8 or higher)
- Kafka (set up a local or remote Kafka broker)
- Virtual environment (optional but recommended)

### Steps

1. Clone the repository:
   ```bash
   https://github.com/Mani9047/Kafka-Django-Live-Location.git
   cd Kafka-Django-Live-Location
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # For Linux/Mac
   env\Scripts\activate   # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up Kafka:
   - Download and install Kafka from [Apache Kafka Downloads](https://kafka.apache.org/downloads).
   - Start Zookeeper and Kafka Broker:
     ```bash
     bin/zookeeper-server-start.sh config/zookeeper.properties
     bin/kafka-server-start.sh config/server.properties
     ```



5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Run the kafka producer:
   ```bash
   python kafkaproducer.py
   ```



7. Open the application in your browser at [http://localhost:8000](http://localhost:8000).

## Configuration

### Kafka Settings

Update the Kafka configurations in your Django settings file:
```python
KAFKA_BROKER_URL = 'localhost:9092'
KAFKA_TOPIC = 'your topic name'
```



## Usage

1. Log in with your credentials or create an account.
2. Share your location via the provided interface.
3. Other users connected to the platform will see your location and details in real-time.
q

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed explanation of your changes.


## Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Channels Documentation](https://channels.readthedocs.io/)
- [Kafka-Python Documentation](https://kafka-python.readthedocs.io/)
# Live Location Sharing with Kafka and Django Channels

This project is a real-time location-sharing platform built using **Django**, **Django Channels**, and **Kafka-Python**. It allows users to share their live location along with their details, and other users can view this information in real-time.

## Features

- **Real-Time Location Sharing**: Users can share their current location in real-time.
- **Kafka Integration**: Efficient message streaming and handling with Kafka.
- **WebSocket Support**: Django Channels enables live updates through WebSocket connections.
- **User Details Sharing**: Share additional user information along with the location.
- **Scalable Architecture**: Kafka ensures high scalability and fault tolerance.

## Tech Stack

- **Backend**: Django, Django Channels
- **Message Broker**: Kafka (with Kafka-Python)
- **Frontend**: HTML, CSS, JavaScript (for WebSocket integration)
- **Database**: SQLite (can be replaced with PostgreSQL or any other database)

## Installation

### Prerequisites

- Python (3.8 or higher)
- Kafka (set up a local or remote Kafka broker)
- Virtual environment (optional but recommended)

### Steps

1. Clone the repository:
   ```bash
   https://github.com/Mani9047/Kafka-Django-Live-Location.git
   cd Kafka-Django-Live-Location
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # For Linux/Mac
   env\Scripts\activate   # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up Kafka:
   - Download and install Kafka from [Apache Kafka Downloads](https://kafka.apache.org/downloads).
   - Start Zookeeper and Kafka Broker:
     ```bash
     bin/zookeeper-server-start.sh config/zookeeper.properties
     bin/kafka-server-start.sh config/server.properties
     ```



5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Run the kafka producer:
   ```bash
   python kafkaproducer.py
   ```



7. Open the application in your browser at [http://localhost:8000](http://localhost:8000).

## Configuration

### Kafka Settings

Update the Kafka configurations in your Django settings file:
```python
KAFKA_BROKER_URL = 'localhost:9092'
KAFKA_TOPIC = 'your topic name'
```



## Usage

1. Log in with your credentials or create an account.
2. Share your location via the provided interface.
3. Other users connected to the platform will see your location and details in real-time.
q

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed explanation of your changes.


## Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Channels Documentation](https://channels.readthedocs.io/)
- [Kafka-Python Documentation](https://kafka-python.readthedocs.io/)
