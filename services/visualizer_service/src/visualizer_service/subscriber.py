"""Event Subscriber for Visualizer Service"""
import json
import pika
from visualizer_service.config import settings


class EventSubscriber:
    """Subscriber for events from RabbitMQ"""
    
    def __init__(self):
        self.connection = None
        self.channel = None
        self.events = []
    
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
    
    def callback(self, ch, method, properties, body):
        """Handle received events"""
        try:
            event = json.loads(body)
            self.events.append(event)
            print(f"Received event: {event}")
            ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as e:
            print(f"Error processing event: {e}")
    
    def start_consuming(self):
        """Start consuming events"""
        if not self.channel:
            self.connect()
        
        self.channel.basic_consume(
            queue='game_events',
            on_message_callback=self.callback
        )
        
        print("Started consuming events...")
        self.channel.start_consuming()
    
    def close(self):
        """Close the connection"""
        if self.connection:
            self.connection.close()
