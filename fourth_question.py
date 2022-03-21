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
