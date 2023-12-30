# pip install pymongo Terminalde çalıştır

from pymongo import MongoClient

# MongoDB sunucusuna bağlan
client = MongoClient("mongodb://localhost:27017")  #mongo arayüzünden localhost yanındaki 3 noktaya tıkladık copy connection string dedik ve tırnak içine yapıştırdık

# Bir veritabanı oluşturmak ya da mevcut veritabanına erişmek
db = client["mydb"]  #client istemci. köşeli parantez içine mydb yazdık. mydb varsa bağlan yoksa oluştur demek

# Bir koleksiyon oluşturmak veya mevcut kolleksiyona erişmek
collection = db["customers"]

# Sistemdeki veri tabanlarının listesi
print(client.list_database_names())
# Veritabanındaki kolleksiyonların listesi
print(db.list_collection_names())

client.close()
