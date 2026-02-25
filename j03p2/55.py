num1=int(input("plrase enter num1: "))
op=input("please enter an operator: ")
num2=int(input("please enter num2: "))
if op=="+":
    print(f"{num1}{op}{num2} = {num1+num2}")
elif op=="-":
     print(f"{num1}{op}{num2} = {num1-num2}")
elif op=="*":
     print(f"{num1}{op}{num2} = {num1*num2}")
elif op=="/":
    if num2==0:
        print("num2 cannot be zero!")
    else:
         print(f"{num1}{op}{num2} = {num1/num2}")
else:
    print("invalid operator")    