from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk,Image
from datetime import datetime
from time import *
from threading import Thread
from pygame import mixer
#IMPORTED REQUIRED LIBRARIES

#Creating Window
window = Tk()
window.title("Alarm Clock")
window.geometry("440x220")
window.configure(bg="white")

#Frame Line
frame_line = Frame(window,width=440, height=2, bg="black")
frame_line.grid(row=0, column=0)

#Body Where it will be easy to make Changes
body = Frame(window, width=440, height=218, bg="aliceblue")
body.grid(row=1, column=0)

#Displaying Current Time
currenttimetitle = Label(body, text="Current Time:", height=1, font="Candara 15 bold",bg="aliceblue", fg="midnightblue")
currenttimetitle.place(x=10, y=0)

def update_time():
    current_time = strftime('%I:%M:%S %p')
    time_label.config(text=current_time)
    time_label.after(1000, update_time)
    #This after keyword help in Updating the called function in 1000 milliseconds(1000milliseconds = 1 second)

#Create a label to display the time
time_label = Label(body, font=('Bahnschrift', 20), bg="aliceblue")
time_label.place(x=10, y=23)

#Call the update_time function to initialize and start updating the time
update_time()


#Displaying the Image Of Clock PNG File
img = Image.open("alarmclock.png")
img = ImageTk.PhotoImage(img)

#Placement of Image
app_image = Label(body, height=100, image=img, bg="aliceblue")
app_image.place(x=15, y=80)

#Printing and Placing Heading
heading = Label(body, text="Set The Alarm at:", height=1, font='Bahnschrift 22 bold',bg="aliceblue", fg="black")
heading.place(x=140, y=74)

#Printing and Placing Hour
hour = Label(body, text="Hour", height=1, font="Candara 15",bg="aliceblue", fg="midnightblue")
hour.place(x=140, y=110)

#Creatind and Placing Hour ComboBox
combobox_hour = Combobox(body, width=3, font=("Bahnschrift 14"))
combobox_hour['values'] = ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")          #values in combobox can be stored in similar way too which is showed in next 4 lines
#start_value = 1
#end_value = 12
#values = [str(x) for x in range(start_value, end_value + 1)]
#combobox_hour['values'] = values
combobox_hour.current(11)
combobox_hour.place(x=145, y=140)

#Printing and Placing Minute
minute = Label(body, text="Minute", height=1, font="Candara 15",bg="aliceblue", fg="midnightblue")
minute.place(x=210, y=110)

#Creatind and Placing Minute ComboBox
combobox_minute = Combobox(body, width=3, font=("Bahnschrift 14"))
combobox_minute['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09",
                           "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
                           "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
                           "30", "31", "32", "33", "34", "35", "36", "37", "38", "39",
                           "40", "41", "42", "43", "44", "45", "46", "47", "48", "49",
                           "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")                    #values in combobox can be stored in similar way too which is showed in next 4 lines
#start_value = 0
#end_value = 59
#values = [str(x) for x in range(start_value, end_value + 1)]
#combobox_minute['values'] = values
combobox_minute.current(0)
combobox_minute.place(x=215, y=140)

#Printing and Placing Second
second = Label(body, text="Second", height=1, font="Candara 15",bg="aliceblue", fg="midnightblue")
second.place(x=280, y=110)

#Creatind and Placing Minute ComboBox
combobox_second = Combobox(body, width=3, font=("Bahnschrift 14"))
combobox_second['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09",
                           "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
                           "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
                           "30", "31", "32", "33", "34", "35", "36", "37", "38", "39",
                           "40", "41", "42", "43", "44", "45", "46", "47", "48", "49",
                           "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")                  #values in combobox can be stored in similar way too which is showed in next 4 lines
#start_value = 0
#end_value = 59
#values = [str(x) for x in range(start_value, end_value + 1)]
#combobox_second['values'] = values
combobox_second.current(0)
combobox_second.place(x=285, y=140)

#Printing and Placing TimePeriod
timeperiod = Label(body, text="Period", height=1, font="Candara 15",bg="aliceblue", fg="midnightblue")
timeperiod.place(x=350, y=110)

#Creatind and Placing TimePeriod ComboBox
combobox_timeperiod = Combobox(body, width=3, font=("Candara 14"))
combobox_timeperiod['values'] = ("AM","PM")
combobox_timeperiod.current(0)
combobox_timeperiod.place(x=355, y=140)

#Activate Alarm
def activate_alarm():
    t = Thread(target=alarm)
    t.start()

def deactivate_alarm():
    print("Deactivated Alarm: ", selected.get())
    mixer.music.stop()

selected = IntVar()

#Creating RadioButton for Activating The Alarm
activate = Radiobutton(body, text="Activate The Alarm", font=("Rockwell 15 bold"), value=1, bg="aliceblue", command=activate_alarm, variable=selected)
activate.place(x=140, y=175)

selected = IntVar()

#Creating RadioButton for Deactivating The Alarm
deactivate = Radiobutton(body, text="Deactivate The Alarm", font=("Rockwell 15 bold"), value=2, bg="aliceblue", command=deactivate_alarm, variable=selected)
deactivate.place(x=180, y=20)



#Defining mp3 File in Function
def sound_alert():
    mixer.music.load("beepalarm.mp3")
    mixer.music.play()
    selected.set(0)
    
def alarm():
    while True:
        control = 1
        print(control)
        alarm_period = combobox_timeperiod.get()
        alarm_hour = combobox_hour.get()
        alarm_minute = combobox_minute.get()
        alarm_second = combobox_second.get()

        now = datetime.now()
        
        periodnow = now.strftime("%p")
        hournow = now.strftime("%I")
        minutenow = now.strftime("%M")
        secondnow = now.strftime("%S")

        if control == 1:
            if alarm_period == periodnow:
                if alarm_hour == hournow:
                    if alarm_minute == minutenow:
                        if alarm_second == secondnow:
                            sound_alert()
        sleep(1)

mixer.init()

window.mainloop()