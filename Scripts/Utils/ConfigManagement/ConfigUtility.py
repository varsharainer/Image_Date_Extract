
from configparser import ConfigParser
import logging

class ConfigUtility(object):
    logger = logging.getLogger('')
    parser = ConfigParser()


    def __init__(self, conf_file):
        try:
            self.parser.read(conf_file)
        except:
            self.logger.error("Exception occurred during configuration reading from File")

    def get_configuration(self, conf_section, conf_name):
        try:
            return self.parser.get(conf_section, conf_name)
        except:
            self.logger.error("Exception occurred during retrieving configuration")
            return " "


