import pymongo


client = pymongo.MongoClient("mongodb+srv://mdsirajulislam:Economics1@cluster0.jh2k1xl.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['myinfo']
collection = database["sudh"]



data= collection.find({"comapanyName" : "iNeuron" })
data=collection.find({"courseOffered": {"$gt": "E"}})
for i in data:
    print(i)