import tkinter
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import requests
import tkinter.messagebox
from CommandsDao import Commands
from MotorDataDao import MotorDatum
import numpy as np


class ClientApplication(object):
    Price30 =[2.0, 2.0, 1.9, 1.7, 1.9, 1.7, 1.7, 2.2, 2.2, 2.5, 2.3, 2.4, 2.1, 2.3, 2.3, 2.2, 2.1, 2.1, 2.2, 4.6, 2.5, 2.3, 2.0, 2.0]
    Price31 = [1.9, 1.9, 1.9, 2.2, 2.0, 1.9, 2.0, 2.3, 3.4, 2.3, 0.4, 1.8, 2.5, 2.5, 2.3, 2.3, 2.3, 2.5, 2.7, 3.3, 5.8, 4.5, 3.1, 2.9]
    Price1 = [2.9, 3.3, 2.7, 2.8, 2.5, 2.6, 5.0, 6.6, 2.7, 2.9, 3.0, 3.0, 2.9, 2.8, 2.5, 2.3, 2.2, 2.5, 2.6, 17.2, 11.4, 3.1, 2.6, 2.4]
    Price2 = [2.3, 2.5, 2.5, 2.6, 2.6, 2.7, 2.5, 3.0, 2.9, 3.3, 3.1, 3.1, 2.9, 3.4, 3.0, 2.7, 2.8, 2.6, 2.7, 3.9, 2.8, 3.3, 2.6, 2.3]
    Price3 = [2.4, 2.6, 2.3, 2.4, 2.6, 2.9, 4.1, 9.8, 4.9, 2.6, 3.4, 2.6, 3.7, 2.8, 2.4, 2.3, 2.3, 2.4, 3.0, 3.1, 3.5, 2.8, 2.3, 2.2]
    Price4 = [2.4, 2.2, 2.2, 2.2, 1.9, 1.9, 1.9, 2.8, 2.6, 2.9, 2.9, 2.4, 2.6, 2.6, 2.4, 2.4, 2.5, 2.3, 2.5, 2.6, 2.3, 2.8, 4, 2.2, 2.2]
    Price5 = [2.2, 2.2, 2.2, 2.3, 2.4, 2.6, 3.1, 3.6, 3.4, 6.0, 6.6, 5.0, 3.7, 3.9, 4.0, 3.7, 3.6, 4.5, 2.9, 3.8, 3.7, 3.2, 3.7, 3.0]
    Price6 = [2.8, 2.4, 2.5, 2.5, 2.3, 2.7, 2.6, 3.0, 2.8, 2.8, 3.2, 2.6, 2.3, 2.3, 2.2, 2.4, 2.5, 2.4, 2.3, 2.5, 2.8, 2.2, 2.2, 1.9]
    Price7 = [2.0, 1.9, 2.0, 1.9, 1.9, 2.0, 2.0, 2.2, 2.2, 2.5, 2.2, 2.3, 2.3, 2.3, 2.0, 2.2, 2.2, 2.0, 2.4, 2.9, 2.6, 2.9, 2.4, 2.0]
    Price8 = [2.1, 2.0, 1.9, 1.9, 1.9, 2.3, 11.9, 8.7, 2.5, 2.7, 2.7, 3.0, 3.8, 2.7, 3.0, 4.3, 2.6, 3.0, 3.0, 2.9, 3.2, 2.6, 2.2, 2.1]

    Load30 = [8.85, 5.05, 0, 6.31, 6.31, 7.58, 6.31, 6.31, 6.32, 3.26, 2.52, 3.78, 5.04, 2.52, 3.78, 2.52, 5.05, 2.52, 3.78, 3.78, 3.78, 6.31, 6.31, 7.58]
    Load31 = [6.31, 6.31, 6.31, 7.58, 6.31, 6.31, 6.31, 7.58, 5.04, 12.66, 30.32, 6.31, 10.09, 16.47, 19.01, 15.2, 13.94, 13.94, 7.58, 7.58, 7.58, 8.85, 11.39, 10.12]
    Load1 = [10.12, 10.12, 11.39, 10.12, 8.85, 11.39, 11.39, 8.85, 8.85, 13.93, 51.96, 8.85, 29.16, 16.47, 16.47, 15.17, 12.66, 10.12, 5.04, 7.58, 7.58, 8.85, 7.58, 8.85]
    Load2 = []
    Load3 = []
    Load4 = []
    Load5 = []
    Load6 = []
    Load7 = []
    Load8 = []

    root_url = "http://192.168.43.225:5000"
    
    def __init__(self):

        if not self.check_site_up():
            print("Site not running!")
            return
        self.root = tkinter.Tk()
        self.root.geometry("1200x750")
        label_power = tkinter.Label(self.root, text="Power Consumption")
        label_power.grid(row=0, column=2)

        label_cost = tkinter.Label(self.root, text="Power Cost")
        label_cost.grid(row=0, column=7)

        self.update_power_plot()

        self.update_cost_plots()

        label_button = tkinter.Label(self.root, text="Change Power")
        label_button.grid(row=2, column=0)

        button_increase = tkinter.Button(self.root, text=">", command=self.increase_power)
        button_increase.grid(row=2, column=2)

        button_decrease = tkinter.Button(self.root, text="<", command=self.decrease_power)
        button_decrease.grid(row=2, column=1)

        self.timer_text = "Time to next refresh: "
        self.remaining = 5
        self.label_timer = tkinter.Label(self.root, text = self.timer_text + str(self.remaining))
        self.label_timer.grid(row=2, column = 3)
        self.countdown()

        self.root.mainloop()

    def check_site_up(self):
        try:
            r = requests.head(self.root_url + "/Commands")
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
        URL = self.root_url + "/Commands"
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
        URL = self.root_url + "/MotorData"
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

    def update_cost_plots(self):
        f = Figure(figsize=(6, 3), dpi=100)
        a = f.add_subplot(111)
        Price = self.Price30+self.Price31+self.Price1+self.Price2+self.Price3+self.Price4+self.Price5+self.Price6+self.Price7+self.Price8
        Load = self.Load30+self.Load31+self.Load1+[11.39]
        a.plot(Load)
        a.set_xlabel('Time in hours')
        a.set_ylabel('Load in KWh')
        f.tight_layout()
        self.power_canvas = FigureCanvasTkAgg(f, self.root)
        self.power_canvas.draw()
        self.power_canvas.get_tk_widget().grid(row=1, column=5, columnspan=5)

        Load = self.Load1
        Cost = self.Load1
        n = len(Cost)
        Price = self.Price1
        Rebate = [0, 0, 0, 0, 0, 0, 0, 0, 14, 14, 20, 20, 14, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
        index = range(1, 25)
        Pd = 5
        NewDemand = np.zeros(n)
        minimumPrice = np.zeros(n)
        New_Cost = np.zeros(n)
        IndxMinPrice = np.zeros(n)
        FinalPrice = 0
        NewPrice = np.zeros((n, n))
        for i in range(len(Cost)):
            for j in range(len(Cost)):
                NewPrice[i, j] = (Price[j]-Rebate[i]+Rebate[j])+Pd*abs(i-j)

            minimumPrice[i] = min(NewPrice[i, :])
            for j in range(len(Cost)):
                if NewPrice[i, j] == minimumPrice[i]:
                    IndxMinPrice[i] = j

        for i in range(len(Cost)):
            for j in range(len(Cost)):
                if IndxMinPrice[j] == i:
                    NewDemand[i] = NewDemand[i] + Load[j]
                    k = abs(j-i)
                    if k == 0:
                        New_Cost[i] = New_Cost[i] + Load[i]*Price[i]
                    else:
                        New_Cost[i] = New_Cost[i] + (Pd*k+Price[i])*Load[j]

        InitialPrice = np.zeros(n)
        Initial_Price = np.zeros(n)
        InitialPricef = 0
        for i in range(len(Cost)):
            New_Cost[i] = New_Cost[i] - Rebate[i]*Load[i]
            FinalPrice = FinalPrice + New_Cost[i]
            Initial_Price[i] = InitialPrice[i] + Load[i]*Price[i]
            InitialPricef = InitialPricef + Initial_Price[i]

        f = plt.Figure(figsize=(6, 2), dpi=100)
        a = f.add_subplot(111)
        line1, = a.plot(NewDemand, 'r')
        line2, = a.plot(self.Load1, 'b')
        a.set_xlabel("Time (hours)")
        a.set_ylabel('Consumption in KWh')
        a.legend(handles=[line1, line2], labels=["New Demand", "Initial Load"])
        f.tight_layout()
        self.power_canvas = FigureCanvasTkAgg(f, self.root)
        self.power_canvas.draw()
        self.power_canvas.get_tk_widget().grid(row=2, column=5, columnspan=5)

        f = plt.Figure(figsize=(6, 2), dpi=100)
        a = f.add_subplot(111)
        line1, = a.plot(New_Cost, 'r')
        line2, = a.plot(Initial_Price, 'b')
        a.set_xlabel("Time (hours)")
        a.set_ylabel("Prices in c$/KWh")
        a.legend(handles=[line1, line2], labels=["New Cost", "Initial Price"])
        f.tight_layout()
        self.power_canvas = FigureCanvasTkAgg(f, self.root)
        self.power_canvas.draw()
        self.power_canvas.get_tk_widget().grid(row=3, column=5, columnspan=5)



if __name__ == "__main__":
    ClientApplication()