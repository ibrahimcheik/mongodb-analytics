from pymongo import MongoClient

client = MongoClient("mongodb+srv://ibrahimcheik:Admin-1993@mflix.jphy3.mongodb.net/mflix?retryWrites=true&w=majority")

print(client.mflix)
