from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
from datetime import datetime, timezone
import pprint 


uri = "mongodb+srv://graghavendrayadav:Raghu@cluster0.gwjlwmk.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'expenseTracking' database
    db = client.expenseTracking

    # Get reference to 'expenses' collection
    collection = db.expenses

    ids_to_find = [
        ObjectId("65d66f3f3b8face7c98ec187"),
        ObjectId("65d66f093720c762a1b7eb68"),
        ObjectId("65d66a73f8baaf9a74cc5087"),
    ]

    # Find documents with the specified IDs
    found_documents = collection.find({"_id": {"$in": ids_to_find}})

    # Check if any documents were found
    if found_documents:
        for document in found_documents:
            pprint.pprint(document)
            print("---")
    else:
        print("No documents found with the specified IDs.")


except Exception as e:
    print(e)
finally:
    client.close()

