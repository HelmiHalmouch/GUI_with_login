import os 
username1 = 'admin'
file1 = open(username1, "r")

verify = file1.read().splitlines() 
print(verify)