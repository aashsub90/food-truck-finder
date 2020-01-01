import os
from configparser import SafeConfigParser

def get_config(section, key):
    """Get the value from the configuration file
    
    Arguments:
        section {string} -- Section name
        key {string} -- Key under the section provided
    
    Returns:
        value -- Value of the key specified
    """
    parser = SafeConfigParser()
    config_path = os.environ['CONFIG_PATH']
    parser.read(config_path+'config.ini')
    return parser.get(section, key)