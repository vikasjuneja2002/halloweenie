#!/usr/bin/python3

import random
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

neighborhoodMap = {(0, 0) : "E", 
                   (0, 1) : "SW", 
                   (0, 2) : "SE", 
                   (0, 3) : "SW", 
                   (0, 4) : "S",
                   (1, 0) : "SE", 
                   (1, 1) : "NW", 
                   (1, 2) : "NS", 
                   (1, 3) : "NSE", 
                   (1, 4) : "NSW",
                   (2, 0) : "NE", 
                   (2, 1) : "SEW", 
                   (2, 2) : "NSEW", 
                   (2, 3) : "NSW", 
                   (2, 4) : "NS",
                   (3, 0) : "SE", 
                   (3, 1) : "NW", 
                   (3, 2) : "NS", 
                   (3, 3) : "NE", 
                   (3, 4) : "NSW",
                   (4, 0) : "N", 
                   (4, 1) : "E", 
                   (4, 2) : "NEW", 
                   (4, 3) : "EW", 
                   (4, 4) : "NW"}

class Game:
  def __init__(self, numMonst):
    self.numMonst = numMonst
    self.neighborhood = [][]

    for i in range(0, xsize)
      for j in range(0, ysize)
        self.neighborhood[i][j] = Home()


class Home(Observer):
  def __init__(self):
    nummons = random.randint(0, 10)
    exits = [False, False, False, False]

    for i in range(0, nummons):
      monsters[i] = random.choice([ Vampire(), Ghoul(), Zombie(), Werewolf()])

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
    message.damageMessage(player, wep, self, damage)

  def update(self):

  def beDefeated(self):
    Messages.defeatMsg(self)
    update()


class Weapon:
  def __init__(self):
    self.uses = -1
    self.mindammod = 1
    self.maxdammod = 1

  def calcDammod(self):
    return random.uniform(self.mindammod, self.maxdammod)


class HersheyKiss(Weapon):
  def __init__(self):
    super().__init__()


class ChocolateBar(Weapon):
  def __init__(self):
    self.uses = 4
    self.mindammod = 2.0
    self.maxdammod = 2.4


class NerdBombs(Weapon):
  def __init__(self):
    self.uses = 1
    self.mindammod = 3.5
    self.maxdammod = 5.0



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
    slef.maxatk = 10
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
  def name(creature):
    if (creature is  you):
      return 'you'
    else:
      return 'the ' + creature.__class__.__name__


  # Returns the possessive form of the given string
  def genit(noun):

    if (noun is you):
      return 'your'
    else:
      return name(noun) + '\'s'


  # Returns the properly-conjugated form of the verb "to be"
  def is_are(noun):
    if (noun is you):
      return 'are'
    else:
      return 'is'


  # Returns a phrase consisting of the name() of a creature
  # followed by its is_are()
  def x_is(noun):
    return self.name(noun) + ' ' + self.is_are(noun)


  # Sets a message based on damage dealt
  def damageMsg(attacker, weapon, target, damage):
    msgtoprint = 'Can\'t happen'

    if (damage == 0):
      msgtoprint = self.x_is(target).capitalize() + ' unharmed by '
      msgtoprint = msgtoprint + self.genit(attacker) + ' the '
      msgtoprint = msgtoprint + weapon.__class__.__name__ + '!'

    elif (target.calcDammod(weapon) > 1 ):
      msgtoprint = name(target).capitalize() + ' '
      msgtoprint = msgtoprint + 'wince'

      if (target is not you):
        msgtoprint = msgtoprint + 's'

      msgtoprint = msgtoprint + '! '

    if (damage < 0):
      msgtoprint = attacker.name() + ' heals '
      msgtoprint = msgtoprint + target.genit() + ' wounds.'


    print(msgtoprint)

  # Sends the message indicating that a monster has been defeated.
  def defeatMsg(defeated):
    print(self.name(defeated) + ' returns to human form.')
 
  def exitsMsg(x, y):
    exits = neighborhoodMap[(x, y)]
    msgtoprint = 'There are exits in the following directions: '

    for d in exits:
      if (d == 'N')
        msgtoprint = msgtoprint + 'north '
      if (d == 'S')
        msgtoprint = msgtoprint + 'south '
      if (d == 'E')
        msgtoprint = msgtoprint + 'east '
      if (d == 'W')
        msgtoprint = msgtoprint + 'west '


class itemStack():
  def __init__(self, itemType, num):
    this.itemType = itemType
