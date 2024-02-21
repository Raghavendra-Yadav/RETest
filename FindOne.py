from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint
from InsertOne import uri

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'bank' database
    db = client.expenseTracking

    # Get reference to 'accounts' collection
    accounts_collection = db.expenses

    document_to_find = {
        "_id": ObjectId("65d66f093720c762a1b7eb68")  # Example ID, replace with actual
    }

    # Find the document with the specified ID
    found_document = accounts_collection.find_one(document_to_find)

    if found_document:
        pprint.pprint(found_document)
        print("Document found!")
    else:
        print("Document not found with the specified ID.")


except Exception as e:
    print(e)
finally:
    client.close()