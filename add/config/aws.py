import os
import logging

USER_DOMAIN = os.environ.get('ADD_DOMAIN')
ZONE_ID = os.environ.get('ADD_ZONE_ID')

NEW_TTL_S = int(os.environ.get('ADD_NEW_TTL', '60'))
AWS_IS_DEBUG = bool(int(os.environ.get('ADD_AWS_DEBUG', '0')))
