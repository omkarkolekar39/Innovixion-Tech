import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S %p')
    time_label.config(text=current_time)
    time_label.after(1000, update_time)  # Update every 1000 milliseconds (1 second)

# Create the main window
root = tk.Tk()
root.title("Current Time Display")

# Create a label to display the time
time_label = tk.Label(root, font=('Bahnschrift', 40, 'bold'), background='black', foreground='white')
time_label.pack(anchor='center')

# Call the update_time function to initialize and start updating the time
update_time()

# Run the Tkinter event loop
root.mainloop()