# Ask user to put his decklist

# texte = input("Entrez un texte : ")

def mappingElements(texte):
  #Create dictionnary with card name for key and card number for value
  map={}

  #Split elements from optcgsim import decklist and put it in a map
  listeText = texte.split(" ")
  for element in listeText:
    info = element.split("x")
    map[info[1]] = info[0]
  return map
  # print(dico)