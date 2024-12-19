from kafka import KafkaProducer
import json
import time


KAFKA_BROKER = 'localhost:9092'
TOPIC_NAME = 'pizztopic'

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  
)

latitude = 31.520370
longitude = 74.358749

def generate_random_location():
    """Update latitude and longitude by adding 2."""
    global latitude, longitude
    latitude += 2
    longitude += 2
    return {"latitude": latitude, "longitude": longitude}

try:
    print("Producing updated location data...")
    while True:
        location = generate_random_location()
        producer.send(TOPIC_NAME, location)
        print(f"Sent: {location}")
        time.sleep(5) 
except KeyboardInterrupt:
    print("\nProducer stopped.")
finally:
    producer.close()
