import os
from tkinter import *
from PIL import ImageTk, Image
#Imported Required Libraries

#Main Window
window = Tk()
window.title("Bank Account Management System")

#Functions
def finish_register():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()

    if name == "" or age == "" or gender == "" or password == "":
        notif.config(fg= "red", text= "Please Enter All The Required Details *")
        return

    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg= "red", text= "Account Already Exists")
            return
        else:
            new_file = open(name,"w")
            new_file.write(name+"\n")
            new_file.write(password+"\n")
            new_file.write(age+"\n")
            new_file.write(gender+"\n")
            new_file.write("0")
            new_file.close()
            notif.config(fg= "green", text= "Account Created")

def register():
    #Variables
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()

    #Register Screen
    register_screen = Toplevel(window)
    register_screen.title("Register")

    #Labels
    Label(register_screen , text= "Please Enter Your Required Details Below to Register", font= ("Calibri bold", 16)).grid(row= 0, sticky= N,pady= 10)
    Label(register_screen , text= "Name", font= ("Calibri", 14)).grid(row= 1, sticky= W)
    Label(register_screen , text= "Age", font= ("Calibri", 14)).grid(row= 2, sticky= W)
    Label(register_screen , text= "Gender", font= ("Calibri", 14)).grid(row= 3, sticky= W)
    Label(register_screen , text= "Password", font= ("Calibri", 14)).grid(row= 4, sticky= W)
    notif = Label(register_screen , font= ("Calibri", 14))
    notif.grid(row= 6, sticky= N, pady= 10)

    #Entries
    Entry(register_screen, textvariable= temp_name, width= 40).grid(row= 1,column= 0)
    Entry(register_screen, textvariable= temp_age, width= 40).grid(row= 2,column= 0)
    Entry(register_screen, textvariable= temp_gender, width= 40).grid(row= 3,column= 0)
    Entry(register_screen, textvariable= temp_password,show= "*", width= 40).grid(row= 4,column= 0)

    #Buttons
    Button(register_screen, text= "Register", command= finish_register, font= ("Calibri", 14)).grid(row= 5, sticky= N, pady= 10)

def login_successful():
    global login_name
    all_accounts = os.listdir()
    login_name  = temp_login_name.get()
    login_password = temp_login_password.get()

    for name in all_accounts:
        if name == login_name:
            print("Account Already Exists")
            file = open(name,"r")
            file_data = file.read()
            file_data = file_data.split("\n")
            password = file_data[1]
            #Account Dashboard   
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(window)
                account_dashboard.title("Dashboard")

                #Labels
                Label(account_dashboard, text= "Account Dashboard", font= ("Calibri bold", 20)).grid(row= 0, sticky= N, pady= 10)
                Label(account_dashboard, text= "Welcome", font= ("Calibri", 18)).grid(row= 1, sticky= N, pady= 5)

                #Buttons
                Button(account_dashboard, text= "Personal Details", font= ("Calibri", 16), command= personal_details, width= 40).grid(row= 2, sticky= N, padx= 10)
                Button(account_dashboard, text= "Deposit", font= ("Calibri", 16), command= deposit, width= 40).grid(row= 3, sticky= N, padx= 10)
                Button(account_dashboard, text= "Withdraw", font= ("Calibri", 16), command= withdraw, width=40).grid(row= 4, sticky= N, padx= 10)
                Label(account_dashboard).grid(row= 5, sticky= N, pady= 10)
                return
            else:
                login_notif.config(fg= "red", text= "Inncorrect Password!")
                return
    login_notif.config(fg= "red", text= "No Account Found!")

def personal_details():
    #Variables
    file = open(login_name,"r")
    file_data = file.read()
    user_details = file_data.split("\n")
    details_name = user_details[0]
    details_age = user_details[2]
    details_gender = user_details[3]
    details_balance = user_details[4]

    #Personal Details Screen
    personal_details_screen = Toplevel(window)
    personal_details_screen.title("Personal Details")

    #Labels
    Label(personal_details_screen, text= "Personal Details", font= ("Calibri bold", 20)).grid(row= 0, sticky= N, pady= 10)
    Label(personal_details_screen, text= "Name : "+details_name, font= ("Calibri", 16)).grid(row= 1, sticky= W)
    Label(personal_details_screen, text= "Age : "+details_age, font= ("Calibri", 16)).grid(row= 2, sticky= W)
    Label(personal_details_screen, text= "Gender : "+details_gender, font= ("Calibri", 16)).grid(row= 3, sticky= W)
    Label(personal_details_screen, text= "Balance : $"+details_balance, font= ("Calibri", 16)).grid(row= 4, sticky= W)


def deposit():
    #Variables
    global amount
    global deposit_notif
    global current_balance_label
    amount = StringVar()
    file = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split("\n")
    details_balance = user_details[4]
    
    #Deposit Screen
    deposit_screen = Toplevel(window)
    deposit_screen.title("Deposit")

    #Labels
    Label(deposit_screen, text = "Deposit", font= ("Calibri bold", 20)).grid(row= 0, sticky= N, pady= 10)
    current_balance_label = Label(deposit_screen, text = "Current Balance : $"+details_balance, font= ("Calibri", 16))
    current_balance_label.grid(row= 1, sticky= W, pady= 10)
    Label(deposit_screen, text = "Amount : ", font= ("Calibri", 14)).grid(row= 2, sticky= W, pady= 10)
    deposit_notif = Label(deposit_screen, font= ("Calibri", 14))
    deposit_notif.grid(row= 4, sticky= N, pady= 10)

    #Entry
    Entry(deposit_screen, textvariable= amount, width= 40).grid(row= 2, column= 1)

    #Button
    Button(deposit_screen, text= "Finish", font= ("Calibri", 14), command= finish_deposit).grid(row= 3, sticky= N, pady= 10)

def finish_deposit():
    if amount.get() == "":
        deposit_notif.config(text= "Enter Amount to Deposit!", fg= "red")
        return
    if float(amount.get()) <= 0:
        deposit_notif.config(text= "Negative Currency is not Accepted to Deposit!", fg= "red")
        return
    
    file = open(login_name, "r+")
    file_data = file.read()
    details = file_data.split("\n")
    current_balance = details[4]
    updated_balance = current_balance
    updated_balance = float(updated_balance) + float(amount.get())
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text= "Current Balance : $"+str(updated_balance), fg= "green")
    deposit_notif.config(text= "Balance Updated!", fg= "green")

def withdraw():
    #Variables
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount = StringVar()
    file = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split("\n")
    details_balance = user_details[4]
    
    #Deposit Screen
    withdraw_screen = Toplevel(window)
    withdraw_screen.title("Withdraw")

    #Labels
    Label(withdraw_screen, text = "Deposit", font= ("Calibri bold", 20)).grid(row= 0, sticky= N, pady= 10)
    current_balance_label = Label(withdraw_screen, text = "Current Balance : $"+details_balance, font= ("Calibri", 16))
    current_balance_label.grid(row= 1, sticky= W, pady= 10)
    Label(withdraw_screen, text = "Amount : ", font= ("Calibri", 14)).grid(row= 2, sticky= W, pady= 10)
    withdraw_notif = Label(withdraw_screen, font= ("Calibri", 14))
    withdraw_notif.grid(row= 4, sticky= N, pady= 10)

    #Entry
    Entry(withdraw_screen, textvariable= withdraw_amount, width= 40).grid(row= 2, column= 1)

    #Button
    Button(withdraw_screen, text= "Finish", font= ("Calibri", 14), command= finish_withdraw).grid(row= 3, sticky= N, pady= 10)

def finish_withdraw():
    if withdraw_amount.get() == "":
        withdraw_notif.config(text= "Enter Amount to Deposit!", fg= "red")
        return
    if float(withdraw_amount.get()) <= 0:
        withdraw_notif.config(text= "Negative Currency is not Accepted to Deposit!", fg= "red")
        return
    
    file = open(login_name, "r+")
    file_data = file.read()
    details = file_data.split("\n")
    current_balance = details[4]
    
    if float(withdraw_amount.get()) > float(current_balance):
        withdraw_notif.config(tex= "Insufficient Funds", fg= "red")
        return

    updated_balance = current_balance
    updated_balance = float(updated_balance) - float(withdraw_amount.get())
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text= "Current Balance : $"+str(updated_balance), fg= "green")
    withdraw_notif.config(text= "Balance Updated!", fg= "green")

def login():
    #Variables
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_name = StringVar()
    temp_login_password = StringVar()

    #Login Screen
    login_screen = Toplevel(window)
    login_screen.title("Login")

    #Labels
    Label(login_screen, text="Login to Your Account", font= ("Calibri bold", 16)).grid(row= 0, sticky= N, pady= 10)
    Label(login_screen, text="Username", font= ("Calibri", 14)).grid(row= 1, sticky= W)
    Label(login_screen, text="Password", font= ("Calibri", 14)).grid(row= 2, sticky= W)
    login_notif = Label(login_screen , font=("Calibri", 14))
    login_notif.grid(row= 4, sticky= N)

    #Entry
    Entry(login_screen, textvariable= temp_login_name, width= 40).grid(row= 1,column= 1, padx= 10)
    Entry(login_screen, textvariable= temp_login_password,show= "*", width= 40).grid(row= 2,column= 1, padx= 10)

    #Buttons
    Button(login_screen, text= "Login", command= login_successful, font=("Calibri", 12)).grid(row= 3, sticky= N, pady= 10)


#Importing Image on Main Window
img = Image.open("bank.png")
img = img.resize((300,200))
img = ImageTk.PhotoImage(img)

#Labels
Label(window, text= "Bank Account Management System", font= ("Calibri bold", 20)).grid(row= 0, sticky=N, pady= 10)
Label(window, text= "Best Bank Account Management System GUI Which is Easy To Use", font= ("Calibri", 16)).grid(row= 10, sticky=N)
Label(window, image=img).grid(row=2, sticky=N, pady= 10)

#Buttons
Button(window, text="Login", font=("Calibri", 12),width= 30, command= login).grid(row= 3, sticky=N)
Button(window, text="Register", font=("Calibri", 12),width= 30, command= register).grid(row= 4, sticky=N, pady= 10)




window.mainloop()