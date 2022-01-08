import tkinter as tk
from tkinter import ttk


# define the aloe_vera window
def AVeraWindow(root): 
    root.title('Aloe Vera')
    root.geometry('525x500')
    root.configure(bg='#4b8d2f')
    root.grid()
    createWidgets(root)
    return root

# create a slider
def createSlider(container, f, t): 
    s = tk.Scale(container, bg='#4b8d2f', orient='horizontal', fg='white', activebackground='blue', 
                 from_=int(f), to=int(t), 
                 length=300)
    return s

def createLabel(container, t):
    l = tk.Label(text=t, background='#4b8d2f', foreground='white', justify='left', anchor=tk.W, padx=25, pady=25)
    return l


def createWidgets(container):

    # create the stress label: 
    stress_label = createLabel(container, 'What was your percieved stress level today?:\n0–25: Resting state, \n26–50: Low stress, \n51–75: Medium stress,\n76–100: High stress')
    stress_label.grid(row=0, column=0)

    # create and grid the stress slider
    stress_slider = createSlider(container, 0, 100)
    stress_slider.grid(row=0, column=1)

    # create the energy label: 
    energy_label = createLabel(container, 'This is a energy slider: ')
    energy_label.grid(row=1, column=0)

    # create and grid the energy slider
    energy_slider = createSlider(container, 0, 100)
    energy_slider.grid(row=1, column=1)

    # create the energy label: 
    rank_label = createLabel(container, 'This is a energy slider: ')
    rank_label.grid(row=2, column=0)

    # create and grid the energy slider
    rank_slider = createSlider(container, 0, 10)
    rank_slider.grid(row=2, column=1)

    
def main(): 
    window = tk.Tk()
    app = AVeraWindow(window)
    app.mainloop()

if __name__ == '__main__':
    main()