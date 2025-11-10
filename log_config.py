import logging

def config_log(module):
    logging.basicConfig(filename='Dir_status.log',level=10,format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    logger=logging.getLogger('{}'.format(module))
    return logger
