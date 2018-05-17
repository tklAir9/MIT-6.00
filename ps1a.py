# Problem Set 1
# Name: Uzair Hasan
# Collaborators: None
# Date & Time: May 16, 2018, 5:06am - 5:14am
##Objective of this code is find the 1000th prime number

counter = 1 #amount of primes
place = 3 #which number we are evaluating 
while (counter!=1000): #keep checking until we find 1000th
    for x in range(3,place):
        if(place%x==0): #if we get no remainder
            place+=2 #increment place by 2 (skipping even numbers)
            break #stop loop and skip else block
    else: #loop didnt break
        counter+=1 #found a prime, add to counter
        place+=2 #increment place by 2 (skipping even numbers)
print(place-2) #print value of 1000th number (subtract 2 because we added 2 after the 1000th)

##Any questions, feel free to email me and ask!
##uzairhasan12@hotmail.com
