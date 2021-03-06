import json

def load_config():
    global CONFIG
    with open(config_file, 'r') as configfile:
        CONFIG = json.load( configfile )
    return CONFIG

def save_config():
    with open(config_file, 'w') as configfile:
        json.dump(CONFIG, configfile, indent=4,ensure_ascii=False)

config_file = 'my.json'

CONFIG = {}

load_config()

if not "coins" in CONFIG:
    CONFIG["coins"] = {}
if not "cals" in CONFIG:
    CONFIG["cals"] = {}