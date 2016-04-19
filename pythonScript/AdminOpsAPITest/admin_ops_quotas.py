# -*- coding: utf-8 -*-
from awsauth import S3Auth
import requests

host = "192.168.122.100"
ep = "admin"
s3uid = ""
access = ""
secret = ""

# get user quota info
url = "http://%s/%s/user?quota&uid=%s&quota-type=user"%(host, ep, s3uid)
response = requests.get(url,auth=S3Auth(access, secret))
print 'get user quota info'
print 'status code: ', response.status_code
print 'content: ', response.content
