'''Title :Graphical User Interface with Login
   Authors: GHANMI Helmi
   Date : 04 November 2018
   Description: Creat a Graphical User Interface (GUI) with login in Tikinter python 
'''
from tkinter import*
import sys, os 

# def the fauntion fro the main screen 

def  main_acount_screen():
	
	#link the function of registration with the main interface 
	global main_screen

	#create folder to save the new id 
	directory  ='user_id_file_liste' 
	if not os.path.exists(directory):
		os.makedirs(directory)

	#1-Create the GUI window, 2- Set the parameters size then thetitleof the GUI window 
	main_screen = Tk()
	main_screen.geometry("600x500")
	main_screen.title("Account Register&Login")

	Label(text="Choose Login Or Register", bg="red", width="300", height="2", font=("Calibri", 15)).pack() 
	Label(text="").pack()

	#creat a quit button 
	Button(main_screen, text='QUIT', command=main_screen.quit).pack(side=RIGHT)

	#Button(text="Login", height="2", width="30",font=("Calibri", 13)).pack() 
	#Label(text="").pack() 
	# add command=register in button widget
	Button(text="Register", height="2", width="30",font=("Calibri", 13), command=register).pack()

	# add command = login 
	Button(text="Login", height="2", width="30",font=("Calibri", 13), command = login).pack()


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
	file = open('user_id_file_liste/'+username_info, "w")
 
	# write username and password information into file
	file.write(username_info + "\n")
	file.write(password_info)
	file.close()

	username_entry.delete(0, END)
	password_entry.delete(0, END)
 
	# set a label for showing success information on screen 
	Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

'''Designing New Screen For Login'''
# define login function
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

''' Define login verification function'''
'''def login_verification():
	print('working....')'''

def login_verify():

	#get username and password
    username1 = username_verify.get()
    password1 = password_verify.get()

    # this will delete the entry after login button is pressed
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    #The method listdir() returns a list containing the names of the entries in the directory given by path.
    list_of_files = os.listdir('user_id_file_liste')
    #print(list_of_files)

    #defining verification's conditions 
    if username1 in list_of_files:
    	# open the file in read mode
    	#read the file, 
    	#as splitlines() actually splits on the newline character,
    	#the newline character is not left hanging at the end of each line. if password1 in verify:
        file1 = open('user_id_file_liste/'+username1, "r")
        verify = file1.read().splitlines()

        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
def login_sucess():
	global login_success_screen   # make login_success_screen global
	login_success_screen = Toplevel(login_screen)
	login_success_screen.title("Success")
	login_success_screen.geometry("150x100")
	Label(login_success_screen, text="Login Success").pack()

	# create OK button
	Button(login_success_screen, text="OK", command=delete_login_success).pack()
	
def delete_login_success():
    login_success_screen.destroy()

#Designing Invalid Password Popup

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

# add function if username not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_user_not_found_screen():
	user_not_found_screen.destroy()

#Try the GUI interface 

if __name__=='__main__':
	main_acount_screen()