import tkinter as tk
from tkinter import StringVar, ttk
from typing_extensions import IntVar


BACKGROUND = '#4b8d2f'

# define the aloe_vera window
def AVeraWindow(root): 
    root.title('Aloe Vera')
    root.geometry('800x300')
    root.configure(bg=BACKGROUND)
    root.grid()
    
    global lev, lev_color
    lev = StringVar(root, value='Resting State')
    lev_color = StringVar(root, value='White')
    
    createWidgets(root)
   
    return root

# create a slider
def createSlider(container, f, t, c=None, v=None): 
    s = tk.Scale(container, bg=BACKGROUND, orient='horizontal', fg='white', activebackground='blue', 
                 from_=int(f), to=int(t), 
                 length=300, command=c, variable=v)
    return s

# create a label
def createLabel(container, t):
    l = tk.Label(container, text=t, background=BACKGROUND, foreground='white', justify='left', anchor=tk.W, padx=25, pady=25)
    return l


def update_stress_var(var):
    global lev, lev_color
    new_val = int(var)
    
    if new_val < 26: 
        lev.set('Resting State')

    elif new_val < 51: 
        lev.set('Low Stress')

    elif new_val < 76:
        lev.set('Medium Stress')

    else: 
        lev.set('High Stress')
    
    
    
def createWidgets(container):
    global lev, lev_color

    # create the stress label:
    stress_label = createLabel(container, 'What was your percieved stress level today?')
    stress_label.grid(row=0, column=0)
    
    # create and grid the stress slider
    stress_slider = createSlider(container, 0, 100, c=update_stress_var)
    stress_slider.grid(row=0, column=1)
    
    # categorize the slider state to the right
    level_label = tk.Label(container, background=BACKGROUND, textvariable=lev, padx=25, pady=25, fg='white')
    level_label.grid(row=0, column = 3)

    # create the energy label: 
    sleep_label = createLabel(container, 'How well do you think you slept last night?')
    sleep_label.grid(row=1, column=0)

    # create and grid the energy slider
    sleep_slider = createSlider(container, 0, 100)
    sleep_slider.grid(row=1, column=1)

    # create the energy label: 
    body_battery_label = createLabel(container, 'Where do you think your body battery is right now?')
    body_battery_label.grid(row=2, column=0)

    # create and grid the energy slider
    body_batter_slider = createSlider(container, 0, 100)
    body_batter_slider.grid(row=2, column=1)

    
def main(): 
    window = tk.Tk()
    app = AVeraWindow(window)
    app.mainloop()

if __name__ == '__main__':
    main()