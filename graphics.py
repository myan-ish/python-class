#Graphics

from tkinter import *

#click function
def click():
	ent_txt = name.get()
	e_val = e.get()
window = Tk()
window.title(" Budget Calculator")
window.configure(background="black")

#label
Label(window, text="Enter a file name:", bg="black", fg="white", font="none 12 bold").grid(row=1, column=0, sticky=W)

#text entry boxes
name = Entry(window, width=20, bg="white")
name.grid(row=1, column="3", sticky=W)
sum = 0
big=-1
dic=list()

#anoother label
Label(window, text="Enter your respective day's expense:", bg="black", fg="white", font="none 12 bold").grid(row=3, column=0, sticky=W)

#another entry plus add button
e = Entry(window, width=20, bg="white")
e.grid(row=3, column="3", sticky=W)

#add a submit button
Button(window, text="SUBMIT", width=6, command= click).grid(row=7,column=0,sticky="W")

#output box

#save data
