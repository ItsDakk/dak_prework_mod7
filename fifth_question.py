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