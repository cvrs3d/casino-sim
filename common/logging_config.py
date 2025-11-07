"""Logging Configuration for Services"""
import logging
import sys


def setup_logging(service_name: str, level=logging.INFO):
    """Setup logging configuration for a service"""
    
    # Create logger
    logger = logging.getLogger(service_name)
    logger.setLevel(level)
    
    # Create console handler
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    
    # Create formatter
    formatter = logging.Formatter(
        f'%(asctime)s - {service_name} - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    handler.setFormatter(formatter)
    
    # Add handler to logger
    logger.addHandler(handler)
    
    return logger
