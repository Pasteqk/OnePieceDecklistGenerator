import csv 

def csvRead(filename):

    dictionarry = {}
    with open (filename) as file:
        reader = csv.reader(file,delimiter = ",")
        for ligne in reader:
            dictionarry[ligne[0]] = ligne[1:]
    return dictionarry

def getCard(dictionarry, idCard):
    return dictionarry.get(idCard, "Carte inconnu")

dictionarry = csvRead("onePieceTcgCardDatabase.csv")
print(dictionarry)