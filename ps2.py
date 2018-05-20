# Problem Set 2
# Name: Uzair Hasan
# Collaborators: None
# Date & Time: May 20, 2018, 9:26am - 9:40am

##Objective of this code is figure out if with the equation 6a + 9b + 20c can you get an answer for numbers 50+

def dioph(test):
    for a in range(0, test): 
        aValue = 6*a
        if(aValue > test): #if aValue alone is greater than test value
            break  #end function
        for b in range(0, test): 
            bValue = 9*b
            if(bValue + aValue > test):  #if aValue+ bValue are greater than test value
                break  #move back and increase AValue
            for c in range (0, test):
                temp = bValue + aValue + c*20
                if (temp > test): #if equation is greater than test value
                    break #move back and increase bValue
                elif(temp == test): #what we are looking for, temp == test
                    print (str(test) + ' = ' + str(a) + '*6 + ' + str (b) + '*9 + ' + str (c) + '*20') #print values
                    break #move back and increase bValue
                
for x in range(50,56): #test numbers between 50 and 56-1 
    dioph(x) #call dioph function with argument of loop value
    
""" 
 
Since we can find 5 numbers in a row after 50, we know that we can find any
number >50. This is because it is able to fill the +1 gap 5 times, which means moving
forward, it is impossible not to find a combination for a number >50

"""
##Any questions, feel free to email me and ask!
##uzairhasan12@hotmail.com
