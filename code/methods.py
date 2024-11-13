import data
from database import db
import math

def width_(w):
    if w >= 160:
        return 166
    return int(w - int(w % 10))

def minTime(machines, past_cutting_time):
    temp = machines[0]

    for machine in machines:

        if not len(machine.estimate):
            machine.default_winding_time = data.MAX_TIME
        elif temp.default_winding_time - past_cutting_time > machine.default_winding_time - past_cutting_time:
            temp = machine

    return temp


def machine_filling(machines_data, reserve):
    machines = [data.Machine(1), data.Machine(2), data.Machine(3)]

    # заполнение сменного задания на каждый станок
    for key in machines_data.keys():
        estimate = []
        for spool in machines_data[key]:
            weight = float(spool[3].replace(',', '.'))
            count_card = db.count_card(spool)
            weight_card = data.weight()[width_(int(spool[2]))]
            temp = []

            while weight >= count_card * weight_card:
                    temp.append(data.Spool(data.Cardboard(spool[0], width_(int(spool[2])), weight_card), count_card, 0.6))
                    weight -= weight_card * count_card
            
            if weight > 0:
                temp.append(data.Spool(data.Cardboard(spool[0], width_(int(spool[2])), weight / count_card), count_card, 0.6))
            
            estimate.append(temp)
        
        machines[key-1].estimate = estimate

    # заполнение резерва каждого станка
    for key in reserve.keys():
        for spool in reserve[key]:
            weight_card = data.weight()[width_(int(spool[1]))]

            for _ in range(int(spool[2])):
                machines[key-1].reserve.cardboards.append(data.Cardboard(spool[0], width_(int(spool[1])), weight_card))

    return machines

def processing(machine, reserve, spool):
    temp_reserve = []

    while machine.trigger[spool.count - 1] < spool.cardboard.weight and spool.cardboard in reserve:
        ind_card_res = reserve.contains(spool.cardboard)
        card = reserve.cardboards.pop(ind_card_res)
        
        for i in range(spool.count):
            if machine.trigger[i] < spool.cardboard.weight:
                ind_card_machine = i
                break

        if card.weight <= spool.cardboard.weight - machine.trigger[ind_card_machine]:
            machine.trigger[ind_card_machine] += card.weight
        else:
            if card.weight - (spool.cardboard.weight - machine.trigger[ind_card_machine]) != 0:
                temp_reserve.append(data.Cardboard(card.quality, card.width, card.weight - (spool.cardboard.weight - machine.trigger[ind_card_machine])))
            machine.trigger[ind_card_machine] = spool.cardboard.weight

    return machine, temp_reserve, reserve

def cutting(machine, width, spool):
    global width_then
    
    reserve = []
    count = 0

    count_reel = db.count_reel(width, spool.cardboard.width)
    count_reel = {70: count_reel[0], 100: count_reel[1], 150: count_reel[2], 166: count_reel[3]}

    for i in range(spool.count):
        if machine.trigger[i] < spool.cardboard.weight:
            count += 1

    coef = math.ceil(count / count_reel[spool.cardboard.width])

    log = [spool.cardboard.quality, spool.cardboard.width, coef, machine.index]

    for key in count_reel.keys():
        count_reel[key] *= coef

    count_reel[spool.cardboard.width] -= count

    for i in range(count):
        if data.weight()[spool.cardboard.width] - (spool.cardboard.weight - machine.trigger[spool.count - 1 - i]) != 0:
            machine.reserve.cardboards.append(data.Cardboard(spool.cardboard.quality, spool.cardboard.width, data.weight()[spool.cardboard.width] - (spool.cardboard.weight - machine.trigger[spool.count - 1 - i])))
        machine.trigger[spool.count - 1 - i] = spool.cardboard.weight

    for key, value in count_reel.items():
        for _ in range(value):
            reserve.append(data.Cardboard(spool.cardboard.quality, key, data.weight()[key]))

    return machine, reserve, log
    

def workshop_150_filling(workshop_data):
    reels = []

    for reel in workshop_data:
        reels.append(data.Spool(data.Cardboard(reel[0], 150, data.weight()[150]), int(reel[1]), 0.6))

    return reels