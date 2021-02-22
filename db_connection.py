from pymodm import connect
import urllib 
import yaml
# from cryptography.fernet import Fernet
import base64
import sys
import os

# file containing mongo credentials
passFile = "/etc/secrets/mongodb/secrets.yml"

with open(passFile, 'r') as ymlfile:
    topic_list = yaml.load(ymlfile)

# read username, password and authentication key
key = topic_list["SECRETS"]["KEY"]
user = topic_list["SECRETS"]["USER"]
password = topic_list["SECRETS"]["PASS"]

userName = user
password = password
decodedPassword = urllib.parse.quote(password)
decodedUserName = urllib.parse.quote(userName)
MONGO_DB_NAME = topic_list['DB']['DB_NAME']
MONGO_DB_URL = topic_list['DB']['DB_URL']
MONGOD_URI = 'mongodb://'+decodedUserName+":"+decodedPassword+"@"+MONGO_DB_URL+'/'+MONGO_DB_NAME 

# connect to mongo
CLIENT = connect(MONGOD_URI)
print('\nINFO: connected to {}'.format(MONGO_DB_NAME))

