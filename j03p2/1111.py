num1=int(input("enter number1 (must be 3 digits):"))
num2=int(input("enter number2 (must be 3 digits):"))

Num1FD= num1//100
Num1SD= num1//10
Num1TD= num1%10

Num2FD= num2//100
Num2SD= num2//10
Num2TD= num2%10

if Num1FD==False or Num2FD==False:
    print("both numbers must be 3 digits")
elif  num1>999 or num2>999:
    print("both numbers must be 3 digits")
elif num1==num2:
    print(f"{num1} = {num2}")
elif num1>num2:
    print(f"{num1} < {num2}")
elif num1<num2:
    print(f"{num2} < {num1}") 

#the following lines are unnecessary and additional they were written just for reasurance   

#elif Num1TD>Num2TD:
#    print(f"{num1} < {num2}")
#elif Num1TD<Num2TD:
#    print(f"{num2} < {num1}")
#elif Num1TD==Num2TD and Num1SD>Num2SD:
#    print(f"{num1} < {num2}")
#elif Num1TD==Num2TD and Num1SD<Num2SD:
#    print(f"{num2} < {num1}")
#elif Num1TD==Num2TD and Num1SD==Num2SD and Num1FD>Num2FD:
#    print(f"{num1} < {num2}")
#elif Num1TD==Num2TD and Num1SD==Num2SD and Num1FD<Num2FD:
#    print(f"{num2} < {num1}")

else:
    print("invalid number")