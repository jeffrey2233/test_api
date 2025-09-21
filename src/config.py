import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "..", "settings.ini"))

BASE_URL = config["DEFAULT"]["base_url"]
USERNAME = config["DEFAULT"]["username"]
PASSWORD = config["DEFAULT"]["password"]
