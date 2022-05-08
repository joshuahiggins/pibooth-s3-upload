# -*- coding: utf-8 -*-

"""pibooth plugin for uploading pictures to an S3 bucket"""

import os
import boto3

try:
    from botocore.exceptions import ClientError
except ImportError:
    InstalledAppFlow = None
    pass

import pibooth
from pibooth.utils import LOGGER


__version__ = "1.0.0"

SECTION = 'S3'


@pibooth.hookimpl
def pibooth_configure(cfg):
    """Declare the new configuration options"""
    cfg.add_option(SECTION, 'aws_access_key', '', "AWS Access Key")
    cfg.add_option(SECTION, 'aws_secret_key', '', "AWS Secret Key")
    cfg.add_option(SECTION, 's3_bucket_name', '',
        "AWS S3 bucket name for uploading files",
        "Bucket name", '')
    cfg.add_option(SECTION, 's3_prefix', '',
        "(Optional) Path prefix within AWS S3 bucket (ex: 'some-event-name/')",
        "Path prefix (optional)", '')


@pibooth.hookimpl
def pibooth_startup(app, cfg):
    """Verify AWS credentials"""
    aws_access_key = cfg.get(SECTION, 'aws_access_key')
    aws_secret_key = cfg.get(SECTION, 'aws_secret_key')
    s3_bucket_name = cfg.get(SECTION, 's3_bucket_name')

    if not aws_access_key:
        LOGGER.error("AWS Access Key not defined in ["+SECTION+"][aws_access_key], uploading deactivated")
    elif not aws_secret_key:
        LOGGER.error("AWS Secret Key not defined in ["+SECTION+"][aws_secret_key], uploading deactivated")
    elif not s3_bucket_name:
        LOGGER.error("S3 Bucket Name not defined in ["+SECTION+"][s3_bucket_name], uploading deactivated")
    else:
        LOGGER.info("Initializing S3 client")
        app.s3_client = boto3.client(
          's3',
          aws_access_key_id=aws_access_key,
          aws_secret_access_key=aws_secret_key
        )


@pibooth.hookimpl
def state_processing_exit(app, cfg):
    """Upload picture to S3 bucket"""
    if hasattr(app, 's3_client'):
        s3_prefix = cfg.get(SECTION, 's3_prefix').strip('"')
        s3_bucket_name = cfg.get(SECTION, 's3_bucket_name').strip('"')
        upload_path = s3_prefix + os.path.basename(app.previous_picture_file)

        try:
            response = app.s3_client.upload_file(app.previous_picture_file, s3_bucket_name, upload_path)
            LOGGER.info("File uploaded to S3: " + upload_path)
        except ClientError as e:
            LOGGER.error(e)
