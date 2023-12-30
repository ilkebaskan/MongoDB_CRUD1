from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["mydb"]
collection = db["customers"]

# Bir Query olmaksızın  find_one
result = collection.find_one()  # ilk dökümanı getirdi
print(result)

print(f"Name: {result['name']}\nAddress: {result['address']}\nSalary: {result['salary']}")


# Bir query ile find_one
query = {"name": "Peter"}
result = collection.find_one(query)
print(f"Name: {result['name']}\nAddress: {result['address']}\nSalary: {result['salary']}")

client.close()



