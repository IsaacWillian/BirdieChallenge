import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dados"]
mycol = mydb["ofertas"]
print(mycol)
for i in mycol.find():
    print(i)


