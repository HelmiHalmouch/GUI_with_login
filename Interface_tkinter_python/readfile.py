import os 
list_of_files = os.listdir('user_file_liste')
print(list_of_files)



username1 = 'admin'
passeword = input('Please enter you passeword:')
file1 = open(username1, "r")

verify = file1.read().splitlines() 
#print(verify)

if passeword  in verify:
	print('Login success ')
else :
	print('No No ')
