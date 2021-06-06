
from pymongo import MongoClient

client = MongoClient("mongodb+srv://luis:-#sAEThgbr#tjs8@scrapping.w5sjz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database('mercado_libre')

#la idea es que esto mas adelante reciba la tabla
def get_record_count(table=None):
    records =db.series_x #esto que dice series x la idea es que se cambie por lo que llegue en table
    return records.count_documents({})

def post_record(product,table=None):
    records = db.series_x #esto que dice series x la idea es que se cambie por lo que llegue en table
    records.insert_one(product)
