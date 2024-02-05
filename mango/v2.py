import pymongo
import time

# MongoDB-server'ga bog'lanish
client = pymongo.MongoClient("mongodb://localhost:27017/")

# MongoDB'dagi ma'lumotlar bazasini tanlash
db = client["mydatabase"]

# Ma'lumot qo'shish va TTL so'zini belgilash
collection = db["mycollection"]
data_to_insert = {"name": "John", "age": 30, "city": "New York", "expireAt": int(time.time()) + 3600}
result = collection.insert_one(data_to_insert)
print(f"Inserted document ID: {result.inserted_id}")

# Ma'lumotni o'qish
document = collection.find_one({"name": "John"})
print(f"Read document: {document}")

"""
Agar MongoDB-da ma'lumotlarni belgilangan vaqt o'tgandan so'ng avtomatik ravishda o'chirishni istasangiz,
 MongoDB tizimida TTL (Time-To-Live) so'zi yordamida ma'lumotlarni o'chirish mumkin.
Bu so'z orqali ma'lumotlarga bir muddat tanlanadi va ushbu muddat o'tib ketganda MongoDB avtomatik ravishda ma'lumotni o'chiradi.
Quyidagi misol kodda, MongoDB tizimida TTL so'zini ishlatish orqali ma'lumotni bir soat (3600 sekund) muddatida saqlab turamiz:"""

"""
Ushbu kod misolida, expireAt nomli yangi maydon orqali ma'lumotga TTL muddatini (UNIX vaqti formatida) qo'shilyapti. 
MongoDB avtomatik ravishda ushbu muddatdan so'ng ma'lumotni o'chiradi.
Bu usul orqali, avtomatik ravishda MongoDB tizimida ma'lumotlarni o'chirishni amalga oshirishingiz mumkin."""
