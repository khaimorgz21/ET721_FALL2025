def addthreenumbers(n1=0, n2=0, n3=0):
    return n1+n2+n3

def subtracttwonumbers(n1=0 , n2=0):
    return n1-n2

def multplythreenumbers(n1=1 , n2=1, n3=1):
    return n1*n2*n3

def dividetwonumbers(n1,n2):
    try:
        return n1/n2
    expect ZeroDivisionError:
        print("ERROR! can't divide by zero")
    expect ValueError:
        print("ERROR! not a")
    