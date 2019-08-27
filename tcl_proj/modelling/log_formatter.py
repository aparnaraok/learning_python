import logging

def get_log_formatter(message):
    '''Log formatter
    '''
    print(" ")
    logging.info("=" * 50)
    logging.info(message)
    logging.info("=" * 50)
    print(" ")