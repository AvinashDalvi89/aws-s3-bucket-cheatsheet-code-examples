import json
import boto3
import datetime
import time
from time import mktime


client = boto3.client('s3')
response = client.list_objects(Bucket='angularbuildbucket')
print(response)
today_date_time = datetime.datetime.now().replace(tzinfo=None)
print(today_date_time)
    
for file in response.get("Contents"):
    file_name =file.get("Key")
    modified_time = file.get("LastModified").replace(tzinfo=None)
         
    difference_days_delta = today_date_time - modified_time
    difference_days = difference_days_delta.days
    print("difference_days---", difference_days)
    if difference_days > 60:
        print("file more than 60 days older : - ", file_name)
