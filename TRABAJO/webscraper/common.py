import yaml

__config = None
 
def config():
    global __config
    if not __config:
        with open('C:/Users/Usuario/Portafolio/TRABAJO/webscraper/config.yaml', mode='r') as f:
            __config = yaml.safe_load(f)    
    return __config

