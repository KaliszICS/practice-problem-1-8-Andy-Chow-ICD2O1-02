
'''
    Assignment: boolean logic
    Author: Andy Chow
    Date Created: Sept 26, 2024
    Date Last Modified: Sept 26, 2024
'''

def q1():
    bool1 = True
    bool2 = False
    print(bool1 and bool2)
    print(bool1 or bool2)
  #Write Assignment code here

def q2():
    inter1 = input("Enter an integer: ")
    inter1 = int(inter1)
    bool3 = inter1 != 0 
    print(bool3)
  #Write Assignment code here

def q3():
    num1 = input("Enter a number: ")
    num1 = float(num1)
    bool4 = num1 > -1 and num1 < 11
    print(bool4)
  #Write Assignment code here

def q4():
    food1 = input("Input food: ")
    drink1 = input("Input drink: ")
    bool5 = not food1 == "pizza" or not drink1 == "pop"
    print(bool5)
  #Write Assignment code here

def q5():
    inter2 = input("Enter an integer: ")
    inter2 = int(inter2)
    bool6 = not inter2%2
    print(f"The integer {inter2} is {bool6}.")
  #Write Assignment code here

#Do not edit code after this
#Comment out the followwing code when running tests

# q1()
# q2()
# q3()
# q4()
# q5()
