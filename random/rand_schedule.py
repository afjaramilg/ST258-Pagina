#lavadora, secadora, tv, AC, estufa
import random
import pymongo
electro=["lavadora","secadora", "tv", "ac", "estufa"]

horario = {
    "hora_1": [],
    "hora_2": [],
    "hora_3": [],
    "hora_4": [],
    "hora_5": [],
    "hora_6": [],
    "hora_7": [],
    "hora_8": [],
    "hora_9": [],
    "hora_10": [],
    "hora_11": [],
    "hora_12": [],
    "hora_13": [],
    "hora_14": [],
    "hora_15": [],
    "hora_16": [],
    "hora_17": [],
    "hora_18": [],
    "hora_19": [],
    "hora_20": [],
    "hora_21": [],
    "hora_22": [],
    "hora_23": [],
    "hora_24": [],
}


#print(random.choices(electro,k=random.randint(0,5)))

for x in horario:
    lista = random.choices(electro,k=random.randint(0,5))
    lista = list(dict.fromkeys(lista))
    horario[x]= lista

client = pymongo.MongoClient("mongodb+srv://luis:bbkNOQ65@scrapping.w5sjz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.integrador
db.schedule.delete_many({})
db.schedule.insert_one(horario)
print(horario)