"""
Logger Utility
"""

import os
import logging.handlers
import time
import datetime

from Scripts.Utils import utility

class Logger(object):
    """
    Contain methods for Logger class
    """

    def __init__(self, config):
        """
        :param config
        """
        ts = time.time()
        service_name = utility.config['service_name']
        log_file_path = utility.config['path']['log_path'] + os.sep + service_name

        if not os.path.isdir(log_file_path):
            os.makedirs(log_file_path)


        log_file = log_file_path + os.sep + service_name
        self.log_obj = logging.getLogger(service_name)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', '%Y-%m-%d %H:%M:%S')
        logHandler = logging.handlers.TimedRotatingFileHandler(filename=str(log_file), backupCount=2, when='M', interval=600)
        logHandler.setLevel(utility.config['log_level'])
        logHandler.setFormatter(formatter)

        self.log_obj.addHandler(logHandler)
        self.log_obj.setLevel(utility.config['log_level'])
        self.log_obj.debug('Logger Initialized')



