"""Maskify user mobile number
Write a method to maskify user mobile number except last 3 digits and print the output
Ex: maskify(“9988776655”) should print “#######655”"""
# function to replace the numbers and print the number 
def change(mobile):

    if not mobile.isdigit() or len(mobile) < 3:# the condition whether input contains all digits or not and legth of mobile less than 3 

        return "Invalid input"

    return "#" * (len(mobile) - 3) + mobile[-3:]
inp=input("Enter mobile Number")#TAking input from user
print(change(inp))