# Question 1:
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