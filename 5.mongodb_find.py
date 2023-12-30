from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["mydb"]
collection = db["customers"]

# Bir query olmaksızın find()
mydocs = collection.find()
print("All Documents")
for doc in mydocs:
    print(doc)

mydocs = collection.find()
print("All Documents")
for doc in mydocs:
    print(doc["name"])
    print(type(doc))

# Bir query ile find()
query = {"name": "Sandy"}
mydocs = collection.find(query)
for doc in mydocs:
    print(doc)

query = {"salary": 50000}
mydocs = collection.find(query)
for doc in mydocs:
    print(doc)

# Query ve projection beraber kullanımı
query = {"salary": 50000} #fitreleme
projection = {"_id": 0,"name": 1, "address": 1}  #field seçimi 0= id gelmesin 1= name address gelsin
mydocs = collection.find(query,projection)
for doc in mydocs:
    print(doc)

#salary haricindeki tüm bilgileri getir
query = {"salary": 50000}
projection = {"salary": 0}
mydocs = collection.find(query, projection)
for doc in mydocs:
    print(doc)

query = {"salary": 60000} #fitreleme
projection = {"name": 1, "address": 1}  #field seçimi 0= id gelmesin 1= name address gelsin
mydocs = collection.find(query,projection)
for doc in mydocs:
    print(doc)

#
mydocs = collection.find({},{"_id": 0, "name": 1, "salary": 1}) # query boş yani fitreleme yapmadım.hepsi demek
for doc in mydocs:
    print(doc)

mydocs = collection.find({},{"_id": 0, "ddress": 0})
for doc in mydocs:
    print(doc)

client.close()