# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()

class Var(object):
    API_ID = int(('8087060'))
    API_HASH = str(('ead24e1abe37e9a80b16ef0f468350b6'))
    BOT_TOKEN = str(('5723710010:AAH57aNzcpjebJU31_7vlrNEZPlBKSu3Ujo'))
    SLEEP_THRESHOLD = int(('SLEEP_THRESHOLD', '60'))
    WORKERS = int(('WORKERS', '3'))
    BIN_CHANNEL = int(('-1001161191495', None))     
    PORT = int(('PORT', 8080))
    BIND_ADRESS = str(('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    HAS_SSL = ('HAS_SSL', False)
    HAS_SSL = True if HAS_SSL.lower() == 'true' else False
    # OWNER_ID = int(getenv('OWNER_ID')) #TODO
    NO_PORT = ('NO_PORT', False)
    NO_PORT = True if NO_PORT.lower() == 'true' else False
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    if ON_HEROKU:
        URL = f"https://{FQDN}/"     
    else:
        URL = "http{}://{}{}/".format('s' if HAS_SSL else '', FQDN, '' if NO_PORT else ':'+ str(PORT))
