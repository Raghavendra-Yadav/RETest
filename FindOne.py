from bson import ObjectId
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

    # inserting one account
    document_to_find = {
        "_id": ObjectId("65d64dba999922566cf03558")
    }

    # Write an expression that inserts the 'new_account' document into the 'accounts' collection.
    result = collection.insert_one(document_to_find)

    pprint.pprint(result)


except Exception as e:
    print(e)
finally:
    client.close()

