from database import db
import sys

MAX_TIME = sys.maxsize

def weight():
    return {70: (600 * 75) / 1050, 100: (600 * 105) / 1050, 150: (600 * 150) / 1050, 166: (600 * 166) / 1050}

class Machine:
    def __init__(self, index) -> None:
        self.index = index
        self.estimate = []

        self.trigger = []
        for _ in range(db.capacity(index)):
            self.trigger.append(0)

        self.reserve = Reserve()
        self.default_winding_time = 0

    def clear(self):
        for i in range(len(self.trigger)):
            self.trigger[i] = 0

class Reserve:
    def __init__(self):
        self.cardboards = []

    def __contains__(self, item):
        for t in self.cardboards:
            if t.quality == item.quality and t.width == item.width:
                return True
        return False
    
    def contains(self, item):
        elem = None
        for t in self.cardboards:
            if t.quality == item.quality and t.width == item.width:
                return self.cardboards.index(t)
            
    def concat(self, temp):
        for card in temp:
            self.cardboards.append(card)

    def array(self):
        temp = []
        for card in self.cardboards:
            temp.append([card.quality, card.width, card.weight])
        return temp
    
class Spool:
    def __init__(self, cardboard, count, thickness):
        self.cardboard = cardboard
        self.count = count
        self.thickness = thickness

class Cardboard:
    def __init__(self, quality, width, weight):
        self.quality = quality
        self.width = width
        self.weight = weight


