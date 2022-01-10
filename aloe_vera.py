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
    
    global stress_lev, sleep_lev, body_bat_lev, stress_int, sleep_int, body_bat_int
    stress_lev = StringVar(root, value='Resting State')
    sleep_lev = StringVar(root, value='Poor')
    body_bat_lev = StringVar(root, value='0')
    stress_int = tk.IntVar(root, value=0)
    sleep_int = tk.IntVar(root, value=0)
    body_bat_int = tk.IntVar(root, value=0)
    
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

# updates the sleep level label
def update_sleep_lev(var):
    global sleep_lev
    new_val = int(var)
    
    if new_val > 99: 
        sleep_lev.set('Excellent')
    elif new_val > 79: 
        sleep_lev.set('Good')
    elif new_val > 49:
        sleep_lev.set('Moderate')
    else: 
        sleep_lev.set('Poor')
    
# updates the stress level label
def update_stress_lev(var):
    global stress_lev
    new_val = int(var)
    
    if new_val < 26: 
        stress_lev.set('Resting State')
    elif new_val < 51: 
        stress_lev.set('Low Stress')
    elif new_val < 76:
        stress_lev.set('Medium Stress')
    else: 
        stress_lev.set('High Stress')

# update the body battery label
def update_battery_level(var):
    global body_bat_lev
    body_bat_lev.set(var)

def submit_vals():
    global stress_int, sleep_int, body_bat_int
    print(stress_int.get(), sleep_int.get(), body_bat_int.get())
    
    

# creates the widgets to go in the container passed to it 
def createWidgets(container):
    global stress_lev, sleep_lev, stress_int, body_bat_int, sleep_int

    # create the stress label:
    stress_label = createLabel(container, 'What was your percieved stress level today?')
    stress_label.grid(row=0, column=0)
    
    # create and grid the stress slider
    stress_slider = createSlider(container, 0, 100, c=update_stress_lev, v=stress_int)
    stress_slider.grid(row=0, column=1)
    
    # categorize the slider state to the right
    level_label = tk.Label(container, background=BACKGROUND, textvariable=stress_lev, padx=25, pady=25, fg='white')
    level_label.grid(row=0, column = 3)

    # create the sleep label: 
    sleep_label = createLabel(container, 'How well do you think you slept last night?')
    sleep_label.grid(row=1, column=0)

    # create and grid the sleep slider
    sleep_slider = createSlider(container, 0, 100, c=update_sleep_lev, v=sleep_int)
    sleep_slider.grid(row=1, column=1)

    # categorize the slider state to the right
    sleep_level_label = tk.Label(container, background=BACKGROUND, textvariable=sleep_lev, padx=25, pady=25, fg='white')
    sleep_level_label.grid(row=1, column = 3)

    # create the energy label: 
    body_battery_q = createLabel(container, 'Where do you think your body battery is right now?')
    body_battery_q.grid(row=2, column=0)

    # create and grid the energy slider
    body_battery_slider = createSlider(container, 0, 100, c=update_battery_level, v=body_bat_int)
    body_battery_slider.grid(row=2, column=1)

    # categorize the slider state to the right
    body_battery_label = tk.Label(container, background=BACKGROUND, textvariable=body_bat_lev, padx=25, pady=25, fg='white')
    body_battery_label.grid(row=2, column = 3)

    # 
    submit_button = tk.Button(container, text='Submit', highlightbackground=BACKGROUND, fg='white', activeforeground='blue', command=submit_vals)
    submit_button.grid(row=3, column=1)

    
def main(): 
    window = tk.Tk()
    app = AVeraWindow(window)
    app.mainloop()

if __name__ == '__main__':
    main()