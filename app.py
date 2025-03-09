from tkinter import *
import datetime
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox, Button, Label
import winsound

# Create the main application window
obj = Tk()
obj.geometry("400x200")
obj.title("Alarm Clock")

def alarm():
    # Retrieve the input time values
    x = int(e1.get())
    y = int(e2.get())
    
    # Convert PM time to 24-hour format
    if c1.get() == "PM":
        x += 12
    
    showinfo("Notification", "Alarm has been set")
    
    while True:
        # Check if the current time matches the set alarm time
        if x == datetime.datetime.now().hour and y == datetime.datetime.now().minute:
            showinfo("Notification", "WAKE UP SLEEPY HEAD")
            
            # Beep 100 times when the alarm goes off
            for _ in range(100):
                winsound.Beep(1000, 100)
            break

# Labels for hour and minute input fields
l1 = Label(obj, text="HOURS:")
l2 = Label(obj, text="MINUTES:")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

# Input fields for hour and minute
e1 = Entry(obj)
e2 = Entry(obj)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

# Button to set the alarm
b1 = Button(obj, text="SET ALARM", command=alarm)
b1.grid(row=2, column=1)

# Dropdown to select AM or PM
c1 = Combobox(obj, values=["AM", "PM"])
c1.grid(row=0, column=2)

# Label for AM/PM selection
l3 = Label(obj, text="AM OR PM")
l3.grid(row=0, column=3)

# Run the main event loop
obj.mainloop()
