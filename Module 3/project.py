 import datetime

today = datetime.date.today()
print("Today's date is:", today)

attendance = float(input("Enter your attendance percentage: "))
exam_date_input = input("Enter your exam date : ")

exam_date = datetime.datetime.strptime(exam_date_input, "%Y-%m-%d").date()

print("Exam Date is:", exam_date)

if exam_date >= today:
    print("Exam date is valid.")

    if attendance >= 75:
        print("You are eligible for the exam.")
    else:
        print("Attendance is below 75%.")