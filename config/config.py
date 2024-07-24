from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb://localhost:27017"

# create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.Blogging
blogs_collection = db['blogs']

# send a ping to confirm a successfull connection
try:
    client.admin.command('ping')
except Exception as e:
    print(e)