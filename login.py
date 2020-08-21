from tkinter import *
from PIL import ImageTk, Image
from mpms import Mpms
from tkinter import messagebox
import sqlite3

window = Tk()
window.title("Login")
window.resizable(0,0)

window_width = 270
window_height = 340

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width,window_height,x_cordinate,y_cordinate))

#Start Define Functions For Buttons
def login():
	#databse connection
	con = sqlite3.connect("mpms_login.db")
	cursor = con.cursor()

	cursor.execute("SELECT id,username,password FROM admin WHERE username = :usrname",{'usrname':username.get()})
	result = cursor.fetchall()
	if len(result) > 0:
		for x in result:
			id = x[0]
			usrnme = x[1]
			pword = x[2]

		status = 1
		if pswrd.get() == pword:
			window.destroy()
			cursor.execute("INSERT INTO admin_curr_status (status,aid) VALUES (:status, :id)",{'status':status, 'id':id})
			Mpms.function_register(usrnme)
		else:
			username.delete(0, END)
			pswrd.delete(0, END)
			messagebox.showwarning("Warning","Wrong Username or Password")
	else:
		username.delete(0, END)
		pswrd.delete(0, END)
		messagebox.showwarning("warning","Username or Password is Wrong")

	con.commit()
	con.close()

def cancel():
	window.destroy()

#End Define Functions For Buttons

#frame
frame = LabelFrame(window, padx=20,pady=10)
frame.pack(pady=8)

#HEADING
Label(frame, text="WELCOME TO\n MANPOWER MANAGEMENT SYSTEM").grid(row=0, column=0,columnspan=2, pady=10)

ste = ImageTk.PhotoImage(Image.open("img/manPower.jpg"))
Label(frame, image=ste).grid(row=1, column=0, columnspan=2, padx=0)

#Label and Textfield for username
Label(frame, text="USERNAME").grid(row=2, column=0, pady=3)
username = Entry(frame, borderwidth=2)
username.grid(row=2, column=1, pady=3)

#Label and Textfield for password
Label(frame, text="PASSWORD").grid(row=3, column=0, pady=3)
pswrd = Entry(frame,show='*', borderwidth=2)
pswrd.grid(row=3, column=1, pady=3)

#buttons
Button(frame, text="LOGIN",width=27, command=login).grid(row=4, column=0, columnspan=2,pady=3)
Button(frame, text="CANCEL",width=27, command=cancel).grid(row=5, column=0, columnspan=2)

window.mainloop()