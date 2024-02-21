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
    documents_to_delete = {"description": "Rent"}

    # Search for sample document before delete
    print("Searching for sample target document before delete: ")
    pprint.pprint(accounts_collection.find_one(documents_to_delete))

    # Write an expression that deletes the target accounts.
    result = accounts_collection.delete_many(documents_to_delete)

    # Search for sample document after delete
    print("Searching for sample target document after delete: ")
    pprint.pprint(accounts_collection.find_one(documents_to_delete))

    print("Documents deleted: " + str(result.deleted_count))


except Exception as e:
    print(e)
finally:
    client.close()