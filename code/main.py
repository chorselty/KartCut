import  gui, data, methods
from logs import xlxs
from database import db
import sys, math

past_cutting_time = 0
width_then = 0

class Main:
    def __init__(self, ui):
        self.ui = ui
    
    def workshop_main(self, machines, reserve, stage):
        global past_cutting_time, width_then
        past_cutting_time_local = 0

        while methods.minTime(machines, 0).default_winding_time != data.MAX_TIME:
            machine = methods.minTime(machines, past_cutting_time_local)

            for spool in machine.estimate.pop(0):
                
                # Проверка резерва станка навивки на наличие нужного картона
                machine, temp_reserve, machine.reserve = methods.processing(machine, machine.reserve, spool)
                machine.reserve.concat(temp_reserve)

                # Проверка общего резерва на наличие нужного картона
                machine, temp_reserve, reserve = methods.processing(machine, reserve, spool)
                machine.reserve.concat(temp_reserve)

                # Проверка на количество заполненных полос
                if machine.trigger[spool.count - 1] < spool.cardboard.weight:
                    width = self.ui.add_roller_row([spool.cardboard.quality, spool.cardboard.width, db.roller(spool.cardboard.quality), machine.index - 1])
                    machine, temp_reserve, log = methods.cutting(machine, width, spool) # Резка
                    reserve.concat(temp_reserve)

                    xlxs.result(log, stage, past_cutting_time)

                    past_cutting_time_local += db.time_cut(spool, width_then) * log[2]
                    

                    width_then = spool.cardboard.width

                machine.default_winding_time += db.time_wind(spool)
                machine.clear()
            
            machines[machine.index - 1] = machine

        past_cutting_time += past_cutting_time_local
        return machines, reserve
        
    def workshop_additionally(self, machines, reserve):
        return self.workshop_main(machines, reserve, 'additionally')

    def workshop_150(self, reels, reserve):
        global past_cutting_time, width_then
        past_cutting_time_local = 0
        for reel in reels:
            while reel.cardboard in reserve and reel.count != 0:
                reel.count -= reserve.cardboards.pop(reserve.contains(reel.cardboard))
            if reel.count != 0:
                width = self.ui.add_roller_row([reel.cardboard.quality, reel.cardboard.width, db.roller(reel.cardboard.quality), 0])
                count_reels = db.count_reel(width, 150)[2]

                coef = math.ceil(reel.count / count_reels)

                past_cutting_time_local += db.time(reel, width_then)[0] * coef
                width_then = 150

                xlxs.result([reel.cardboard.quality, reel.cardboard.width, coef], '150', past_cutting_time)

                count_reels = count_reels * coef
                count_reels -= reel.count

                for i in range(count_reels):
                    reserve.cardboards.append(data.Cardboard(reel.cardboard.quality, 150, data.weight()[150]))
        past_cutting_time += past_cutting_time_local
        return reserve
    
    def next_day_reserve(self, machines, reserve):
        return self.workshop_main(machines, reserve, 'reserve')



    def get(self, name):
        m_1 = self.ui.get_today_m_1()
        m_2 = self.ui.get_today_m_2()
        m_3 = self.ui.get_today_m_3()

        rm_1 = self.ui.get_reserve_m_1()
        rm_2 = self.ui.get_reserve_m_2()
        rm_3 = self.ui.get_reserve_m_3()

        tm_1 = self.ui.get_tommorow_m_1()
        tm_2 = self.ui.get_tommorow_m_2()
        tm_3 = self.ui.get_tommorow_m_3()

        a = self.ui.get_addititonal()

        thf = self.ui.get_thf()

        names = {
            'main': [{1: m_1, 2: m_2, 3: m_3}, {1: rm_1, 2: rm_2, 3: rm_3}],
            'additionaly': [{1: a, 2: [], 3: []} , {1: [], 2: [], 3: []}],
            '150': thf,
            'yesterday': {1: tm_1, 2: tm_2, 3: tm_3},
        }

        return names[name]

    def main(self):
        global past_cutting_time
        reserve = data.Reserve()

        db.connect()
        xlxs.create()

        machines = methods.machine_filling(self.get('main')[0], self.get('main')[1])
        machines, reserve = self.workshop_main(machines, reserve, 'main')

        machines_additionaly = methods.machine_filling(self.get('additionaly')[0], self.get('additionaly')[1])
        _, reserve = self.workshop_additionally(machines_additionaly, reserve)

        reels = methods.workshop_150_filling(self.get('150'))
        reserve = self.workshop_150(reels, reserve)

        machines_yesterday = methods.machine_filling(self.get('yesterday'), {1: machines[0].reserve.array(), 2: machines[1].reserve.array(), 3: machines[2].reserve.array()}) # не заработает, резерв поправить        
        self.next_day_reserve(machines_yesterday, reserve)
        print(past_cutting_time)


app = gui.QApplication(sys.argv)
mwindow = gui.MainWindow()
mwindow.show()
window = gui.Ui_MainWindow()
window.setupUi(mwindow, app)
method = Main(window)
window.assign_fuction(method)
app.exec()