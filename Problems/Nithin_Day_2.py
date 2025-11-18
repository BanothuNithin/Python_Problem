from math import ceil
# 1. Given number is evnen or not
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")
#o/p: 6 is an Even number

# 2. Divisible by 5 but Not by 10
num = int(input("Enter then number:"))
if num%5==0 and num!=10:
    print("Satisfy")
else:
    print("Not Satisfy")
#o/p: Satisfy

# 3. Biggest Among Two Numbers
num1 = int(input("Enter the value:"))
num2 = int(input("Enter the value:"))
if num1>num2:
    print("Biggest is :",num1)
else:
    print("Biggest is:",num2)
#o/p: Biggest is: 7

# 4. Smallest Among Two Numbers
num1 = int(input("Enter the value:"))
num2 = int(input("Enter the value:"))
if num1<num2:
    print("Smallest is :",num1)
else:
    print("Smallest is:",num2)
#o/p: Smallest is: 4

# 5. Divisible by 2, 3, and 6
num = int(input("Enter the value:"))
if num%2==0 and num%3==0 and num%6==0:
    print("Satisfy")
else:
    print("Not Satisfy")
#o/p: Satisfy

# 6. Voting Eligibility
age = int(input("Enter the age:"))
if age>=18:
    print(f"{age} Eligible to vote")
else:
    print(f"{age} Not Eligible to vote")
#o/p: 18 Eligible to vote

# 7. Student Pass/Fail Based on All Subjects >= 35
sub1 = int(input("Enter the maths marks:"))
sub2 = int(input("Enter the physics marks"))
sub3 = int(input("Enter the chemistry marks"))

if (sub1 and sub2 and sub3) >=35:
    print("Pass")
else:
    print("Fail")
#o/p: Fail

# 8. Student Pass if Passed Any One Subject (>= 35)
sub1 = int(input("Enter the maths marks:"))
sub2 = int(input("Enter the physics marks"))
sub3 = int(input("Enter the chemistry marks"))

if (sub1 or sub2 or sub3) >=35:
    print("Pass")
else:
    print("Fail")
#o/p: Pass

# 9. Student Pass if Passed Any Two Subjects
sub1 = int(input("Enter the maths marks:"))
sub2 = int(input("Enter the physics marks"))
sub3 = int(input("Enter the chemistry marks"))

if ((sub1 and sub2)  or (sub2 and sub3) or(sub1 and sub3))>=35:
    print("Pass")
else:
    print("Fail")
#o/p: Pass

# 10. Biggest Among Three Numbers
num1 = int(input("Enter the value:"))
num2 = int(input("Enter the value:"))
num3 = int(input("Enter the value:"))
if num1>num2 or num1>num3:
    print("Biggest is:",num1)
elif num2>num1 or num2>num3:
    print("Biggest is:",num2)
else:
    print("Biggest is:",num3)
#o/p: Biggest is: 9

# 11. Smallest Among Three Numbers
num1 = int(input("Enter the value:"))
num2 = int(input("Enter the value:"))
num3 = int(input("Enter the value:"))
if num1<num2 or num1<num3:
    print("Smallest is:",num1)
elif num2<num1 or num2<num3:
    print("Smallest is:",num2)
else:
    print("Smallest is:",num3)
#o/p: Smallest is: 4

# 12. Perfect Square or Not
num = int(input("Enter the value:"))
if (num**0.5) * (num**0.5) == num:
    print(f"{num} Perfect Square")
else:
    print(f"{num} Not Perfect Square")
#o/p: Perfect Square

# 13. Cars Required for Members (Max 5 per car)
num = int(input("Enter the value:"))
cars_required = ceil(num/5)
if cars_required <=5:
    print(cars_required)
#o/p: 4

# 14. Second Biggest Among Three Numbers
num1 = int(input("Enter the value:"))
num2 = int(input("Enter the value:"))
num3 = int(input("Enter the value:"))

numbers = [num1,num2,num3]
sorting = sorted(numbers)
print(sorting)
print("Second Biggest: ",sorting[1])
#o/p: Second Biggest: 18

# 15. Leap Year or Not
year = int(input("Enter the year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} Leap year")
else:
    print(f"{year} Not a Leap year")
#o/p: Leap year