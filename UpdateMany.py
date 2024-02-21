from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

uri = "mongodb+srv://graghavendrayadav:Raghu@cluster0.gwjlwmk.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'bank' database
    db = client.expenseTracking

    # Get reference to 'accounts' collection
    collection = db.expenses

    # Filter
    select_accounts = {"description": "Rent"}

    # Print original document
    set_field = {"$set": {"balance": 250}}

    # Write an expression that adds to the target account balance by the specified amount.
    result = collection.update_many(select_accounts, set_field)

    # Print updated document
    print("Documents matched: " + str(result.matched_count))
    print("Documents updated: " + str(result.modified_count))
    pprint.pprint(collection.find_one(select_accounts))

except Exception as e:
    print(e)
finally:
    client.close()