import datetime
import pandas as pd
from pymongo import MongoClient


def get_database():
    CONNECTION_STRING ="mongodb+srv://rohanthakur:NXEaPckQIKO39QaT@testcluster.4aecceu.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    mydb=client.Teachable                      #Database_name
    mycoll=mydb.master_table
    x = mycoll.find_one()
    print(type(x))
    print(x)
    
    '''Find items using query in collection'''
    # myquery = { "area": { "$regex": "^n" } }
    # mydoc = mycoll.find(myquery).limit(8)
    # for x in mydoc:
    #     print(x)

    '''Sorting 
    sort("name", 1) #ascending
    sort("name", -1) #descending'''
    # mydoc = mycoll.find().sort("titl e")
    # for x in mydoc:
    #     print(x)

    '''Display Collection in df'''
    # df = pd.DataFrame(list(mycoll.find()))
    # print(df)

    '''Adding Entries'''
    mydict = {'title': 'Fun with Place Value in Hindi', 'subject': 'Mathematics', 'area': 'numbers', 'video_link': 'https://youtu.be/mULStcte_ag', 
    'video_thumbnail': 'contents','isnotes':True,'note_link':'https://drive.google.com/file/d/1hhegYDe8mx8upJCOgAa8pJBm9CrtgN5K/view?usp=sharing',
    'entry_date':datetime.datetime.now()}

    mycoll.insert_one(mydict) 

    '''Deleting Entries'''
    # myquery = { "name": "rohan" }
    # mycoll.delete_one(myquery)

    # query = { "address": {"$regex": "^S"} }
    # mycoll.delete_many(query)

    '''Random pick'''
    # print(mycoll.find_one())

    """Find item in collection"""
    # for x in mycoll.find({},{ "title": 'Fun with Place Value in Hindi' }):
    #     print(x)

    # x = mycoll.find_one({ "title": "Fun with Place Value in Hindi"})
    # print(x)


    """Update items in collection"""
    # myquery = { "address": "Valley 345" }
    # newvalues = { "$set": { "address": "Canyon 123" } }
    # mycoll.update_one(myquery, newvalues)

    # myquery = { "address": { "$regex": "^S" } }
    # newvalues = { "$set": { "name": "Minnie" } }
    # x = mycoll.update_many(myquery, newvalues)
    
    return mydb.client


if __name__ == "__main__":
    # planet_name = input("Enter Planet Name: ")   
    dbname = get_database()