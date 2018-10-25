#Decorator as a logging class:

# import logging
#
# class LogDecorator:
#     def __init__(self, f):
#
#          logging.debug("A logging is about to start")
#          f()
#     def __call__(self):
#         logging.debug("Stop logging")
#
# @LogDecorator
#
# def myfunct():
#     logging.info("The decorator function called")
#
# myfunct()

# output
# A logging is about to start
# The decorator function called
# Done

import logging

LOG_FILENAME = 'logging_example.out'
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.ERROR,
)

logging.info('This message should go to the log file') #This place is higher
#info is greater so nothing gets printed
#critical is less than error so it gets printed.
with open(LOG_FILENAME, 'rt') as f:
    body = f.read()

print('FILE:')
print(body)


#Print will happen based on level / hierarchy irrespective of the level specified

# FILE:
# DEBUG:root:This message should go to the log file
# INFO:root:This message should go to the log file
# CRITICAL:root:This message should go to the log file


