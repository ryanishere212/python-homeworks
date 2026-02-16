Side1=int(input("enter side1: "))
Side2=int(input("enter side2: "))
Side3=int(input("enter side3: "))

if Side1>Side2 and Side1>Side3:
    if Side1*Side1 == Side2*Side2 + Side3*Side3:
        print("Yes")
    else:
        print("No")
elif Side2>Side1 and Side2>Side3:
    if Side2*Side2 == Side1*Side1 + Side3*Side3:
        print("Yes")
    else:
        print("No")
elif Side3>Side1 and Side3>Side2:
    if Side3*Side3 == Side1*Side1 + Side2*Side2:
        print("Yes")
    else:
        print("No")        
else:
    print("invalid")