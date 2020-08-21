from tkinter import *
from tkinter import messagebox
import sqlite3
import datetime

class Mpms:
	def function_register(login_name):
		login_namee = login_name
		register = Tk()
		register.title("Hospital Management System")
		register.resizable(0,0)
		register_window_width = 326
		register_window_height = 500

		register_screen_width = register.winfo_screenwidth()
		register_screen_height = register.winfo_screenheight()

		register_x = int(register_screen_width/2 - register_window_width/2)
		register_y = int(register_screen_height/2 - register_window_height/2)

		register.geometry("{}x{}+{}+{}".format(register_window_width,register_window_height,register_x,register_y))

		register_frame = LabelFrame(register, padx=20,pady=10)
		register_frame.grid(row=0, column=0, padx=10, pady=(10,10), columnspan=5)
		
		#Start Define Functions For Buttons
		def register_save(register_sex, register_companyy, register_department):
			register_con = sqlite3.connect("mpms.db")
			register_cursor = register_con.cursor()
			date = datetime.datetime.now()
			if register_sex == 1:
				register_sexx = "Male"
			else:
				register_sexx = "Female"
			if register_id_num.get() != '' and register_name.get() != '' and register_companyy != 'Select Department' and register_department != "No Jobs From This Company" and register_department != 'Select Department' and register_department != 'Enrolling Time Passed' and register_department != 'Enrolling Time Passed or Still not Started':
				nic = str(register_id_num.get())
				curr_year = date.strftime("%Y")
				if(len(nic) == 10 or len(nic) == 12):
					if(len(nic) == 12):
						x = re.findall("[a-zA-Z]",nic)
						if x == []:
							year = int(nic[0] + nic[1] + nic[2] + nic[3])
							if (int(curr_year) - year) >= 18:
								register_cursor.execute("SELECT workers_count,enrolled_workers FROM working_details WHERE company_name = :c and department_name = :d",{'c':register_companyy,'d':register_department})
								result = register_cursor.fetchall()
								if result[0][1] <= result[0][0]:
									e = result[0][1] + 1
									register_cursor.execute("UPDATE working_details SET enrolled_workers = :e WHERE company_name = :c and department_name = :d",{'e':e,'c':register_companyy,'d':register_department})
									register_cursor.execute("SELECT id FROM department WHERE company_name = :c and department_name = :d",{'c':register_companyy,'d':register_department})
									com_id = register_cursor.fetchall()
									register_cursor.execute("INSERT INTO workers_data (creation_date,nic,name,cdid,pNumber,age,address,sex) VALUES (:ndate,:id_num,:name,:cdid,:contact,:age,:address,:sex)",
											{
													'ndate' : date,
													'id_num' : register_id_num.get(),
													'name' : register_name.get(),
													'cdid' : com_id[0][0],
													'contact' : register_contact.get(),
													'age' : register_age.get(),
													'address' : register_address.get(),
													'sex' : register_sexx
											})
									messagebox.showinfo("Success","Saved Data Successfully.")
									register_id_num.delete(0, END)
									register_name.delete(0, END)
									register_contact.delete(0, END)
									register_age.delete(0, END)
									register_address.delete(0, END)
									register_company.set("Select Company")
									Button(register_frame, text="Save", width=14,state=DISABLED).grid(row=8, column=0, pady=(8,0))
								else:
									messagebox.showinfo("Information", "No Workers Needed.")
									register_company.set("Select Company")
							else:
								messagebox.showwarning("Warning","Age Below 18")
								register_id_num.delete(0, END)
								register_name.delete(0, END)
								register_contact.delete(0, END)
								register_age.delete(0, END)
								register_address.delete(0, END)
								register_company.set("Select Company")
						else:
							messagebox.showwarning("Warning","ID Number is not Valid")
							register_id_num.delete(0, END)
					else:
						if nic[9] == 'v':
							year = int("19" + nic[0] + nic[1])
							if (int(curr_year) - year) >= 18:
								register_cursor.execute("SELECT workers_count,enrolled_workers FROM working_details WHERE company_name = :c and department_name = :d",{'c':register_companyy,'d':register_department})
								result = register_cursor.fetchall()
								if result[0][1] <= result[0][0]:
									e = result[0][1] + 1
									register_cursor.execute("UPDATE working_details SET enrolled_workers = :e WHERE company_name = :c and department_name = :d",{'e':e,'c':register_companyy,'d':register_department})
									register_cursor.execute("SELECT id FROM department WHERE company_name = :c and department_name = :d",{'c':register_companyy,'d':register_department})
									com_id = register_cursor.fetchall()
									register_cursor.execute("INSERT INTO workers_data (creation_date,nic,name,cdid,pNumber,age,address,sex) VALUES (:ndate,:id_num,:name,:cdid,:contact,:age,:address,:sex)",
											{
													'ndate' : date,
													'id_num' : register_id_num.get(),
													'name' : register_name.get(),
													'cdid' : com_id[0][0],
													'contact' : register_contact.get(),
													'age' : register_age.get(),
													'address' : register_address.get(),
													'sex' : register_sexx
											})
									messagebox.showinfo("Success","Saved Data Successfully.")
									register_id_num.delete(0, END)
									register_name.delete(0, END)
									register_contact.delete(0, END)
									register_age.delete(0, END)
									register_address.delete(0, END)
									register_company.set("Select Company")
									Button(register_frame, text="Save", width=14,state=DISABLED).grid(row=8, column=0, pady=(8,0))
								else:
									messagebox.showinfo("Information", "No Workers Needed.")
									register_company.set("Select Company")
							else:
								messagebox.showwarning("Warning","Age Below 18")
								register_id_num.delete(0, END)
								register_name.delete(0, END)
								register_contact.delete(0, END)
								register_age.delete(0, END)
								register_address.delete(0, END)
								register_company.set("Select Company")
						else:
							messagebox.showwarning("Warning","ID Number is not Valid")
							register_id_num.delete(0, END)
				else:
					messagebox.showwarning("Warning","ID Number is Not Valid")
					register_id_num.delete(0, END)
			else:
				messagebox.showwarning("Warning","Required Fields are Empty")

			register_con.commit()
			register_con.close()

		def register_delete():
			register_id_num.delete(0, END)
			register_name.delete(0, END)
			register_contact.delete(0, END)
			register_age.delete(0, END)
			register_address.delete(0, END)


		def register_select_dep(self):
			register_con = sqlite3.connect('mpms.db')
			register_cursor = register_con.cursor()
			today = datetime.datetime.now().date()
			yesterday = today - datetime.timedelta(days=1)

			ndate = datetime.datetime.now()

			if str(ndate.strftime("%p")) == "AM":
				if int(ndate.strftime("%I")) < 8:
					register_cursor.execute("SELECT department_name,workers_count,enrolled_workers FROM working_details WHERE company_name = :x and creation_date = :yesterday",{'x':register_company.get(),'yesterday':yesterday})
					register_dep_names = []
					register_result = register_cursor.fetchall()
					for register_x in register_result:
						if register_x[2] < register_x[1]:
							register_dep_names.append(register_x[0])

					if register_dep_names == []:
						register_dep_names = ["No Jobs From This Company"]
				else:
					register_dep_names = ["Enrolling Time Passed"]
			elif str(ndate.strftime("%p")) == "PM":
				register_dep_names = ["Enrolling Time Passed or Still not Started"]

			register_con.commit()
			register_con.close()

			register_depart = StringVar()
			register_depart.set("Select Department")
			register_dep = OptionMenu(register_frame, register_depart, *register_dep_names)
			register_dep.grid(row=3,column=1, padx=(15,0), pady=(8,0), columnspan=4)
			register_dep.config(width=16)
			Button(register_frame, text="Save", width=14, command=lambda:register_save(register_radio.get(), register_company.get(), register_depart.get())).grid(row=8, column=0, pady=(8,0))
		#register_select_dep

		def select_dep_for_details(self):
			con = sqlite3.connect('mpms.db')
			cursor = con.cursor()
			cursor.execute("SELECT department_name FROM department WHERE company_name = :x",{'x':company.get()})
			dep_names = []
			result = cursor.fetchall()
			for x in result:
				dep_names.append(x[0])
			con.commit()
			con.close()

			if dep_names == []:
				dep_names = [""]

			department = StringVar()
			department.set("Select Department")
			d_option = OptionMenu(register, department, *dep_names)
			d_option.grid(row=2, column=1, padx=(20,0))
			d_option.config(width=16)

			Button(register, text="Show Details",width=35, command=lambda:show(company.get(),department.get())).grid(row=3, column=0, pady=(5,0),columnspan=2,padx=(28,0))
		#select_dep_for_details

		def show(companyy,department):
			if department != 'Select Department':
				con = sqlite3.connect('mpms.db')
				cursor = con.cursor()
				ndate = datetime.datetime.now()
				today = datetime.datetime.now().date()
				if str(ndate.strftime("%p")) == "AM":
					day = today - datetime.timedelta(days=1)
				elif str(ndate.strftime("%p")) == "PM":
					day = datetime.datetime.now().date()
				cursor.execute("SELECT company_name,department_name,payment,workers_count,enrolled_workers FROM working_details WHERE company_name = :c and department_name = :d and creation_date = :ndate",{'c':companyy,'d':department, 'ndate':day})
				result_list = cursor.fetchall()
				if len(result_list) > 0:
					messagebox.showinfo("Woking Details","Company : {}\nDepartment : {}\nPayment : {}\nWorkers Count : {}\nEnrolled Workers : {}".format(result_list[0][0],result_list[0][1],result_list[0][2],result_list[0][3],result_list[0][4]))
				else:
					messagebox.showwarning("Warning","No Details")
					
				con.commit()
				con.close()

				Button(register, text="Show Details",width=35,state=DISABLED).grid(row=3, column=0, pady=(5,0) ,columnspan=2,padx=(28,0))
			else:
				messagebox.showwarning("Warning","Required Fields are Empty")
		#show
		#menu Functions
		def register_add_com():
			register.destroy()
			company = Tk()
			company.title("Add Company")
			company.resizable(0,0)

			#Add Function to Close Button "X"
			def doSomething():
				company.destroy()
				Mpms.function_register(login_namee)
			company.protocol('WM_DELETE_WINDOW',doSomething)

			window_width = 315
			window_height = 170

			screen_width = company.winfo_screenwidth()
			screen_height = company.winfo_screenheight()

			x = int(screen_width/2 - window_width/2)
			y = int(screen_height/2 - window_height/2)

			company.geometry("{}x{}+{}+{}".format(window_width,window_height,x,y))

			#Start Define Functions For Buttons
			def close():
				company.destroy()
				Mpms.function_register(login_namee)
				
			def add():
				dp_name = d_name.get()
				dpname_list = dp_name.split(',')
				#Label(company,text=dpname_list[0]).grid(row=2, column=0)

				if c_name.get() != '' and d_name.get() != '':	
					con = sqlite3.connect('mpms.db')
					cursor = con.cursor()
					date = datetime.datetime.now()
					datetime_list = str(date).split(' ')		
					cursor.execute("INSERT INTO company (company_name,date_of_add) VALUES (:cName,:date_time)",{'cName':c_name.get(),'date_time':datetime_list[0] + ' ' + datetime_list[1]})
					d = d_name.get()
					d_name_list = d.strip().split(',')
					for i in d_name_list:
						if i != '':
							cursor.execute("INSERT INTO department (company_name,department_name,creation_date) VALUES (:cName,:dName,:date_time)",{'cName':c_name.get(),'dName':i,'date_time':datetime_list[0] + ' ' + datetime_list[1]})
					messagebox.showinfo("Success","Saved Data Successfully.")
					c_name.delete(0, END)
					d_name.delete(0, END)
					con.commit()
					con.close()
				else:
					messagebox.showwarning("Warning","Required Fields are Empty")


			frame = LabelFrame(company, padx=20,pady=10)
			frame.grid(row=0, column=0, padx=10, pady=(10,5), columnspan=5)

			Label(frame, text = "Company Name", anchor=W).grid(row=0, column=0,sticky=E+W)
			c_name = Entry(frame, borderwidth=1)
			c_name.grid(row=0, column=1, padx=(10,0))

			Label(frame, text = "Department Name(s)\nSep by    ' ,'", anchor=W).grid(row=1, column=0, pady=(10,10), sticky=E+W)
			d_name = Entry(frame, borderwidth=1)
			d_name.grid(row=1, column=1, padx=(10,0), pady=(10,10))
			
			Button(frame, text="Add to Database",width=15,command=add).grid(row=2, column=0)
			Button(frame, text="close",width=15,command=close).grid(row=2, column=1)
			Label(company, text="Software by Ranidu Harshana", width=40, anchor=CENTER).grid(row=1, column=0, columnspan=2, padx=(0,10))

			company.mainloop()
		#register_add_com

		def register_add_dep():
			register.destroy()
			add_dep = Tk()
			add_dep.title("Add Department")
			add_dep.resizable(0,0)

			#Add Function to Close Button "X"
			def doSomething():
				add_dep.destroy()
				Mpms.function_register(login_namee)
			add_dep.protocol('WM_DELETE_WINDOW',doSomething)

			add_dep_window_width = 325
			add_dep_window_height = 210

			add_dep_screen_width = add_dep.winfo_screenwidth()
			add_dep_screen_height = add_dep.winfo_screenheight()

			add_dep_x = int(add_dep_screen_width/2 - add_dep_window_width/2)
			add_dep_y = int(add_dep_screen_height/2 - add_dep_window_height/2)

			add_dep.geometry("{}x{}+{}+{}".format(add_dep_window_width,add_dep_window_height,add_dep_x,add_dep_y))
			
			add_dep_frame = LabelFrame(add_dep, padx=20,pady=10)
			add_dep_frame.grid(row=0, column=0, padx=10, pady=(10,10), columnspan=2)

			def add_department():
				con = sqlite3.connect('mpms.db')
				cursor = con.cursor()
				if add_dep_company.get() != "Select Company" and add_dep_company.get() != "" and  add_dep_entry.get() != '':
					cursor.execute("SELECT department_name FROM department WHERE company_name = :c",{'c':add_dep_company.get()})

					result = cursor.fetchall()
					date = datetime.datetime.now().date()
					new_dept = add_dep_entry.get()
					new_dept_list = new_dept.split(',')
					already_list = []
					for x in result:
						if x[0] in new_dept_list:
							already_list.append(x[0])		
					if already_list == []:
						if new_dept != '':
							for dd in new_dept_list:
								cursor.execute("INSERT INTO department (company_name,department_name,creation_date) VALUES (:c,:d,:ndate)",{'c':add_dep_company.get(),'d':dd,'ndate':date})
							messagebox.showinfo("Success", "Data Insereted Successfully.")
							add_dep_entry.delete(0,END)
							add_dep_company.set("Select Company")
						else:
							messagebox.showwarning("Warning","Required Fields Are Empty.")
					else:
						s = ''
						for ii in already_list:
							s = s + " " + str(ii)
						messagebox.showwarning("Warning", "Department " + s + ", is Already Exist in the Database")
				else:
					messagebox.showwarning("Warning", "Required Fields Are Empty.")
				con.commit()
				con.close()
			#add_department

			def close():
				add_dep.destroy()
				Mpms.function_register(login_namee)
			#close

			Label(add_dep_frame,text="Company Name", anchor=W).grid(row=0,column=0,sticky=E+W,pady=(10,0))

			add_dep_company = StringVar()
			add_dep_company.set("Select Company")
			add_dep_company_list = []

			con = sqlite3.connect('mpms.db')
			cursor = con.cursor()

			cursor.execute("SELECT company_name FROM company")
			result = cursor.fetchall()
			for iterr in result:
				add_dep_company_list.append(iterr[0])
			con.commit()
			con.close()
			#print(add_dep_company_list)
			add_dep_com = OptionMenu(add_dep_frame, add_dep_company, *add_dep_company_list)
			add_dep_com.grid(row=0, column=1,padx=(12,0),pady=(10,0))
			add_dep_com.config(width=16)

			Label(add_dep_frame, text="Department Name", anchor=W).grid(row=1,column=0,sticky=E+W,pady=(10,0))
			add_dep_entry = Entry(add_dep_frame,borderwidth=1,width=22)
			add_dep_entry.grid(row=1, column=1,padx=(12,0),pady=(10,0))

			Button(add_dep_frame,text="Add Department",width=14,command=add_department).grid(row=2, column=0,pady=(8,0))
			Button(add_dep_frame,text="Close",width=15, command=close).grid(row=2, column=1,pady=(8,0))
			Label(add_dep, text="Software by Ranidu Harshana", width=40, anchor=CENTER).grid(row=1, column=0, columnspan=2,pady=(5,0))

			add_dep.mainloop()     
		#register_add_dep
			
		def register_add_working_details():
			register.destroy()
			window_add_working_details = Tk()
			window_add_working_details.title("Add window_add_working_details")
			window_add_working_details.resizable(0,0)

			#Add Function to Close Button "X"
			def doSomething():
				window_add_working_details.destroy()
				Mpms.function_register(login_namee)
			window_add_working_details.protocol('WM_DELETE_WINDOW',doSomething)

			window_width = 335
			window_height = 232

			screen_width = window_add_working_details.winfo_screenwidth()
			screen_height = window_add_working_details.winfo_screenheight()

			x = int(screen_width/2 - window_width/2)
			y = int(screen_height/2 - window_height/2)

			window_add_working_details.geometry("{}x{}+{}+{}".format(window_width,window_height,x,y))

			frame = LabelFrame(window_add_working_details, padx=20,pady=10)
			frame.grid(row=0, column=0, padx=10, pady=(10,5), columnspan=5)

			#Start Define Functions For Buttons
			def close():
				window_add_working_details.destroy()
				Mpms.function_register(login_namee)

			def select_dep(self):
				con = sqlite3.connect('mpms.db')
				cursor = con.cursor()
				cursor.execute("SELECT department_name FROM department WHERE company_name = :x",{'x':company.get()})
				dep_names = []
				result = cursor.fetchall()
				ndate = datetime.datetime.now().date()
				#print(ndate)
				#ndate = date.strftime('%x')
				for x in result:
					cursor.execute("SELECT workers_count FROM working_details WHERE company_name = :c and department_name = :d and creation_date = :ndate",{'c':company.get(),'d':x[0],'ndate':ndate})
					result1 = cursor.fetchall()
					if result1 == []:
						dep_names.append(x[0])
				con.commit()
				con.close()

				if dep_names == []:
					dep_names = ["Already Added Working Details"]

				depart = StringVar()
				depart.set("Select Department")
				dep = OptionMenu(frame, depart, *dep_names)
				dep.grid(row=1,column=1, padx=(15,0), pady=(8,0), columnspan=4)
				dep.config(width=16)
				Button(frame, text="Save",width=15, command=lambda:Save(company.get(),depart.get())).grid(row=4, column=0, pady=(5,0))
				Button(frame, text="Close",width=15,command=close).grid(row=4, column=1, pady=(5,0))

			def Save(companyy,department):
				if department != 'Already Added Working Details' and department != 'Select Department' and payment.get() != '' and workers_count.get() != '':
					con = sqlite3.connect('mpms.db')
					cursor = con.cursor()
					ndate = datetime.datetime.now().date()
					#ndate = date.strftime("%x")
					cursor.execute("INSERT INTO working_details (company_name,department_name,payment,workers_count,creation_date) VALUES (:c,:d,:p,:w,:ndate)",{'c':companyy,'d':department, 'p':payment.get(), 'w':workers_count.get(), 'ndate': ndate})
					con.commit()
					con.close()

					messagebox.showinfo("Success","Saved Data Successfully.")
					payment.delete(0, END)
					workers_count.delete(0, END)

					Button(frame, text="Save",width=15,state=DISABLED).grid(row=4, column=0, pady=(5,0))
					Button(frame, text="Close",width=15, command=close).grid(row=4, column=1, pady=(5,0))
				else:
					messagebox.showwarning("Warning","Required Fields are Empty")
		
			#Label and Dropdown for Company Name
			Label(frame, text="Company Name", anchor=W).grid(row=0, column=0, sticky=W+E, pady=(8,0))

			#get company names from databse
			company = StringVar()
			company.set("Select Company")
			con = sqlite3.connect('mpms.db')
			cursor = con.cursor()
			company_names = []
			cursor.execute("SELECT company_name FROM company")
			result = cursor.fetchall()
			for x in result:
				company_names.append(x[0])
			con.commit()
			con.close()

			if company_names== []:
				company_names = ["No Companies Added"]

			com_name = OptionMenu(frame, company, *company_names, command=select_dep)
			com_name.grid(row=0,column=1, padx=(15,0), pady=(8,0), columnspan=4)
			com_name.config(width=16)

			#Label and Dropdown for Department
			Label(frame, text="Department", anchor=W).grid(row=1, column=0, sticky=W+E, pady=(8,0))

			depart = StringVar()
			depart.set("Select Department")
			dep = OptionMenu(frame, depart, "Select Company First")
			dep.grid(row=1,column=1, padx=(15,0), pady=(8,0))
			dep.config(width=16)

			Label(frame, text="Workers Count", anchor=W).grid(row=2, column=0, sticky=W+E, pady=(8,0))
			workers_count = Entry(frame, width=22)
			workers_count.grid(row=2, column=1, padx=(15,0), pady=(8,0))

			Label(frame, text="payment(Rs.)", anchor=W).grid(row=3, column=0, sticky=W+E, pady=(8,0))
			payment = Entry(frame, width=22)
			payment.grid(row=3, column=1, padx=(15,0), pady=(8,0))

			Button(frame, text="Save",width=15,state=DISABLED).grid(row=4, column=0, pady=(5,0))
			Button(frame, text="Close",width=15,command=close).grid(row=4, column=1, pady=(5,0))

			Label(window_add_working_details, text="Software by Ranidu Harshana", width=40, anchor=CENTER).grid(row=1, column=0, columnspan=5, padx=(0,10))

			window_add_working_details.mainloop()
		#register_add_working_details
		def pay_salary():
			pay = Tk()
			pay.title("Pay Salary")
			pay.resizable(0,0)
			pay_window_width = 350
			pay_window_height = 250

			pay_screen_width = pay.winfo_screenwidth()
			pay_screen_height = pay.winfo_screenheight()

			pay_x = int(pay_screen_width/2 - pay_window_width/2) + 345
			pay_y = int(pay_screen_height/2 - pay_window_height/2) - 30

			pay.geometry("{}x{}+{}+{}".format(pay_window_width,pay_window_height,pay_x,pay_y))

			frame = LabelFrame(pay, padx=20,pady=10)
			frame.grid(row=0, column=0, padx=10, pady=(10,5), columnspan=2) 

			def register_showRecord(idno = ""):
				if idno != "":
					con = sqlite3.connect('mpms.db')
					cursor = con.cursor()
					ndate = datetime.datetime.now().date()

					cursor.execute("SELECT creation_date,name,cdid FROM workers_data WHERE nic = :nic",{'nic':idno})
					result = cursor.fetchall()
					if result != []:
						datee = str(result[0][0]).split(" ")

					if result != [] and str(ndate) == str(datee[0]):
						cursor.execute("SELECT payment FROM working_details WHERE id = :cdid",{'cdid':result[0][2]})
						result1 = cursor.fetchall()

						Label(frame, text=result[0][1], fg='blue', width=40).grid(row=2, column=0, columnspan=2)
						Label(frame, text=result[0][0], fg='blue', width=40).grid(row=3, column=0, columnspan=2)
						Label(frame, text=result1[0][0], fg='blue', width=40).grid(row=4, column=0, columnspan=2)
						Button(frame, text="Salary Paied",width=40,command=lambda:pay_sal(register_show_id.get(),datee[0])).grid(row=5, column=0, columnspan=2, pady=(5,0)) 
					else:
						messagebox.showwarning("Warning", "ID Number Is Not in the Database")
						register_show_id.delete(0,END)
					con.commit()
					con.close()
				else:
					messagebox.showwarning("Warning","Enter ID Number")
			#register_showRecord
	
			def pay_sal(idno,id_added_date):
				if idno != "":
					#print(id_added_date)
					ndate = datetime.datetime.now().date()
					#print(ndate)
					if str(ndate) == str(id_added_date):
						date = datetime.datetime.now()
						ampm = date.strftime("%p")
						h = int(date.strftime("%I"))
						if ampm == "PM":
							if h >= 6:
								con = sqlite3.connect('mpms.db')
								cursor = con.cursor()
								cursor.execute("SELECT payment FROM workers_data WHERE nic = :nic",{'nic':idno})
								result2 = cursor.fetchall()
								if result2[0][0] == 'Not Paied':
									date = datetime.datetime.now()
									cursor.execute("UPDATE workers_data SET payment = 'Paied',paied_time = :t WHERE nic = :nic",{'t':date,'nic':idno})
									messagebox.showinfo("Success","Salary Paied.")
									register_show_id.delete(0,END)
									Label(frame, width=40).grid(row=2, column=0, columnspan=2)
									Label(frame, width=40).grid(row=3, column=0, columnspan=2)
									Label(frame, width=40).grid(row=4, column=0, columnspan=2)
									Button(frame, text="Salary Paied",width=40,state=DISABLED).grid(row=5, column=0, columnspan=2, pady=(5,0)) 
								else:
									messagebox.showwarning("Warning","Salary Has Already Paied")
									register_show_id.delete(0,END)
									Label(frame, width=40).grid(row=2, column=0, columnspan=2)
									Label(frame, width=40).grid(row=3, column=0, columnspan=2)
									Label(frame, width=40).grid(row=4, column=0, columnspan=2)
									Button(frame, text="Salary Paied",width=40,state=DISABLED).grid(row=5, column=0, columnspan=2, pady=(5,0)) 
								con.commit()
								con.close()
								Button(frame, text="Salary Paied",width=40,state=DISABLED).grid(row=5, column=0, columnspan=2, pady=(5,0)) 
							else:
								messagebox.showwarning("Warning","It is not the time to Pay the Salary")
								Button(frame, text="Salary Paied",width=40,state=DISABLED).grid(row=5, column=0, columnspan=2, pady=(5,0)) 
								register_show_id.delete(0,END)
								Label(frame, width=40).grid(row=2, column=0, columnspan=2)
								Label(frame, width=40).grid(row=3, column=0, columnspan=2)
								Label(frame, width=40).grid(row=4, column=0, columnspan=2)
						else:
							messagebox.showwarning("Warning","It is not the time to Pay the Salary")
							Button(frame, text="Salary Paied",width=40,state=DISABLED).grid(row=5, column=0, columnspan=2, pady=(5,0)) 
							register_show_id.delete(0,END)
							Label(frame, width=40).grid(row=2, column=0, columnspan=2)
							Label(frame, width=40).grid(row=3, column=0, columnspan=2)
							Label(frame, width=40).grid(row=4, column=0, columnspan=2)
					else:
						messagebox.showwarning("Warning", "ID Number Is Not in the Database")
						register_show_id.delete(0,END)
						Label(frame, width=40).grid(row=2, column=0, columnspan=2)
						Label(frame, width=40).grid(row=3, column=0, columnspan=2)
						Label(frame, width=40).grid(row=4, column=0, columnspan=2)
				else:
					Button(frame, text="Salary Paied",width=40,state=DISABLED).grid(row=5, column=0, columnspan=2, pady=(5,0)) 
					messagebox.showwarning("Warning","Enter ID Number")
			#pay_sal
			
			Label(frame,text="Enter ID", anchor=W).grid(row=0, column=0, sticky=W+E, padx=(10,0))
			register_show_id = Entry(frame, borderwidth=1)
			register_show_id.grid(row=0, column=1, padx=(14,0))

			#Buttons
			Button(frame, text="Show Record",width=40, command=lambda:register_showRecord(register_show_id.get())).grid(row=1, column=0, columnspan=2, pady=(5,0))

			Label(frame, text="No Record Selected.", fg='blue', width=40).grid(row=2, column=0, columnspan=2)
			
			Button(frame, text="Salary Paied",width=40,state=DISABLED).grid(row=5, column=0, columnspan=2, pady=(5,0)) 

			Label(pay, text="Software by Ranidu Harshana", width=40, anchor=CENTER).grid(row=6, column=0, columnspan=2,pady=(10,0))

		#Define Menus
		register_menu = Menu(register)
		register.config(menu = register_menu)
		#Construct Menu
		register_account_menu = Menu(register_menu)
		register_menu.add_cascade(label = "Account", menu = register_account_menu)
		register_account_menu.add_command(label="Logged As " + login_name)
		register_account_menu.add_command(label="Logout", command=register.destroy)

		register_add_menu = Menu(register_menu)
		register_menu.add_cascade(label = "Add" ,menu = register_add_menu)
		register_add_menu.add_command(label="Add Company", command=register_add_com)
		register_add_menu.add_command(label="Add Department", command=register_add_dep)

		register_pay_salary = Menu(register_menu)
		register_menu.add_cascade(label="Working Details", menu=register_pay_salary)
		register_pay_salary.add_command(label="Add Working Details", command=register_add_working_details)
		register_pay_salary.add_command(label="Pay Salary", command=pay_salary)

		#Label and Textfield for ID Number
		Label(register_frame,  text="ID Number(*)", anchor=W).grid(row=0, column=0, sticky=E+W)
		register_id_num = Entry(register_frame, borderwidth=1, width=22)
		register_id_num.grid(row=0,column=1, padx=(15,0), pady=(8,0), columnspan=4)

		#Label and Textfield for Name
		Label(register_frame, text="Name(*)", anchor=W).grid(row=1, column=0, sticky=W+E, pady=(8,0))
		register_name = Entry(register_frame, borderwidth=1, width=22)
		register_name.grid(row=1,column=1, padx=(15,0), pady=(8,0), columnspan=4)

		#Label and Dropdown for Company Name
		Label(register_frame, text="Company Name(*)", anchor=W).grid(row=2, column=0, sticky=W+E, pady=(8,0))
		#get company names from databse
		register_company = StringVar()
		register_company.set("Select Company")
		register_con = sqlite3.connect('mpms.db')
		register_cursor = register_con.cursor()
		register_company_names = []
		register_cursor.execute("SELECT company_name FROM company")
		register_result = register_cursor.fetchall()
		for register_x in register_result:
			register_company_names.append(register_x[0])
		register_con.commit()
		register_con.close()

		if register_company_names== []:
			register_company_names = ["No Companies Added"]

		register_com_name = OptionMenu(register_frame, register_company, *register_company_names, command=register_select_dep)
		register_com_name.grid(row=2,column=1, padx=(15,0), pady=(8,0), columnspan=4)
		register_com_name.config(width=16)

		#Label and Dropdown for Department
		Label(register_frame, text="Department(*)", anchor=W).grid(row=3, column=0, sticky=W+E, pady=(8,0))

		register_depart = StringVar()
		register_depart.set("Select Department")
		register_dep = OptionMenu(register_frame, register_depart, "Select Company First")
		register_dep.grid(row=3,column=1, padx=(15,0), pady=(8,0), columnspan=4)
		register_dep.config(width=16)


		#Label and Textfield for Contact Number
		Label(register_frame, text="Contact Number", anchor=W).grid(row=4, column=0, sticky=W+E, pady=(8,0))
		register_contact = Entry(register_frame, borderwidth=1, width=22)
		register_contact.grid(row=4,column=1, padx=(15,0), pady=(8,0), columnspan=4)

		#Label and Textfield for Age
		Label(register_frame, text="Age", anchor=W).grid(row=5, column=0, sticky=W+E, pady=(8,0))
		register_age = Entry(register_frame, borderwidth=1, width=22)
		register_age.grid(row=5,column=1, padx=(15,0), pady=(8,0), columnspan=4)

		#Label and Textfield for Address
		Label(register_frame, text="Address", anchor=W).grid(row=6, column=0, sticky=W+E, pady=(8,0))
		register_address = Entry(register_frame, borderwidth=1, width=22)
		register_address.grid(row=6,column=1, padx=(15,0), pady=(8,0), columnspan=4)

		#Label and Radio Buttons for sex
		Label(register_frame, text="Sex", anchor=W).grid(row=7, column=0, sticky=W+E, pady=(8,0))

		#dInitilize Radio Buttons
		register_radio = IntVar()

		Radiobutton(register_frame,text="Female", variable=register_radio, value=0).grid(row=7, column=2, pady=(8,0))
		Radiobutton(register_frame,text="Male", variable=register_radio, value=1).grid(row=7, column=4, pady=(8,0))

		Button(register_frame, text="Save", width=14,state=DISABLED).grid(row=8, column=0, pady=(8,0))
		Button(register_frame, text="Delete", width=16, command=register_delete).grid(row=8, column=1, padx=(8,0), pady=(8,0), columnspan=4)

		Label(register, text="Company Name", anchor=W).grid(row=1, column=0, sticky=W+E, pady=(8,0),padx=(30,0))
		register_con = sqlite3.connect('mpms.db')
		register_cursor = register_con.cursor()
		company_names = []
		register_cursor.execute("SELECT company_name FROM company")
		register_result = register_cursor.fetchall()
		for register_x in register_result:
			company_names.append(register_x[0])
		register_con.commit()
		register_con.close()

		if company_names == []:
			company_names = ["No Companies Added"]

		company = StringVar()
		company.set("Select Company")
		c_option = OptionMenu(register, company, *company_names, command=select_dep_for_details)
		c_option.grid(row=1, column=1, padx=(20,0))
		c_option.config(width=16)

		Label(register, text="Department", anchor=W).grid(row=2, column=0, sticky=W+E, pady=(8,0),padx=(30,0))
		department = StringVar()
		department.set("Select Department")
		d_option = OptionMenu(register, department, "Select Contry First")
		d_option.grid(row=2, column=1, padx=(20,0))
		d_option.config(width=16)

		Button(register, text="Show Details",width=35,state=DISABLED).grid(row=3, column=0, pady=(5,0),columnspan=2,padx=(28,0))

		Label(register, text="Software by Ranidu Harshana", width=40, anchor=CENTER).grid(row=4, column=0, columnspan=2,pady=(10,0))

		register.mainloop()

#Mpms.function_register()