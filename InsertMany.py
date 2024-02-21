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

    # inserting Many expense
    new_expense = [
        {
            "expense_logger": "Ada Lovelace",
            "description": "groceries",
            "amount": 175,
            "last_updated": datetime.now(timezone.utc),
        },
        {
            "expense_holder": "al-Khwarizmi",
            "description": "groceries",
            "amount": "Gas",
            "amount": 60,
            "last_updated": datetime.now(timezone.utc),
        },
    ]

    # Write an expression that inserts the 'new_account' document into the 'accounts' collection.
    result = collection.insert_many(new_expense)

    document_ids = result.inserted_ids
    print("# of documents inserted: " + str(len(document_ids)))
    print(f"_ids of inserted documents: {document_ids}")

    # Expression that inserts the 'new_expense' document into the 'expenses' collection.
    result = collection.insert_one(new_expense)

    document_id = result.inserted_id
    pprint.pprint(f"_id of inserted document: {document_id}")


except Exception as e:
    print(e)
finally:
    client.close()