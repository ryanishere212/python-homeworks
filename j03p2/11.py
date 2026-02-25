Number=45
Guess=int(input("guess the number:"))
if Guess==Number:
    print("Correct!")
elif Guess!=Number:
    if Guess>Number:
        print("you gotta enter a lower number")
    elif Guess<Number:
        print("you gotta enter a higher number")
else:
    print("invalid")
    