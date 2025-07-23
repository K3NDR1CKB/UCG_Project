age = 17

if age >= 16:
    print(f"You are {age} years old.")
    print("You are old enough to drive!")

print("End of Section 1")
print("=" * 40)

temperature = 75


if temperature < 80:
    print("It's {temperature} degrees outside.")
    print("It's cool! Wear a jacket.")
else:
    print(f"It's {temperature} degrees outside.")
    print("It's cool! Wear a jacket.")

    print("End of Section 2")
    print("=" * 40)

student_grade = 85

if student_grade >= 90: 
    print(f"Your grade is {student_grade}")
    print("Excelent! You got an A!")

elif student_grade >= 80:
    print(f"Your grade is {student_grade}")
    print("Great job! You got a B!")
else:
    print(f"Your grade is {student_grade}")
    print("Keep studying! You can do better!")

score = 95

print("--- Not EQUAL TO (!=) ---")
if score !=100:
    print(f"Your score is {score}")
    print("Almost perfect, but not quite 100!")

    print("End of Section 4 ")

    day = "Saturday"

    if day == "Saturday" or day == "Sunday":
        print(f"today is {day}")
        print("It's the weekend! Time to relax!")
    else:
        print(f"Today is {day}")
        print("It's a weekday. Time for school or work!")