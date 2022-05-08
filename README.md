pibooth-s3-upload
=================

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-red.svg)](https://www.python.org/downloads)
[![PyPi package](https://badge.fury.io/py/pibooth-s3-upload.svg)](https://pypi.org/project/pibooth-s3-upload)
[![PyPi downloads](https://img.shields.io/pypi/dm/pibooth-s3-upload?color=purple)](https://pypi.org/project/pibooth-s3-upload)

`pibooth-s3-upload` is a plugin for the [pibooth](https://pypi.org/project/pibooth) application.

Permits upload of pictures to an [AWS S3](https://aws.amazon.com/s3) bucket. Plugin requires an internet connection.

Install
-------

    $ pip3 install pibooth-s3-upload

Configuration
-------------

Below are the new configuration options available in the [pibooth](https://pypi.org/project/pibooth) configuration. **The keys and their default values are automatically added to your configuration after first** [pibooth](https://pypi.org/project/pibooth) **restart.**

``` {.ini}
[S3]

# AWS Access Key
aws_access_key =

# AWS Secret Key
aws_secret_key =

# AWS S3 bucket name for uploading files
s3_bucket_name =

# (Optional) Path prefix within AWS S3 bucket (ex: some-event-name/)
s3_prefix =

```

## Note

Edit the configuration by running the command `pibooth --config`.
