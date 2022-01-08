import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk


# define the aloe_vera app class
class AVeraApp(ThemedTk): 
    def __init__(self):
        super().__init__()
        self.title('Aloe Vera')
        self.geometry('500x500')
        self.grid()
        self.theme = 'arc'
        self.createWidgets()

    def sliderChanged(self, var):
        newvalue = float(var)
        newvalue = round(newvalue, 0)
        self.s1.set(newvalue)
        print(var)

    def createSlider(self):
        s = ttk.Scale(self, from_=0, to_=100, orient='horizontal', command=self.sliderChanged)
        return s

    def createWidgets(self):
        self.s1 = self.createSlider()
        self.s1.grid(row=0, column=0)


def main(): 
    app = AVeraApp()
    app.mainloop()

if __name__ == '__main__':
    main()