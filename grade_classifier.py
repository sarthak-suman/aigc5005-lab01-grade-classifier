import math


mark_input = input("Enter your mark out of 100: ").strip()

if mark_input == "":
    print("No mark was entered. Please enter a number from 0 to 100.")
else:
    try:
        mark_percentage = float(mark_input)
    except ValueError:
        print("Invalid input. Please enter a numeric mark from 0 to 100.")
    else:
        if not math.isfinite(mark_percentage):
            print("Invalid input. Please enter a finite number from 0 to 100.")
        elif mark_percentage < 0 or mark_percentage > 100:
            print(
                f"Invalid mark: {mark_percentage}. "
                "The valid range is 0 to 100."
            )
        else:
            if mark_percentage >= 80:
                letter_grade = "A"
            elif mark_percentage >= 70:
                letter_grade = "B"
            elif mark_percentage >= 60:
                letter_grade = "C"
            elif mark_percentage >= 50:
                letter_grade = "D"
            else:
                letter_grade = "F"

            print(
                f"Result: {mark_percentage:.1f}% is classified as grade "
                f"{letter_grade}."
            )