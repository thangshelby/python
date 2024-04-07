import pymongo
from django.conf import settings
my_client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
dbname = my_client['facegram']
collection_name = dbname["accounts"]

accounts = collection_name.find({'userName':'Cr7'})


# collection_name.insert_many([medicine_1,medicine_2])

# med_details = collection_name.find({})


# for r in med_details:
# 	print(r["common_name"])

# update_data = collection_name.update_one({'medicine_id':'RR000123456'}, {'$set':{'common_name':'Paracetamol 500'}})

# count = collection_name.count(medicine_1)
# print(count)

# delete_data = collection_name.delete_one({'medicine_id':'RR000123456'})