import os
os.system('clear')

fullName = 'Agustin Gonzalez'

###################################
# DATA TYPES
# Strings
# Numbers
# List
# Tuples
# Dictionaries
# Boolean
###################################

firstName = 'Agustin'
age = 42
names = ['john','bob',45,'Mary','guty']
months = ('Jan','Feb','March','Aprl','May','Jun','Jul','Aug')
Teams = {'Chicago':'Michael J','Lakers':'Shaq','Atlanta':'Dikembe M'}

for x in names:
	print(x)

print('#'*15)

for y in months:
	print(y)	


print(Teams['Chicago'])
print(Teams.values())
print(Teams.keys())

if names[2] > 50:
	pass
	print(names[2])
else:
	print('here')