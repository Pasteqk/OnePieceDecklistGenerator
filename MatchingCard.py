from MappingElements import mappingElements
from csvReader import csvRead


def matchingCard(texte):
    leader = []
    character = []
    event = []
    elements = mappingElements(texte)

    dictionnarry = csvRead("onePieceTcgCardDatabase.csv")


    for clé in dictionnarry:
        # Si la clé est déjà dans l'ensemble, c'est une clé en double
        if clé in elements:
            if dictionnarry[clé][1]=="Leader":
                leader.append(dictionnarry[clé][0]+"("+clé+")"+" x "+elements[clé][0])
            if dictionnarry[clé][1]=="Character":
                character.append(dictionnarry[clé][0]+"("+clé+")"+" x "+elements[clé][0])
            if dictionnarry[clé][1]=="Event":
                event.append(dictionnarry[clé][0]+"("+clé+")"+" x "+elements[clé][0])
    # print(leader)
    # print(character)
    # print(event)