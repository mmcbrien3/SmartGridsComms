import tkinter
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import pyplot
import requests
import tkinter.messagebox
from CommandsDao import Commands
from MotorDataDao import MotorDatum
import numpy as np

class ClientApplication(object):

    def __init__(self):

        if not self.check_site_up():
            print("Site not running!")
            return
        self.root = tkinter.Tk()
        label_power = tkinter.Label(self.root, text="Power Consumption")
        label_power.grid(row=0, column=2)

        label_cost = tkinter.Label(self.root, text="Power Cost")
        label_cost.grid(row=2, column=2)

        self.update_power_plot()

        f = Figure(figsize=(6, 3), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 7, 7, 6, 3, 2, 3])

        self.cost_canvas = FigureCanvasTkAgg(f, self.root)
        self.cost_canvas.draw()
        self.cost_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5)

        label_button = tkinter.Label(self.root, text="Change Power")
        label_button.grid(row=4, column=0)

        button_increase = tkinter.Button(self.root, text=">", command=self.increase_power)
        button_increase.grid(row=4, column=2)

        button_decrease = tkinter.Button(self.root, text="<", command=self.decrease_power)
        button_decrease.grid(row=4, column=1)

        self.timer_text = "Time to next refresh: "
        self.remaining = 5
        self.label_timer = tkinter.Label(self.root, text = self.timer_text + str(self.remaining))
        self.label_timer.grid(row=4, column = 3)
        self.countdown()

        self.root.mainloop()

    def check_site_up(self):
        try:
            r = requests.head("http://192.168.43.225:5000/Commands")
            return r.status_code == 200
        except:
            return False

    def countdown(self):
        if self.remaining <= 0:
            self.label_timer.configure(text="Refreshing!")
            self.refresh()
            self.remaining = 5
            self.root.after(1000, self.countdown)
        else:
            self.label_timer.configure(text= self.timer_text + str(self.remaining))
            self.remaining = self.remaining - 1
            self.root.after(1000, self.countdown)

    def increase_power(self):
        self.send_command("increase")

    def send_command(self, d):
        URL = "http://192.168.43.225:5000/Commands"
        command = Commands()
        command.set_command(d)
        r = requests.post(URL, command.get_postable())
        pastebin_url = r.text
        print("The pastebin URL is:%s" % pastebin_url)
        tkinter.messagebox.showinfo(title="Command Success", message = "Command %s sent successfully" % (d))

    def decrease_power(self):
        self.send_command("decrease")

    def refresh(self):
        self.update_power_plot()

    def get_motor_data(self):
        URL = "http://192.168.43.225:5000/MotorData"
        r = requests.get(url=URL)
        print(r.json())
        all_motor_data = None
        if len(r.json()) > 0:
            all_motor_data = r.json()
        p = []
        if all_motor_data:
            for k, v in all_motor_data.items():
                p.append(float(v['current'])*float(v['voltage']))
        return [p, range(len(p))]

    def update_power_plot(self):
        f = Figure(figsize=(6, 3), dpi=100)
        a = f.add_subplot(111)
        md = self.get_motor_data()
        print(md[0])
        print(md[1])
        a.plot(md[1], md[0])

        self.power_canvas = FigureCanvasTkAgg(f, self.root)
        self.power_canvas.draw()
        self.power_canvas.get_tk_widget().grid(row=1, column=0, columnspan=5)

if __name__ == "__main__":
    ClientApplication()