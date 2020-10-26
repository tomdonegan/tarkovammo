import gspread
import pymongo
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint



scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)

client = gspread.authorize(creds)

sheet = client.open("tarkovammo").sheet1  # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records

# titles_list = []
#
# table_titles = data[0].keys()
# table_values = data[0].values()
#
# table_width = len(table_titles)
#
# ammo_size_data = {}
#
#
# # Finds data for each individual size
# def retrieve_ammo_data_by_size(ammo_size):
#     for i in enumerate(data):
#         if i[1][''] == ammo_size:
#             print(i[1][''])







