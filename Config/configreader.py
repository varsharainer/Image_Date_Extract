"""
Purpose: Read the configuration from YAML file
"""
import yaml
from Scripts.Utils import utility

def read_configuration(file_name):
    """

    :param file_name:
    :return: all the configuration constants
    """

    with open(file_name, 'r') as file_stream:
        print(file_name)
        try:
            return yaml.load(stream=file_stream, Loader=yaml.FullLoader)
        except yaml.YAMLError as err:
            utility.logger.error("Configuration File Read Error " + str(file_name) + "ERROR" + str(err))
