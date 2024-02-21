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
    new_expense = {
        "expense_logger": "Raghavendra Yadav",
        "description": "Rent",
        "amount": 375,
        "last_updated": datetime.now(timezone.utc),
    }

    # Expression that inserts the 'new_expense' document into the 'expenses' collection.
    result = collection.insert_one(new_expense)

    document_id = result.inserted_id
    pprint.pprint(f"_id of inserted document: {document_id}")


except Exception as e:
    print(e)
finally:
    client.close()

