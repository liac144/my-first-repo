def evaluate_student_pass_fail(exam_score, total_classes, attended_classes):
    # Criteria for passing
    passing_exam_score = 70
    minimum_attendance_percentage = 80

    # Calculate attendance percentage
    attendance_percentage = (attended_classes / total_classes) * 100

    # Determine pass/fail status
    if exam_score >= passing_exam_score and attendance_percentage >= minimum_attendance_percentage:
        return "Pass"
    else:
        return "Fail"

# Get user input
try:
    exam_score = float(input("Enter the exam score (0-100): "))  # User input for exam score
    total_classes = int(input("Enter the total number of classes: "))  # User input for total classes
    attended_classes = int(input("Enter the number of classes attended: "))  # User input for attended classes

    # Validate inputs
    if (0 <= exam_score <= 100) and (total_classes > 0) and (0 <= attended_classes <= total_classes):
        # Evaluate pass/fail status
        status = evaluate_student_pass_fail(exam_score, total_classes, attended_classes)
        print(f"The student's status is: {status}")
    else:
        print("Invalid input. Please make sure the exam score is between 0-100, the total classes is greater than 0, and the attended classes is within the range of total classes.")

except ValueError:
    print("Invalid input. Please enter numeric values for exam score and class counts.")
