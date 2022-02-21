###UPDATE STRING IN APPWORX .EXP FILE for Process flows/chains.###
###Created: 8/23/2017###
###Last updated: 7/9/2019 Added functions###
###Last update: 12/11/2019 Created two new functions to speed up process###
###Last update: 12/18/2019 Use class inplace of function###
###Last update: 03/8/2021 Set up tkinter GUI###
###Last update: 04/9/2021 Added CSV options###
###Last update: 01/19/2022 Added options to update libraries, job/process flows, and tasks
###Last update: 02/02/2022 refined search replace options
###Last update: 02/02/2022 moved fuctions and classes to different files

import update as upd
import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import showinfo
from datetime import datetime

def backup_file(exp_file):
    now = datetime.now()
    timestamp = now.strftime("%H%M%S")
    with open(exp_file,"r") as FR:
        FILEBK = FR.read()
        with open(f'{exp_file}.{timestamp}.bak',"w") as F:
            F.write(FILEBK)
           
#GUI FUNCTIONS

def browse_button():
    global exp_file
    filetypes = [('Export Files', '*.exp')]
    folder_path = r'C:\Users\aico0r\OneDrive - Arrow Electronics, Inc'
    exp_file = filedialog.askopenfilename(title = 'Open export file', initialdir = folder_path, filetypes = filetypes)
    showinfo(message = exp_file)

def browse_button_2():
    global csv_file
    filetypes = [('CSV Files', '*.csv')]
    folder_path = r'C:\Users\aico0r\OneDrive - Arrow Electronics, Inc'
    csv_file = filedialog.askopenfilename(title = 'Open CSV file', initialdir = folder_path, filetypes = filetypes)
    showinfo(message = csv_file)

def clear_button_3():
    global csv_file
    csv_file = None
    showinfo(message = 'Cleared CSV File')

def edit_options():
    global jobs_chk
    global tasks_chk
    global libs_chk
    jobs_chk = jobschk.get()
    tasks_chk = taskschk.get()
    libs_chk = libschk.get()

    
def set_choice_var():
    global choice
    choice = var.get()
    
def submit():
    backup_file(exp_file)
    string_search_02 = string_search_01.get()
    string_replace_02 = string_replace_01.get()
    complete = upd.update_file(string_search_02, string_replace_02, csv_file, exp_file, jobs_chk, tasks_chk, libs_chk, choice)
    showinfo(message = complete)

#set variables
    
choice = None
csv_file = None
jobs_chk = None
tasks_chk = None
libs_chk = None

#Define window
wind = tk.Tk()
wind.geometry("450x300")
wind.title('APPWORX RENAME')

BANNER = tk.Label(wind, fg="red", font='Helvetica 10 bold', text=
"This program renames chains/process flows for .exp files\n\
It is a good idea to check .exp for errors with editor before importing.\n")

BANNER.grid(row=0, column=0)

#Export file select

button1 = tk.Button(wind, text="SELECET .exp File", command = browse_button)
button1.grid(row=4, column=0, sticky=tk.W)

#CSV file select
button2 = tk.Button(wind, text="SELECET .csv File", command = browse_button_2)
button2.grid(row=5, column=0, sticky=tk.W)

#CSV file clear
clear_csv_button = tk.Button(wind, text="Clear CSV", command = clear_button_3 )
clear_csv_button.grid(row=5, column=0, sticky=tk.W, padx=100, ipadx=10)

#Check Boxes
#Edit Jobs PF
jobschk = tk.IntVar()
job_pf_option = tk.Checkbutton(wind, text="Process Flows/Jobs", variable = jobschk, command = edit_options )
job_pf_option.grid(row=6, column=0, sticky=tk.W)

#Edit Component tasks
taskschk = tk.IntVar()
job_pf_option = tk.Checkbutton(wind, text="Tasks/Components", variable = taskschk, command = edit_options )
job_pf_option.grid(row=7, column=0, sticky=tk.W)

#Edit Libraries
libschk = tk.IntVar()
job_pf_option = tk.Checkbutton(wind, text="Libraires", variable = libschk, command = edit_options )
job_pf_option.grid(row=8, column=0, sticky=tk.W)

#string entries
tk.Label(wind, text="Old String").grid(row=9, column=0, sticky=tk.W)
tk.Label(wind, text="New String").grid(row=12, column=0, sticky=tk.W)

string_search_01 = tk.Entry()
string_replace_01 = tk.Entry()

string_search_01.grid(row=9, column=0, sticky=tk.W, padx=65, ipadx=40)
string_replace_01.grid(row=12, column=0, sticky=tk.W, padx=65, ipadx=40)

#radiobutton
var = tk.StringVar()
Y_radio = tk.Radiobutton(wind, text="Turn off schedules", variable = var, value='N', command = set_choice_var)
Y_radio.grid(row=14, column=0, sticky=tk.W)
N_radio = tk.Radiobutton(wind, text="Turn on schedules", variable = var, value='Y', command = set_choice_var)
N_radio.grid(row=15, column=0, sticky=tk.W)

#submit button
SubmitButton = tk.Button(text="Submit", command = submit )
SubmitButton.grid(row=100, column=0, sticky=tk.W)

wind.mainloop()



