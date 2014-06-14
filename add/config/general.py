import os

IP_FIND_URL = "http://wtfismyip.com/text"
IS_DEBUG = bool(int(os.environ.get('DEBUG', '0')))
