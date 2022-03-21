# Questions 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below. def hello_name(user_name):

def hello_name(user_name):
    while True:
        user_name = input("What is your user_name? " + 
        "\nEnter 'q' to exit program.")
        if user_name == 'q':
            break
        else:
            print("hello_" + user_name + "!")
    
hello_name(user_name=" ")

# --------------------------------------------

# Question 2:
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():

def first_odds(num_list):
    for number in num_list:
        if number % 2 == 1:
            return number
            print(number)

num_list = list(range(1,102))
first_odds(num_list)

# --------------------------------------------

# Question 3:
# Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below. def max_num_in_list(a_list):

def max_num_in_list(a_list):
    max_number = max(a_list)
    return (max_number)


a_list = [0, 5, 67, 15, 102, 1400, -5, 2, 9]
print(max_num_in_list(a_list))

# --------------------------------------------

# Question 4:
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false). def is_leap_year(a_year):

def leap_year():
    year = input("Is this a leap year? ")
    year = int(year)

    if (year % 400 == 0) and (year % 100 == 0):
        print(bool(True))
    elif (year % 4 == 0) and (year % 100 != 0):
        print(bool(True))
    else:
        print(bool())

leap_year()

# --------------------------------------------

# Question 5:
# Write a function to check to see if all numbers in the list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type. def is_consecutive(a_list):

def is_consecutive(a_list):
    if len(a_list) < 1:
        return False
    min_val = min(a_list)
    max_val = max(a_list)
    if max_val - min_val + 1 == len(a_list):
        for i in range(len(a_list)):
            if a_list[i] < 0:
                j = -a_list - min_val
            else:
                j = a_list[i] - min_val
                if a_list[j] > 0:
                    a_list[j] = -a_list[j]
                else:
                    return False
        return True
    return False



a_list = [2, 3, 4, 8, 6, 7,]
print(is_consecutive(a_list))