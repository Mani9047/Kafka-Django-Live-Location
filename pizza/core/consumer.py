import asyncio
import json
from aiokafka import AIOKafkaConsumer
from channels.generic.websocket import AsyncWebsocketConsumer

class KafkaConsumerWebSocket(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # Start Kafka consumer in the background
        self.consumer_task = asyncio.create_task(self.consume_kafka())

    async def disconnect(self, close_code):
        # Cancel the Kafka consumer task on disconnect
        if self.consumer_task:
            self.consumer_task.cancel()
            try:
                await self.consumer_task  # Ensure the task is closed properly
            except asyncio.CancelledError:
                pass

    async def consume_kafka(self):
        KAFKA_BROKER = 'localhost:9092'
        TOPIC_NAME = 'pizztopic'

        #  Kafka consumer
        consumer = AIOKafkaConsumer(
            TOPIC_NAME,
            bootstrap_servers=KAFKA_BROKER,
            value_deserializer=lambda v: json.loads(v.decode('utf-8'))
        )

        try:
            # Start the consumer
            await consumer.start()
            print("Kafka consumer started...")

            # Kafka messages
            async for message in consumer:
                location_data = message.value

                # Send location data to the WebSocket
                try:
                    await self.send(json.dumps(location_data))
                except Exception as e:
                    print(f"Error sending data to WebSocket: {e}")

        except Exception as e:
            print(f"Kafka consumer error: {e}")
        finally:
            await consumer.stop()
            print("Kafka consumer stopped.")
