"""Event Subscriber for Transaction Service"""
import json
import pika
from transaction_service.config import settings
from transaction_service.repository import TransactionRepository


class EventSubscriber:
    """Subscriber for events from RabbitMQ"""
    
    def __init__(self):
        self.connection = None
        self.channel = None
        self.repository = TransactionRepository()
    
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
            print(f"Received event: {event}")
            # Log the transaction
            # self.repository.create_transaction(event)
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
