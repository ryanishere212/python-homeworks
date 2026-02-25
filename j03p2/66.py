x=int(input("enter number:"))
if x==0:
    print(x)
elif x%15==0:
    if x%5==0 and x%3==0:
        print("Fizzbuzz!")
    elif x%3==0:
        print("Fizz!")
    elif x%5==0:
        print("Buzz!")
elif x%5==0:
    print("Buzz!")
elif x%3==0:
    print("Fizz!")
else:
    print(x)   
