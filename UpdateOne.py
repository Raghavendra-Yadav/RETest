from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
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

    # inserting one expense
    document_to_update = {"_id": ObjectId("65c3cbcc2430d3e6c9de2600")}

    # Update
    add_to_expense = {"$inc": {"expense": 100}}

    # Print original document
    pprint.pprint(collection.find_one(document_to_update))

    # Write an expression that adds to the target account balance by the specified amount.
    result = collection.update_one(document_to_update, add_to_expense)
    print("Documents updated: " + str(result.modified_count))

    # Print updated document
    pprint.pprint(collection.find_one(document_to_update))


except Exception as e:
    print(e)
finally:
    client.close()

