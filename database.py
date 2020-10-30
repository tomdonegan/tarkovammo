import pymongo

connection_url = 'mongodb+srv://tarkov-ammo:escapefromtarkov@cluster0.jxq25.mongodb.net/escape_from_tarkov?retryWrites=true&w=majority'

client = pymongo.MongoClient(connection_url)

db = client.escape_from_tarkov

col = db.tarkov_ammo

x = col.find_one()
titles_list = list(x.keys())[1:]
ammo_data_list = []


def ammo_by_size(ammo_size):
    for i in col.find({'Ammo Size': ammo_size}):
        ammo_data_list.append(list(i.values())[2:])