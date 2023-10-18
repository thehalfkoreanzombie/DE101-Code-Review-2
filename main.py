def plus_three(number_1): #set up one argument in the function
    number_plus_three = number_1 + 3 #set variable to add 3 to the argument
    return(number_plus_three) #return the value after function runs)

print(plus_three(5)) #first call
print(plus_three(10)) #second call

def weather_report(weather_1, weather_2): #creating weather report function
    today = "Today is " + weather_1 + " and " + weather_2 #establishing text string for a return with two arguments
    return(today) #return function

print(weather_report("hailing", "sunny")) #call function with arguments 'hailing' and 'sunny'

top_ten = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for item in top_ten:
    print(item * item)
if 7 in top_ten:
    print("We have a 7!")
else:
    print("No 7 here")