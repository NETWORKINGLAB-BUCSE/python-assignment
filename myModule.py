import math as m
def primeFinder(n): #7
    #n_root=int(n**0.5)+1
    if n<2:
        return  False
    for i in range(2, int(m.sqrt(n))+1):
        if n%i==0:
            return  False
    return True
def digitSum(n):
    digit_sum=0
    while n!=0:
        reminder=n%10
        digit_sum+=reminder
        n=int(n/10)
    return  digit_sum