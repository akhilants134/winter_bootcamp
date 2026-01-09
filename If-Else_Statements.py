
# Declare and initialize marks variable
marks = 54

# Check grade conditions using if-elif-else ladder
if marks < 25:
    print("Grade: F")  # Less than 25 is Grade F
elif marks >= 25 and marks <= 44:
    print("Grade: E")  # Between 25 and 44 is Grade E
elif marks >= 45 and marks <= 49:
    print("Grade: D")  # Between 45 and 49 is Grade D
elif marks >= 50 and marks <= 59:
    print("Grade: C")  # Between 50 and 59 is Grade C
elif marks >= 60 and marks <= 69:
    print("Grade: B")  # Between 60 and 69 is Grade B
elif marks >= 70:
    print("Grade: A")  # 70 and above is Grade A
else:
    print("Invalid marks entered.")  # Handles invalid inputs

