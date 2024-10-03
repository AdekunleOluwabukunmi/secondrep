import pandas as pd

student_data = []

while True:
    name = input("Enter student's name: ")
    course = input("Enter course name: ")
    while True:
        try:
            test_score = float(input("Enter test score (0-40): "))
            if 0 <= test_score <= 40:
                break
            else:
                print("Test score must be between 0 and 40.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            exam_score = float(input("Enter exam score (0-60): "))
            if 0 <= exam_score <= 60:
                break
            else:
                print("Exam score must be between 0 and 60.")
        except ValueError:
            print("Please enter a valid number.")

    total_score = test_score + exam_score
    student_data.append({'Name': name, 'Course': course, 'Test Score': test_score, 'Exam Score': exam_score, 'Total Score': total_score})
    while True:
        another = input("Do you want to enter another data? (yes/no): ").strip().lower()
        if another == 'yes':
            break
        elif another == 'no':
            print("Your data is on the way, please hold on...")
            break
        else:
            print("Wrong command. Please enter 'yes' or 'no'.")

    if another == 'no':
        break

df = pd.DataFrame(student_data)

df.to_excel('student_performance.xlsx', index=False)

print("Data has been saved to 'student_performance.xlsx'.")
import matplotlib.pyplot as plt
average_scores = df.groupby('Name')['Total Score'].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(average_scores['Name'], average_scores['Total Score'], color='skyblue')
plt.title('Average Student Performance')
plt.xlabel('Student')
plt.ylabel('Average Score')
plt.grid(True)
plt.savefig('average_student_performance.png')
plt.show()

if len(df) > 1:
    class_averages = df.groupby('Course')['Total Score'].mean().reset_index()
    print("\nClass Averages:")
    print(class_averages)
else:
    print("\nNot enough data to calculate class averages.")
