import os
import logging

USER_DOMAIN = os.environ.get('ADD_DOMAIN')
ZONE_ID = os.environ.get('ADD_ZONE_ID')
ACCESS_KEY_ID = os.environ.get('ADD_ACCESS_KEY_ID')
SECRET_ACCESS_KEY = os.environ.get('ADD_SECRET_ACCESS_KEY')

OLD_TTL = int(os.environ.get('ADD_OLD_TTL', '60'))
NEW_TTL = int(os.environ.get('ADD_NEW_TTL', '60'))
AWS_IS_DEBUG = bool(int(os.environ.get('ADD_AWS_DEBUG', '0')))
