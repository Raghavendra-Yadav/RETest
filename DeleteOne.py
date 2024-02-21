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

    # Filter by ObjectId
    document_to_delete = {"_id": ObjectId("65d661d1abf05836598556a0")}

    # Search for document before delete
    print("Searching for target document before delete: ")
    pprint.pprint(accounts_collection.find_one(document_to_delete))

    # Write an expression that deletes the target account.
    result = accounts_collection.delete_one(document_to_delete)

    # Search for document after delete
    print("Searching for target document after delete: ")
    pprint.pprint(accounts_collection.find_one(document_to_delete))

    print("Documents deleted: " + str(result.deleted_count))


except Exception as e:
    print(e)
finally:
    client.close()