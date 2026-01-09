
day = int(input("Enter a number (1-7): "))

# Match-case (Python 3.10+ feature) to act like a switch
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        # Default case if no match
        print("Invalid")

