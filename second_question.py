# Write a python function, first_odds that prints the 
# odd numbers from 1-100 and returns nothing def first_odds():

def first_odds(num_list):
    for number in num_list:
        if number % 2 == 1:
            return number
            print(number)

num_list = list(range(1,102))
first_odds(num_list)
