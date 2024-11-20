#Find the sum of prime number from a user list
import myModule as mm
nums=list(map(int,input("Enter numbers:").split()))
#nums=[10, 12, 13,15, 17]
s=0
for n in nums:
    if mm.primeFinder(n):
        s=s+n
if s>=10:
     r=mm.digitSum(s)
else:
     r=s
print(f"Sum of all prime numebr is: {r}")
