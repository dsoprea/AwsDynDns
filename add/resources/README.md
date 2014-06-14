Overview
--------

A low-cost, dynamic-DNS client using Amazon's Route53 (currently $.50/zone).

Based on code from [How and why I'm not running my own DNS](http://www.petekeen.net/how-and-why-im-not-running-my-own-dns).


Installation
------------

In Ubuntu:

```
$ sudo pip install awsdd
```


Prerequisites
-------------

You must already have an A-record for your domain name in the Route53 zone. In 
order to be able to remove the record, prior to creating a new one (if the IP 
has changed), we need to know the TTL value of the current record, which is 
used by the *boto* library to identify the current record.

If you see the following error, it might mean that the TTL disagreed from our default:

```
boto.route53.exception.DNSServerError: DNSServerError: 400 Bad Request
<?xml version="1.0"?>
<ErrorResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/"><Error><Type>Sender</Type><Code>InvalidChangeBatch</Code><Message>Tried to delete resource record set [name='dustinhome.us.', type='A'] but the values provided do not match the current values</Message></Error><RequestId>be44faea-f41c-11e3-a846-5921f19aa715</RequestId></ErrorResponse>
```

In this case, try looking-up your current TTL value in the Route53 console, and setting it into the ADD_OLD_TTL environment variable.


Settings
--------

*awsdd* needs your AWS API credentials, the zone-ID, and the domain name that 
you're updating. All of these things can be defined as environment variables 
or passed as command-line parameters.

The command-line parameters can be found via command-line help. The supported 
environment variables are these, and shouldn't need an explanation:

- USER_DOMAIN
- ZONE_ID
- ACCESS_KEY_ID
- SECRET_ACCESS_KEY


Usage
-----

```
$ ADD_ACCESS_KEY_ID=XXXXXXXXXX ADD_SECRET_ACCESS_KEY=YYYYYYYYYY add_update -d <domain name> -z <zone ID>
```


Debuging
--------

By setting the DEBUG environment variable to "1", you'll get some more verbosity:

```
2014-06-14 19:46:47,057 - add.aws - DEBUG - Updating DNS for domain [ddd.eee].
2014-06-14 19:46:47,057 - add.aws - DEBUG - Fetching current IP.
2014-06-14 19:46:47,077 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTP connection (1): wtfismyip.com
2014-06-14 19:46:47,281 - requests.packages.urllib3.connectionpool - DEBUG - "GET /text HTTP/1.1" 200 13
2014-06-14 19:46:47,281 - add.aws - DEBUG - Current IP: [49.139.31.75]
2014-06-14 19:46:47,581 - add.aws - DEBUG - Current DNS value: [1.2.3.4]
2014-06-14 19:46:47,716 - add.aws - INFO - IP update complete.
```
