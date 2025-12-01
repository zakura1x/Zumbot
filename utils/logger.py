"""
logger.py - Logging utilities for the automation system
"""
import logging
import os
from datetime import datetime
import sys

def setup_logger(name, log_file="logs/automation.log", level=logging.INFO):
    """
    Setup logger with file and console output
    
    Args:
        name: Logger name
        log_file: Path to log file
        level: Logging level
    
    Returns:
        logging.Logger: Configured logger instance
    """
    # Create logs directory if it doesn't exist
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Avoid duplicate handlers
    if logger.handlers:
        return logger
    
    # File handler
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger

def log_execution_time(func):
    """
    Decorator to log function execution time
    """
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(func.__module__)
        start_time = datetime.now()
        
        try:
            result = func(*args, **kwargs)
            end_time = datetime.now()
            execution_time = (end_time - start_time).total_seconds()
            
            logger.info(
                f"Function '{func.__name__}' executed in "
                f"{execution_time:.2f} seconds"
            )
            return result
            
        except Exception as e:
            logger.error(
                f"Function '{func.__name__}' failed after "
                f"{(datetime.now() - start_time).total_seconds():.2f} seconds: {e}"
            )
            raise
    
    return wrapper

# Create a default logger for immediate use
default_logger = setup_logger("work_automation")