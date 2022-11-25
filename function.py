import logging

def app(event, context): 
    logging.basicConfig(level = logging.INFO)
    logger = logging.getLogger()
    logger.info("Python for the win!")
    
    return "Hello World"
