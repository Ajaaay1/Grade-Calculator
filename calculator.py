print("Welcome to the Grade Calculator")

# Ask the user how many grades they want to enter
num_grades = int(input("How many scores would you like to enter? "))

scores = []
for i in range(num_grades):
    score = float(input(f"Enter score #{i + 1}: "))
    scores.append(score)

# Calculate and display the average
if len(scores) > 0:
    average = sum(scores) / len(scores)
    print(f"The average grade is: {average:.2f}")
else:
    print("No scores were entered.")
