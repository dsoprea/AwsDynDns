import requests
import logging

import boto.route53.connection
import boto.route53.record

import add.config.aws
import add.config.general

_logger = logging.getLogger(__name__)

def update_arecord(domain_name, zone_id, access_key, secret_key):
    _logger.debug("Updating DNS for domain [%s].", domain_name)

    _logger.debug("Fetching current IP.")

    ip = requests.get(add.config.general.IP_FIND_URL).text.rstrip()
    _logger.debug("Current IP: [%s]", ip)

    conn = boto.route53.connection.Route53Connection(
            access_key, 
            secret_key)

    record_name = domain_name + '.'

    response = conn.get_all_rrsets(zone_id, 'A', record_name, maxitems=1)

    if response:
        old_ip = response[0].resource_records[0]
        _logger.debug("Current DNS value: [%s]", old_ip)

        if ip == old_ip:
            _logger.info("IP update not necessary.")
            return

        changes = boto.route53.record.ResourceRecordSets(conn, zone_id)

        delete_record = changes.add_change('DELETE', record_name, 'A', add.config.aws.OLD_TTL)
        delete_record.add_value(old_ip)

        changes.commit()
    else:
        old_ip = None

    changes = boto.route53.record.ResourceRecordSets(conn, zone_id)

    create_record = changes.add_change('CREATE', record_name, 'A', add.config.aws.NEW_TTL)
    create_record.add_value(ip)

    changes.commit()

    _logger.info("IP update complete.")
