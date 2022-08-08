import os
import requests
import boto3
import helper


def lambda_handler(event, context):
    helper.HelperFunction.execute()
    return 0
    