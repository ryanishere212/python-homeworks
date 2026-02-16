FG=int(input("please enter your first garde:" ))
SG=int(input("please enter your second garde:" ))
TG=int(input("please enter your third garde:" ))
FoG=int(input("please enter your forth garde:" ))
Sum=(FG+SG+TG+FoG)/4
if Sum>18:
    print("A")
elif Sum>16:
    print("B")
elif Sum>12:
    print("C")
elif Sum>10:
    print("D")
elif Sum<10:
    print("Failed")