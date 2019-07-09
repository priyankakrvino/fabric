from random import randint
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    rn =  randint(range_start, range_end)
    return rn	

if __name__ == "__main__":

   print('854'+str(random_with_N_digits(7)))
