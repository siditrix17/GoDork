#Main file for execution make other file for each op

import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk


gui = Tk()


#the main headers for gui
	# Set the background colour of GUI window
gui.configure(background = "white")

	# set the name of tkinter GUI window
gui.title("GO-DoRK V1")

	# Set the configuration of GUI window
gui.geometry("800x500")

#----------------------

ourMessage ='''


 _____             _____        _____  _  __ __      ____ 
  / ____|           |  __ \      |  __ \| |/ / \ \    / /_ |
 | |  __  ___ ______| |  | | ___ | |__) | ' /   \ \  / / | |
 | | |_ |/ _ \______| |  | |/ _ \|  _  /|  <     \ \/ /  | |
 | |__| | (_) |     | |__| | (_) | | \ \| . \   _ \  /   | |
  \_____|\___/      |_____/ \___/|_|  \_\_|\_\ (_) \/    |_|
                                                            
                                                            

'''


def gettarget():
    #getting the target web address//
    target= entry.get()
    dork=prop.get()
    d_para=payload.get()
    command= "site:"+target+"  "+dork+":"+d_para
    webbrowser.open('https://google.com/search?q='+command)









w = Label(gui, text='''Go-DoRK is a GUI based python tool for google dorking.
          It contains all main dorks that are used For advanced search.
          New dorks will be added In next versions. ** You can custom add your
          own Dork.  Happy Dorking!!!

          Note:Google may try rate-limiting your requests.
                Solve the given CAPTCHA and move on!


          ''')
w.grid(row=0,column=0, columnspan=2)





#target label
targetlabel=Label(gui,text="Enter Target Website:")
targetlabel.grid(row=1,column=1)

#target entry box
entry=Entry(gui,width=50,bg="light blue", borderwidth=3 )
entry.grid(row=2,column=1)
entry.insert(0,"www.example.com")





  
# label
ttk.Label(gui, text = "Select your dork:",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)
  
# Combobox creation
n = tk.StringVar()
prop = ttk.Combobox(gui, width = 27, textvariable = n)
  
# Adding combobox drop down list
prop['values'] = (' intitle', 
                          ' allintitle',
                          ' inurl',
                          ' allinurl',
                          ' intext',
                          ' allintext',
                          ' inanchor',
                          ' allinanchor')
                         
  
prop.grid(column = 1, row = 5)
prop.current()



#another combobox creation

n1 = tk.StringVar()
payload = ttk.Combobox(gui, width = 40, textvariable = n1)
  
# Adding combobox drop down list
payload['values'] = (' login', 
                          ' key',
                          ' password',
                          ' error',
                          ' redirect',
                          ' admin',
                          ' version',
                          ' dump',
                          ' mail',
                          ' db',
                          ' log',
                          ' dat',
                          ' bak',
                            'inc',
                           'reg' 
                           )
  
payload.grid(column = 2, row = 5)
payload.current()



mybutton=Button(gui,text="Submit",command=gettarget)
mybutton.grid(row=5,column=4)

























gui.mainloop()
