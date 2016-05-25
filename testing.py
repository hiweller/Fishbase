# packages
import math
import numpy as np
import matplotlib.pyplot as plt

# obligatory
print('Hello World, AGAIN, You Absolute Motherfucker')

# for loops
# for i in range(0,10): # outputs 0 to 9
# 	print(i)

# while loops
# x = 0
# guesses = 0
# while x != 5 and guesses < 3:
# 	x = int(input('Guess a number:'))

# 	if x != 5:
# 		print('WRONG')
# 		guesses = guesses + 1

# if x == 5:
# 	print('Correct')
# else:
# 	print('You were wrong three times! The penalty is hanging :)')


# poopwards!
def pythagoras(a,b):
	value = math.sqrt(a*a + b*b)
	print(value)

# lists!
c = [5,2,10,48,32,16,49,10,11,32,64,55,34,45,41,23,26,27,72,18]

# first element
c[0]

# last element
c[-1]

# plotting
x = range(10)
plt.plot(c)
show(c)

## TUPLES ##