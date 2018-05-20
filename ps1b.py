# Problem Set 1b
# Name: Uzair Hasan
# Collaborators: None
# Date & Time: May 17, 2018, 4:02pm - 4:15pm (Approx)

##Objective of this code is find the total of all prime numbers logged divided by choosen number
import math
from math import *

place = 3 #which number we are evaluating 
total = 1.0
n = int(input('n value: '))
while (place!=n+1 and place-1!=n+1): #keep checking until we make it 1 after the choosen value
    for x in range(3,place):
        if(place%x==0): #if we get no remainder (even number)
            place +=2 #increment place by 2 (skipping even numbers)
            break #stop loop and skip else block
    else: #loop didnt break
        total += log(place)
        place +=2 #increment place by 2 (skipping even numbers)
print(n/total) #print the ratio
##Any questions, feel free to email me and ask!
##uzairhasan12@hotmail.com
