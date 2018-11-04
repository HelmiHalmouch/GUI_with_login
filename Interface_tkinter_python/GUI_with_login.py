'''Title :Graphical User Interface with Login
   Authors: GHANMI Helmi
   Date : 04 November 2018
   Description: Creat a Graphical User Interface (GUI) with login in Tikinter python 
'''
from tkinter import*

# def the fauntion fro the main screen 

def  main_acount_screen():
	
	#link the function of registration with the main interface 
	global main_screen

	#1-Create the GUI window, 2- Set the parameters size then thetitleof the GUI window 
	main_screen = Tk()
	main_screen.geometry("600x500")
	main_screen.title("Account Register&Login")

	Label(text="Choose Login Or Register", bg="red", width="300", height="2", font=("Calibri", 15)).pack() 
	Label(text="").pack()

	#creat a quit button 
	Button(main_screen, text='QUIT', command=main_screen.quit).pack(side=RIGHT)

	Button(text="Login", height="2", width="30",font=("Calibri", 13)).pack() 
	Label(text="").pack() 
	# add command=register in button widget
	Button(text="Register", height="2", width="30",font=("Calibri", 13), command=register).pack()


	#start the GUI 
	main_screen.mainloop()

'''Designing New Screen For Registration'''
def register():

	'''
	-The Toplevel widget work pretty much like Frame,
	-but it is displayed in a separate, top-level window. 
	-Such windows usually have title bars, borders, and other “window decorations”.
	-And in argument we have to pass global screen variable

	'''
	global username
	global password
	global username_entry
	global password_entry
	global register_screen

	register_screen=Toplevel(main_screen)
	register_screen.title('Register')
	register_screen.geometry('300x250')

	#set text variable 
	username = StringVar()
	password = StringVar()

	# Set label for user's instruction
	Label(register_screen, text="Please enter details below", bg="blue").pack()
	Label(register_screen, text="").pack()

	# Set username label
	username_lable = Label(register_screen, text="Username * ")
	username_lable.pack()

	# Set username entry
	# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
	username_entry = Entry(register_screen, textvariable=username)
	username_entry.pack()

	# Set password label
	password_lable = Label(register_screen, text="Password * ")
	password_lable.pack()

	# Set password entry
	password_entry = Entry(register_screen, textvariable=password, show='*')
	password_entry.pack()

	Label(register_screen, text="").pack()

	# Set register button
	#Button(register_screen, text="Register", width=10, height=1, bg="blue").pack()

	# add command = register 
	Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()

'''Assigning Functions To Register Button'''
	
def register_user():

	""" Now we have to implement event on register button. 
	It means, after filling the entries, as soon as the register button is pressed, 
	entries are saved in a file. So let’s see how to do it."""
 
	# get username and password
	username_info = username.get()
	password_info = password.get()
 
	# Open file in write mode
	file = open(username_info, "w")
 
	# write username and password information into file
	file.write(username_info + "\n")
	file.write(password_info)
	file.close()

	username_entry.delete(0, END)
	print(username_entry.delete(0, END))
	password_entry.delete(0, END)
 
	# set a label for showing success information on screen 
	Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

'''Designing New Screen For Login'''


#Try the GUI interface 

if __name__=='__main__':
	main_acount_screen()