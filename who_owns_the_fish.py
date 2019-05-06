houses = [{} for i in range(5)]
for house in houses:
    house['color'] = None
    house['nationality'] = None
    house['drinks'] = None
    house['smokes'] = None
    house['pet'] = None

# The man living in the house right in the center drinks milk.
houses[2]['drinks'] = 'milk'
# The Norwegian lives in the first house
houses[0]['nationality'] = 'Norwegian'
# The Norwegian lives next to the blue house
houses[1]['color'] = 'blue'

color= ['red', 'white', 'yellow', 'green']
nationality = ['Brit', 'German', 'Dane', 'Swede']
drinks = ['beer', 'water', 'tea', 'coffee']
smokes = ['Dunhills', 'Princes', 'Bluemasters', 'Blends', 'Pall Malls']
pet = ['dogs', 'horses', 'birds', 'cats', 'THE FISH']

def emptyHouseAttr():
    for house in houses:
        if house['color'] == None:
            return house, color, 'color'
        elif house['nationality'] == None:
            return house, nationality, 'nationality'
        elif house['drinks'] == None:
            return house, drinks, 'drinks'
        elif house['smokes'] == None:
            return house, smokes, 'smokes'
        elif house['pet'] == None:
            return house, pet, 'pet'
    return None, None, None
            
def search(houses):
    house, attribute, attrName = emptyHouseAttr();
    
    if len(color) == 0 and len(nationality) == 0 and len(drinks) == 0 and len(smokes) == 0 and len(pet) == 0:
        for house in houses:
            print '\n'
            print 'Color: ' + house['color']
            print 'Nationality: ' + house['nationality']
            print 'Drinks: ' + house['drinks']
            print 'Smokes: ' + house['smokes']
            print 'Pet: ' + house['pet']
        return
        
    while attribute:
        value = attribute[0]
        attribute.remove(attribute[0])
        house[attrName] = value
        
        if checkValues(house):
            search(houses)
        else:
            house[attrName] = None
            attribute.append(value)
            search(houses)
            
            
        house[attrName] = None # Clear the assignment
    return

def checkValues(house):
    bool = True
    if not brit_lives_in_red_house(house):  bool = False 
    if not yellow_house_dunhills(house):    bool = False 
    if not swed_keeps_dogs(house):  bool = False 
    if not german_princes(house):   bool = False
    if not green_house_coffee(house):   bool = False  
    if not dane_drinks_tea(house):   bool = False
    if not bluemasters_and_beers(house):    bool = False
    if not pall_malls_and_birds(house): bool = False
    if not green_house_left_white_house(houses):    bool = False
    if not blends_nextto_water(houses): bool = False
    if not blends_nextto_cats(houses):  bool = False
    if not dunhills_nextto_horses(houses):  bool = False
    return bool

def brit_lives_in_red_house(house):
    # At least one value is unassigned---skip this house
    if house['nationality'] is None or house['color'] is None:
        return True
    
    # One value is either Brit or red, but the other is not
    elif house['nationality'] == 'Brit' and house['color'] != 'red':
        return False
    elif house['nationality'] != 'Brit' and house['color'] == 'red':
        return False
    
    # No house contradicts the test
    else:
        return True

def swed_keeps_dogs(house):
    if house['nationality'] is None or house['pet'] is None:    return True
    elif house['nationality'] == 'Swede' and house['pet'] != 'dogs':    return False
    elif house['nationality'] != 'Swede' and house['pet'] == 'dogs':    return False
    else:   return True
    
def dane_drinks_tea(house):
    if house['nationality'] is None or house['drinks'] is None: return True
    if house['nationality'] == 'Dane' and house['drinks'] != 'tea':     return False
    if house['nationality'] != 'Dane' and house['drinks'] == 'tea':     return False
    else:
        if house['nationality'] == 'Dane' and house['pet'] == 'THE FISH':
            house['pet'] = None
            pet.append('THE FISH')
        return True
    
def green_house_coffee(house):
    if house['color'] is None or house['drinks'] is None:   return True
    if house['color'] == 'green' and house['drinks'] != 'coffee':   return False
    if house['color'] != 'green' and house['drinks'] == 'coffee':
        if house['color'] == 'yellow':
            house['color'] = None
            color.append('yellow')
        return False
    else: return True

def pall_malls_and_birds(house):
    if house['smokes'] is None or house['pet'] is None: return True
    if house['smokes'] == 'Pall Malls' and house['pet'] != 'birds': return False
    if house['smokes'] != 'Pall Malls' and house['pet'] == 'birds': return False
    else:   return True

def yellow_house_dunhills(house):
    if house['smokes'] is None or house['color'] is None:   return True
    if house['smokes'] == 'Dunhills' and house['color'] != 'yellow':    return False
    if house['smokes'] != 'Dunhills' and house['color'] == 'yellow':
        if house['drinks'] == 'beer':
            house['drinks'] = None
            drinks.append('beer')
        return False
    else: return True

def bluemasters_and_beers(house):
    if house['smokes'] is None or house['drinks'] is None:  return True
    if house['smokes'] == 'Bluemasters' and house['drinks'] != 'beer':  return False
    if house['smokes'] != 'Bluemasters' and house['drinks'] == 'beer':
        if house['nationality'] == 'German':
            house['nationality'] = None
            nationality.append('German')
            if house['drinks'] == 'beer':
                house['drinks'] = None
                drinks.append('beer')
        return False
    else:   return True
    
def german_princes(house):
    if house['smokes'] is None or house['nationality'] is None: return True
    if house['smokes'] == 'Princes' and house['nationality'] != 'German':   return False
    if house['smokes'] != 'Princes' and house['nationality'] == 'German':   return False
    else: return True
    
def green_house_left_white_house(houses):
    if houses[0]['color'] == 'white':
        return False
    for i in range(len(houses) - 1):
        if houses[i]['color'] is None or houses[i + 1]['color'] is None:    continue
        if houses[i]['color'] == 'green' and houses[i + 1]['color'] != 'white': return False
        if houses[i]['color'] != 'green' and houses[i + 1]['color'] == 'white': return False
    return True

def blends_nextto_water(houses):
    for i in range(len(houses) - 1):
        if houses[i]['smokes'] is None and houses[i + 1]['drinks'] is None or houses[i - 1]['drinks'] is None:  return True
        if houses[i]['smokes'] == 'Blends' and houses[i + 1]['drinks'] != 'water' and houses[i - 1]['drinks'] != 'water':   return False
        if houses[i]['smokes'] != 'Blends' and (houses[i + 1]['drinks'] == 'water' or houses[i - 1]['drinks'] == 'water'):  return False
    return True
    
def blends_nextto_cats(houses):
    for i in range(len(houses) - 1):
        if houses[i]['smokes'] is None and houses[i + 1]['pet'] is None or houses[i - 1]['pet'] is None:    return True
        if houses[i]['smokes'] == 'Blends' and houses[i + 1]['pet'] == 'cats' or houses[i - 1]['pet'] == 'cats':  return True
        if houses[i]['smokes'] == 'Blends' and (houses[i + 1]['pet'] != 'cats' or houses[i - 1]['pet'] != 'cats'):  return False
        if houses[i]['smokes'] != 'Blends' and houses[i + 1]['pet'] == 'cats' or houses[i - 1]['pet'] == 'cats':    return False
    return True

def dunhills_nextto_horses(houses):
    for i in range(len(houses) - 1):
        if houses[i]['smokes'] == 'Dunhills' and houses[i]['pet'] == 'horses':  return False
        if houses[i]['smokes'] is None and houses[i + 1]['pet'] is None or houses[i - 1]['pet'] is None:    return True
        if houses[i]['smokes'] == 'Dunhills' and houses[i + 1]['pet'] == 'horses' or houses[i - 1]['pet'] == 'horses':  return True
        if houses[i]['smokes'] == 'Dunhills' and houses[i + 1]['pet'] != 'horses' and houses[i - 1]['pet'] != 'horses': return False
        if houses[i]['smokes'] != 'Dunhills' and (houses[i + 1]['pet'] == 'horses' or houses[i - 1]['pet'] == 'horses'):    return False
    return True

search(houses)

