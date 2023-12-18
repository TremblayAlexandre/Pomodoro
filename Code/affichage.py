import time
from tkinter import *
from tkinter import messagebox as alert

class Affichage:
    def __init__(self):
        # -- THE APP SETTINGS --
        self.root = Tk()
        self.root.title("Pomodoro")
        self.root.geometry("500x500")
        self.root.configure(background="white")

        # -- END OF THE APP SETTINGS --

        # -- TIMER ATTRIBUTES --
        self.hourString = StringVar()
        self.minString = StringVar()
        self.secString = StringVar()
        # default values
        self.hourString.set("00")
        self.minString.set("00")
        self.secString.set("00")

        # initialising the text boxes
        self.hourTextBox = Entry(self.root, width=3, font=("Calibri", 20, ""), textvariable=self.hourString)
        self.minutesTextBox = Entry(self.root, width=3, font=("Calibri", 20, ""), textvariable=self.minString)
        self.secondTextBox = Entry(self.root, width=3, font=("Calibri", 20, ""), textvariable=self.secString)

        # placing & centering the text boxes
        self.hourTextBox.place(x=170,y=180)
        self.minutesTextBox.place(x=220,y=180)
        self.secondTextBox.place(x=270,y=180)



        # initialising the button obj
        self.setTimeBtn = Button(self.root, text='Set Time', bd='5', command=self.runTimer)
        self.setTimeBtn.place(relx=0.5, rely = 0.5, anchor=CENTER)


    def run(self):
        # Start the Tkinter event loop
        self.root.mainloop()

    def runTimer(self):
        try:
            clockTime = int(self.hourString.get()) * 3600 + int(self.minString.get()) * 60 + int(self.secString.get())
        except:
            print("Incorrect values")

        while (clockTime >=0 ):

            totalMinutes, totalSeconds = divmod(clockTime, 60)

            totalHours = 0
            if (totalMinutes > 60):
                totalHours, totalMinutes = divmod(totalMinutes, 60)

            self.hourString.set(f"{totalHours}")
            self.minString.set(f"{totalMinutes}")
            self.secString.set(f"{totalSeconds}")

            ### Update the interface
            self.root.update()
            time.sleep(1)

            ### Let the user know if the timer has expired
            if (clockTime == 0):
                alert.showinfo("", "Your time has expired!")

            clockTime -= 1