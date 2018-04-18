#!/usr/bin/python3

import random
import sys
import math
from abc import ABCMeta, abstractmethod


# Shamelessly stolen right off your gitpitch presentation
class Observer(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def update(self):
    pass

class Observable(object):
  def __init__(self):
    self.observers = []

  def add_observer(self, observer):
    if not observer in self.observers:
      self.observers.append(observer)

  def remove_observer(self, observer):
    if observer in self.observers:
      self.observers.remove(observer)

  def remove_all_observers(self):
    self.observers = []

xsize = 5
ysize = 5 


neighborhoodMap = {(0, 0) : "S",  (1, 0) : "ES",  (2, 0) : "WS",   (3, 0) : "ES",  (4, 0) : "W", 
                   (0, 1) : "EN", (1, 1) : "WN",  (2, 1) : "ESN",  (3, 1) : "WN",  (4, 1) : "S", 
                   (0, 2) : "ES", (1, 2) : "WE",  (2, 2) : "WESN", (3, 2) : "WE",  (4, 2) : "WSN", 
                   (0, 3) : "EN", (1, 3) : "WES", (2, 3) : "WEN",  (3, 3) : "WS",  (4, 3) : "SN", 
                   (0, 4) : "E",  (1, 4) : "WEN", (2, 4) : "WE",   (3, 4) : "WEN", (4, 4) : "WN"}
                   
class Home(Observer):
  def __init__(self):
    nummons = random.randint(0, 10)
    game.numMonst = game.numMonst + nummons
    game.origNumMonst = game.numMonst

    self.monsters = []

    for i in range(0, nummons):
      self.monsters.append(random.choice([Vampire(), Ghoul(), Zombie(), Werewolf()]))

  def update(self):
    nummons = len(monsters)

  def spookYou(self):
    numZombs = 0
    numVamps = 0
    numGhuls = 0
    numWolfs = 0
    numPeopl = 0
    msgtoprint = "Monsters!\n"
    for i in self.monsters:
      if (i.__class__.__name__ == "Zombie"):
        numZombs = numZombs + 1
      if (i.__class__.__name__ == "Vampire"):
        numVamps = numVamps + 1
      if (i.__class__.__name__ == "Ghoul"):
        numGhuls = numGhuls + 1
      if (i.__class__.__name__ == "Werewolf"):
        numWolfs = numWolfs + 1
      if (i.__class__.__name__ == "Person"):
        numWolfs = numPeopl + 1

    if (numZombs + numGhuls + numWolfs + numVamps < 1):
      msgtoprint = ""
    if (numZombs > 0):
      msgtoprint = msgtoprint + str(numZombs) + "x Zombie\n"
    if (numVamps > 0):
      msgtoprint = msgtoprint + str(numVamps) + "x Vampire\n"
    if (numWolfs > 0):
      msgtoprint = msgtoprint + str(numWolfs) + "x Werewolf\n"
    if (numGhuls > 0):
      msgtoprint = msgtoprint + str(numGhuls) + "x Ghouls\n"

    if (numPeopl > 0):
      msgtoprint = msgtoprint + "\nThere "

      # My kingdom for a ternary conditional
      # You can have it all, my empire of dirt
      if (numPeopl > 1):
        msgtoprint = msgtoprint + "are "
      if (numPeopl == 1):
        msgtoprint = msgtoprint + "is "
      msgtoprint = msgtoprint + str(numPeopl) + " healthy human"
      if (numPeopl > 1):
        msgtoprint = msgtoprint + "s"

      msgtoprint = msgtoprint + " in the house with you."

    print(msgtoprint)


class Game:
  def __init__(self):
    self.numMonst = 0
    self.origNumMonst = self.numMonst
    self.neighborhood = [[xsize] * ysize for x in range(5)];

  
  def populateHomes(self):
    for i in range(0, xsize):
      for j in range(0, ysize):
        self.neighborhood[i][j] = Home()

  def gameOver(self, killed_by):
    messenger.gameOverMsg(killed_by)
    sys.exit(0)

# Singleton
game = Game()


class itemStack():
  def __init__(self, itemType, num):
    self.itemType = itemType
    self.num = num

  def use(self):
    if (self.num <= 0):
      print("You do not have any of that item to use!")
      return False 

    self.itemType.uses = self.itemType.uses - 1
    if (self.itemType.uses > 0):
      self.itemType.uses = self.itemType.uses - 1

    if (self.itemType.uses == 0):
      self.num = self.num - 1
      self.itemType.uses = self.itemType.maxUses

  def get(self, num):
    self.num = self.num + num
    print("You found " + self.itemType.__class__.__name__ + " " + num + "x.")


class Weapon:
  def __init__(self):
    self.uses = -1
    self.maxUses = -1
    self.mindammod = 1
    self.maxdammod = 1

  def calcDammod(self):
    return random.uniform(self.mindammod, self.maxdammod)


class HersheyKiss(Weapon):
  def __init__(self):
    super().__init__()

class SourStraws(Weapon):
  def __init__(self):
    self.uses = 2
    self.maxUses = 2
    self.mindammod = 1.0
    self.mindammod = 1.75

class ChocolateBar(Weapon):
  def __init__(self):
    self.uses = 4
    self.maxUses = 4
    self.mindammod = 2.0
    self.maxdammod = 2.4


class NerdBombs(Weapon):
  def __init__(self):
    self.uses = 1
    self.maxUses = 1
    self.mindammod = 3.5
    self.maxdammod = 5.0



class You:
  def __init__(self):
    self.hp = 100 + int(random.uniform(0, 27))
    self.damageTable = {}
    self.inventory = [itemStack(HersheyKiss(), 1),
                      itemStack(SourStraws(), 0),
                      itemStack(ChocolateBar(), 0),
                      itemStack(NerdBombs(), 0)]
    self.xloc = 0
    self.yloc = 0

  def takeDamage(self, attacker, mindam, maxdam):
    damage = int(random.uniform(mindam, maxdam))
    self.hp = self.hp - damage
    messenger.damageYouMsg(attacker, damage)
    if (self.hp <= 0):
      game.gameOver()

  def useItem(self, item, target):
    if(item.use()):
      print("You use the " + item.__class__.__name__ + " on " + messenger.name(target) + ".")
      target.takeDamage(item)

  def look(self):
    messenger.exitsMsg(self.xloc, self.yloc)

  def move(self, direction):
    direction = direction.upper()
    if (direction == "NORTH"):
      direction = "N"
    elif (direction == "SOUTH"):
      direction = "S"
    elif (direction == "EAST"):
      direction = "E"
    elif (direction == "WEST"):
      direction = "W"
    elif (len(direction) > 1 or direction not in ("NSEW")):
      print("I've never heard of such a direction.")
      return False

    if (direction not in neighborhoodMap[(self.xloc, self.yloc)]):
      print("There is no exit in that direction!")
      return False
    elif (direction == "N"):
      self.yloc = self.yloc - 1
    elif (direction == "S"):
      self.yloc = self.yloc + 1
    elif (direction == "E"):
      self.xloc = self.xloc + 1
    elif (direction == "W"):
      self.xloc = self.xloc - 1

    self.look()
    game.neighborhood[self.xloc][self.yloc].spookYou()
    return True

# Singleton, so no other "yous" out there
you = You()


class NPC(Observable):
  def __init__(self):
    self.mindammod = 1
    self.maxdammod = 1
    self.hp = 1
    self.damageTable = {}

  # References the damage table and sees what the damage modifier for a given
  # weapon is, and
  def calcDammod(self, wep):
    damage = self.damageTable.get(wep.__class__.__name__, 1)

  # Deducts hit points from the monster's total, and prints a relevant message.
  def takeDamage(self, wep):
    damage = int(self.calcDammod(wep) * wep.calcDammod())
    self.hp = self.hp - damage
    message.damageMessage(you, wep, self, damage)
    if (self.hp <= 0):
        self.beDefeated()

  def attackPlayer():
    you.takeDamage(self.mindammod, self.maxdammod)

  def beDefeated(self):
    messenger.defeatMsg(self)
 
    for i in observers:
      i.monsters.remove(self)
      i.monsters.append(Person())
      i.update()


class Person(NPC):
  def __init__(self):
    self.minatk = -1;
    self.maxatk = -1;
    self.hp = 100
    self.damageTable = {
      'HersheyKiss': 0,
      'SourStraws': 0,
      'ChocolateBar': 0,
      'NerdBombs': 0
    }


class Zombie(NPC):
  def __init__(self):
    self.minatk = 0
    self.maxatk = 10
    self.hp = random.randint(50, 100)
    self.damageTable = { 'SourStraws': 2 }


class Vampire(NPC):
  def __init__(self):
    self.minatk = 10
    self.maxatk = 20
    self.hp = random.randint(100, 200)
    self.damageTable = { 'ChocolateBar': 0 }

class Werewolf(NPC):
  def __init__(self):
    self.minatk = 0
    self.maxatk = 40
    self.hp = 200
    self.damageTable = {
      'ChocolateBar': 0,
      'SourStraws': 0
    }

class Ghoul(NPC):
  def __init__(self):
    self.minatk = 15
    self.maxatk = 30
    self.hp = random.randint(40, 80)
    self.damagetable = {'NerdBombs': 5}



class Messages():
  # Returns the name of the given creature, with or without a definite
  # article as necessary
  def name(self, creature):
    if (creature is  you):
      return 'you'
    else:
      return 'the ' + creature.__class__.__name__


  # Returns the possessive form of the given string
  def genit(self, noun):

    if (noun is you):
      return 'your'
    else:
      return name(noun) + '\'s'


  # Returns the properly-conjugated form of the verb "to be"
  def is_are(self, noun):
    if (noun is you):
      return 'are'
    else:
      return 'is'


  # Returns a phrase consisting of the name() of a creature
  # followed by its is_are()
  def x_is(self, noun):
    return self.name(noun) + ' ' + self.is_are(noun)


  # Sends a message based on damage dealt to a monster
  def damageMsg(attacker, weapon, target, damage):
    msgtoprint = 'Can\'t happen'

    if (damage == 0):
      msgtoprint = self.x_is(target).capitalize() + ' unharmed by '
      msgtoprint = msgtoprint + self.genit(attacker)
      msgtoprint = msgtoprint + weapon.__class__.__name__ + '!'

    elif (target.calcDammod(weapon) > 1 ):
      msgtoprint = self.name(target).capitalize() + ' '
      msgtoprint = msgtoprint + 'winces!'

    if (damage < 0):
      msgtoprint = self.x_is(attacker).capitalize() + ' healing '
      msgtoprint = msgtoprint + self.genit(target) + ' wounds. '
      msgtoprint = msgtoprint + self.x_is(target).capitalize()
      msgtoprint = msgtoprint + ' healed for ' + (-1 * damage) + '.'

    elif (damage > 0):
      msgtoprint = msgtoprint + self.name(attacker).capitalize() + ' takes '
      msgtoprint = msgtoprint + damage + ' points of damage!'

    print(msgtoprint)

  # Sends a message based on damage dealt to you
  def damageYouMsg(attacker, damage):
    msgtoprint = 'Can\'t happen'
    target = you

    if (damage == 0):
      msgtoprint = self.x_is(target).capitalize() + ' unharmed by '
      msgtoprint = msgtoprint + self.name(attacker) + '!'

    if (damage < 0):
      msgtoprint = self.x_is(attacker).capitalize() + ' healing '
      msgtoprint = msgtoprint + self.genit(target) + ' wounds. '
      msgtoprint = msgtoprint + self.x_is(target).capitalize()
      msgtoprint = msgtoprint + ' healed for ' + (-1 * damage) + '.'

    elif (damage > 0):
      msgtoprint = msgtoprint + self.name(target).capitalize() + ' take '
      msgtoprint = msgtoprint + damage + ' points of damage!'

    print(msgtoprint)


  # Sends the message indicating that a monster has been defeated.
  def defeatMsg(defeated):
    print(self.name(defeated) + ' returns to human form.')

  def gameOverMsg(self, killed_by):
    msgtoprint = 'Goodbye.'
    if (killed_by.__class__.__name__ == 'Zombie'):
      msgtoprint = 'Your lifeless body falls to the ground before slowly rising from the dead with a moan...'
    if (killed_by.__class__.__name__ == 'Vampire'):
      msgtoprint = 'Drained of blood, you feel your consciousness fading...\n'
      msgtoprint = msgtoprint + 'You come to in a coffin, '
      msgtoprint = msgtorpint + 'feeling strangely thirsty.'
    if (killed_by.__class__.__name__ == 'Ghoul'):
      msgtoprint = 'You are paralyzed in fear, and you feel your blood run '
      msgtoprint = msgtoprint + 'cold... You lie motionless for hours before the feeling finally returns to your limbs.\n'
      msgtoprint = msgtoprint + 'You hunger for corpses.'
    if (killed_by.__class__.__name__ == 'Werewolf'):
      msgtoprint =  'The moon is shining high above your head. '
      msgtoprint = msgtoprint + 'The hair on the scruff of your neck stands on end, and '
      msgtoprint = msgtoprint + 'a hideous transformation racks your body and '
      msgtoprint = msgtoprint + 'mind.'

    print(msgtoprint)
    print('= = = G A M E  O V E R = = =')
    msgtoprint = 'You defeated ' + str(game.origNumMonst - game.numMonst) + ' out of '
    msgtoprint = msgtoprint + str(game.origNumMonst) + ' monsters before '
    if (not (killed_by is None)):
      msgtoprint = msgtoprint + 'falling to ' + self.name(killed_by) + '.'
    else:
      msgtoprint = msgtoprint + 'quitting.'
    print(msgtoprint)
    print("\nBetter luck next time!")


  def exitsMsg(self, x, y):
    exits = neighborhoodMap[(x, y)]
    msgtoprint = '\nThere are exits in the following directions: '

    for d in exits:
      if (d == 'N'):
        msgtoprint = msgtoprint + 'north '
      if (d == 'S'):
        msgtoprint = msgtoprint + 'south '
      if (d == 'E'):
        msgtoprint = msgtoprint + 'east '
      if (d == 'W'):
        msgtoprint = msgtoprint + 'west '
    
    print(msgtoprint)

  def inventory():
    msgtoprint = "You carry the following items:\n"
    for i in self.inventory:
      if (i.num > 0):
        msgtoprint = msgtoprint + i.num + "x" + self.name(i.itemType)
        if (i.itemType.uses > 0):
          msgtoprint = msgtoprint + " (" + i.itemType.uses + " uses)"
        msgtoprint = msgtoprint + "\n"

    print(msgtoprint)

# Singleton
messenger = Messages()


class interpreter():
  def __init__(self):
    pass

  def read(text):
    text = text.lower()

    if (text == 'quit'):
      if (input("Do you want to quit? (Type 'y' to confirm) ") == 'y'):
        game.gameOver(None)

    if (text == 'north' or
        text == 'south' or
        text == 'east'  or 
        text == 'west'  or
        text == 'n'     or
        text == 's'     or
        text == 'e'     or
        text == 'w'):
      you.move(text)

    if (text[0:3] == 'go '):
      you.move(text[3:])

    if (text[0:6] == 'move '):
      you.move(text[6:])
    
    if (text == 'look'):
      you.look()

    if (text == 'loc'):
      print(str(you.xloc) + ", " + str(you.yloc))

    if (text[0:4] == 'use '):
      arg = text[4:]
      if (arg == "hersheykiss" or arg == "hershey" or arg == "kiss" or arg == "hk"):
        use = HersheyKiss
      elif (arg == "chocolatebar" or arg == "chocolate" or arg == "choco" or arg == "bar" or arg == "cb"):
        use = ChocolateBar
      elif (arg == "sourstraw" or arg == "sourstraws" or arg == "sour" or arg == "straw" or arg == "straws" or arg == "ss"):
        use = SourStraws
      elif (arg == "nerdbombs" or arg == "nerds" or arg == "bombs" or arg == "nerdbomb" or arg == "nerd" or arg == "bomb" or arg == "nb"):
        use = NerdBombs
      else:
        print("I've never heard of such an item...")

      foundItem = False
      print("use: " + str(use)) # delet this

      for item in you.inventory:
        print(str(item.itemType.__class__)) # delet this
        if item.itemType.__class__ is use.__class__:
          print(str(item.itemType.__class__) + " found") # delet this
          foundItem = True
          if item.use():
            for mon in game.neighborhood[you.xloc][you.yloc]:
              if mon is not Person:
                you.useItem(item, mon)
      
      if (not foundItem):
        print("You don't have any of that item!")


#class HersheyKiss(Weapon)
#class SourStraws(Weapon)
#class ChocolateBar(Weapon)
#class NerdBombs(Weapon)

game.populateHomes()
you.look()
while(True):
  text = input(">")
  interpreter.read(text)
