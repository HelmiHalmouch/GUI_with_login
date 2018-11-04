'''Title :Graphical User Interface with Login
   Authors: GHANMI Helmi
   Date : 04 November 2018
   Description: Creat a Graphical User Interface (GUI) with login in Tikinter python 
'''
from tkinter import*

# def the fauntion fro the main screen 

def  main_acount_screen():

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

	Button(text="Register", height="2", width="30",font=("Calibri", 13)).pack()

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
	register_screen=Toplevel(main_screen)
	register_screen.title('Register')
	register_screen.geometry('600x500')

	#set text variable 
	username = SrringVar()
	password = StringVar()


#Try the GUI interface 

if __name__=='__main__':
	main_acount_screen()