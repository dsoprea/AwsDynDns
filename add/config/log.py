import logging
import os

import add.config.aws
import add.config.general

logger = logging.getLogger()

if add.config.general.IS_DEBUG is True:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

ch = logging.StreamHandler()

FMT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(FMT)
ch.setFormatter(formatter)
logger.addHandler(ch)

_AWS_LOGLEVEL = logging.DEBUG if add.config.aws.AWS_IS_DEBUG else logging.WARNING
logging.getLogger('boto').setLevel(_AWS_LOGLEVEL)

_R_LOGLEVEL = logging.DEBUG if add.config.general.IS_DEBUG else logging.WARNING
logging.getLogger('requests.packages.urllib3.connectionpool').\
    setLevel(_R_LOGLEVEL)
