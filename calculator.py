print("Welcome to the Grade Calculator")

num_grades = int(input("How many scores would you like to enter? "))

scores = []
for i in range(num_grades):
    score = float(input(f"Enter score #{i + 1}: "))
    scores.append(score)

if len(scores) > 0:
    average = sum(scores) / len(scores)
    print(f"\nThe average grade is: {average:.2f}")

    if average >= 90:
        letter = "A"
    elif average >= 80:
        letter = "B"
    elif average >= 70:
        letter = "C"
    elif average >= 60:
        letter = "D"
    else:
        letter = "F"
        
    print(f"Your final letter grade is: {letter}")

    
    print(f"Highest Score: {max(scores)}")
    print(f"Lowest Score: {min(scores)}")
    
else:
    print("No scores were entered.")
