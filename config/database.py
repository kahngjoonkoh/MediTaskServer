from pymongo import MongoClient
import yaml

f = open('config/access.yaml', 'r')
access_info = yaml.safe_load(f)
uri = f"mongodb+srv://{access_info['username']}:{access_info['password']}@cluster0.0utopzd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
f.close()

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB")
except Exception as e:
    print(e)

db = client.MediTask
collection_name = db["Appointments"]
