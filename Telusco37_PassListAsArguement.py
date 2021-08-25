

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    return(even, odd)



lst = [21, 24, 31, 54, 42, 13, 15] #prefer to get a number of elements from the user

even, odd = count(lst)

print("Even: {} and Odd:{}" .format(even, odd)) #the format method belongs to strings, so the values are automatically converted to strings and used inside the brackets