import requests
import logging

logging.getLogger('botocore').setLevel(logging.ERROR)
import boto3

import add.config.aws
import add.config.general

_LOGGER = logging.getLogger(__name__)

def update_arecord(domain_name, zone_id):
    _LOGGER.debug("Updating DNS for domain [%s].", domain_name)

    _LOGGER.debug("Fetching current IP.")

    ip = requests.get(add.config.general.IP_FIND_URL).text.rstrip()
    _LOGGER.info("Updating hostname to [{}]".format(ip))

    route53 = boto3.client('route53')

    response = \
        route53.change_resource_record_sets(
            HostedZoneId=zone_id,
            ChangeBatch={
                "Comment": "Automatic DNS update",
                "Changes": [
                    {
                        "Action": "UPSERT",
                        "ResourceRecordSet": {
                            "Name": domain_name,
                            "Type": "A",
                            "TTL": add.config.aws.NEW_TTL_S,
                            "ResourceRecords": [
                                {
                                    "Value": ip
                                },
                            ],
                        }
                    },
                ]
            }
        )


