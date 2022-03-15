# Task 2

print("Enter Marks Obtained in 5 Subjects: ")
markOne = int(input())
markTwo = int(input())

tot = markOne + markTwo
avg = tot/2

user_input = input("What is your target grade?")

if avg >= 87:
    print("Your Grade is A")
    print("Well Done")
elif avg > 50:
    print("Your Grade is a B")
    print("Nice")
elif avg < 40:
    print("Your Grade is a C")
    print("More work")
else:
    print("Fail, better luck next time") 