from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["mydb"]
collection = db["customers"]

# Bir döküman oluşturmak
mydict = {
    "name": "John",
    "address": "Highway 37",
    "salary": 50_000
}

# Kolleksiyona bir döküman eklemek
mydoc = collection.insert_one(mydict)
print(mydoc)
print(type(mydoc))
print(mydoc.inserted_id)

mydict2 = {
    "name": "Peter",
    "address": "Lowstreet 27",
    "salary": 60_000
}

mydoc = collection.insert_one(mydict2)
print(mydoc)
print(type(mydoc))
print(mydoc.inserted_id)


client.close()

