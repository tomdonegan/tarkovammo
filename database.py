import pymongo

connection_url = 'DATABASE KEY REQUIRED'

client = pymongo.MongoClient(connection_url)

db = client.escape_from_tarkov

col = db.tarkov_ammo

x = col.find_one()
titles_list = list(x.keys())[1:]
ammo_data_list = []


def ammo_by_size(ammo_size):
    for i in col.find({'Ammo Size': ammo_size}):
        ammo_data_list.append(list(i.values())[2:])
