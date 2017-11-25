from math import sqrt

def sieve(limit):
    int_list = [x for x in range(2, limit + 1)]
    counter = 2 # start with first prime number
    while counter < sqrt(limit): # checking for numbers greater than square root of limit is not needed
        for x in int_list:
            if x % counter == 0 and x != counter: # do not remove the prime we are checking
                int_list.remove(x)
                int_list = int_list
        counter += 1

    return int_list


#print(sieve(2))
