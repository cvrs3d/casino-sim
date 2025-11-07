"""Event Publisher for Game Service"""
import json
import pika
from game_service.config import settings


class EventPublisher:
    """Publisher for game events to RabbitMQ"""
    
    def __init__(self):
        self.connection = None
        self.channel = None
    
    def connect(self):
        """Establish connection to RabbitMQ"""
        try:
            self.connection = pika.BlockingConnection(
                pika.URLParameters(settings.RABBITMQ_URL)
            )
            self.channel = self.connection.channel()
            self.channel.queue_declare(queue='game_events', durable=True)
        except Exception as e:
            print(f"Failed to connect to RabbitMQ: {e}")
    
    def publish_event(self, event_type: str, event_data: dict):
        """Publish an event to the message broker"""
        if not self.channel:
            self.connect()
        
        message = {
            "type": event_type,
            "data": event_data
        }
        
        try:
            self.channel.basic_publish(
                exchange='',
                routing_key='game_events',
                body=json.dumps(message),
                properties=pika.BasicProperties(
                    delivery_mode=2,  # make message persistent
                )
            )
        except Exception as e:
            print(f"Failed to publish event: {e}")
    
    def close(self):
        """Close the connection"""
        if self.connection:
            self.connection.close()
