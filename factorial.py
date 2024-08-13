n=int(input("Enter a number for the factorial:"))
fact=1
if n<0:
    print("Enter a positive no")
elif n==0:
    print("Entered no is 0 factorial is : 1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print("The Factorial of ",n,"is",fact)
