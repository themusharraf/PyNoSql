import pymongo

# MongoDB-server'ga bog'lanish
client = pymongo.MongoClient("mongodb://localhost:27017/")

# MongoDB'dagi ma'lumotlar bazasini tanlash
db = client["mydatabase"]

# Ma'lumot qo'shish
collection = db["mycollection"]
data_to_insert = {"name": "John", "age": 30, "city": "New York"}
result = collection.insert_one(data_to_insert)
print(f"Inserted document ID: {result.inserted_id}")

# Ma'lumotni o'qish
document = collection.find_one({"name": "John"})
print(f"Read document: {document}")
