naam = 'naam'
leeftijd = 'leeftijd'

def x():
    print("Hallo", naam, "je leeftijd is ", leeftijd)
while naam != 'stop' and leeftijd != 'stop':
    naam = input("Wat is uw naam?  : ")
    if naam == 'stop':
        break
    leeftijd = input("Wat is uw leeftijd?  : ")
    if leeftijd == 'stop':
        break

    x()