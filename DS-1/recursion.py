################################### RECURSION ################################

def factorial(n):
    assert n>=0 and int(n) == n,'factorial number cannot be negative or integer'
    if n <= 1:
        return 1
    else :
        return n*factorial(n-1)


print(factorial(5))


def fibanocci(n):
    assert n>=0 and int(n) == n,'fibanocci number cannot be negative or integer'
    if n in [0,1]:
        return n
    else:
        return fibanocci(n-1)+fibanocci(n-2)
    
print(fibanocci(-3.5))


################################### END ######################################