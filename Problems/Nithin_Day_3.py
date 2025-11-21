
# 1. Print Numbers from 1 to n
N = int(input("Enter the value:"))
for i in range(1,N+1):
    print(i)

# 2. Print Numbers from m to n
N = int(input("Enter the value:"))
M = int(input("Enter the value:"))
for i in range(N,M+1):
    print(i)

#3. Print Numbers from n to 1 in Reverse
N = int(input("Enter the value:"))
for i in range(N,0,-1):
    print(i)

# 4. Print Numbers from n to m in Reverse
N = int(input("Enter the value:"))
M = int(input("Enter the value:"))
for i in range(N,M-1,-1):
    print(i)

#5. Sum of n Natural Numbers
N = int(input("Enter the value:"))
count=0
for i in range(N+1):
    count+=i
print(count)

#6. Factorial of a Number
N = int(input("Enter the value:"))
fact=1
for i in range(1,N+1):
    fact*=i
print(fact)

#7. Sum of m to n Numbers
N = int(input("Enter the vlaue:"))
M = int(input("Enter the value:"))
count=0
for i in range(N,M+1):
    count+=i
print(count)

#8. Product of m to n Numbers
N = int(input("Enter the value:"))
M = int(input("Enter the value:"))
product = 1
for i in range(N,M+1):
    product*=i
print(product)

#9. Print Factors of a Number
N = int(input("Enter the value:"))
for i in range(1,N+1):
    if N%i==0:
        print(i)

# 10. Count of Factors
N = int(input("Enter the value:"))
fact = 1
count = 0
for i in range(1,N+1):
    if N%i==0:
        count+=1
print(count)

#11. Prime Number Check
n = int(input("Enter a number: "))

if n <= 1:
    print("Not a prime number")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

#12. Even Numbers from m to n
N = int(input("Enter the value:"))
M = int(input("Enter the value:"))

for i in range(N,M+1):
    if i%2==0:
        print(i)

#13. Odd Numbers from m to n
N = int(input("Enter the value:"))
M = int(input("Enter the value:"))

for i in range(N,M+1):
    if i%2!=0:
        print(i)

#14. Count of Even and Odd Numbers
N = int(input("Enter the value:"))
M = int(input("Enter the value:"))
Even_count=0
Odd_count=0
for i in range(N,M+1):
    if i%2==0:
        Even_count+=1
    else:
        Odd_count+=1
print("Even =",Even_count)
print("Odd =",Odd_count)

#15. Reverse a String
N = input("Enter the String:")
print(N[::-1])

#16. Check for Palindrome String
N = input("Enter the Sting:")
str_rev = N[::-1]
if N == str_rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#17. Sum of Digits
N = int(input("Enter the value:"))
count=0
while N>0:
    digit = N%10
    count+=digit
    N//=10
print(count)

# 18. Product of Digits
N = int(input("Enter the value:"))
count=1
while N>0:
    digit = N%10
    count*=digit
    N//=10
print(count)

# 19. Armstrong Number Check
n = int(input("Enter a number: "))
temp = n
count = len(str(n))
sum = 0

while n > 0:
    digit = n % 10
    sum += digit ** count
    n //= 10

if sum == temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

# 20. Reverse a Number
N = int(input("Enter the value:"))
rev = 0
while N>0:
    digit = N%10
    rev = rev*10+digit
    N//=10
print(rev)

# 21.Palimdrome check
N = int(input("Enter the value:"))
temp = N
rev = 0
while N>0:
    digit = N%10
    rev = rev*10+digit
    N//=10
if temp==rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#22. Count Vowels in String
N = input("Enter the string:")
vowels=['a','e','i','o','u']
count=0
for ch in N:
    if ch in vowels:
        count+=1
print(count)

#22. Count Constants in String
N = input("Enter the string:")
vowels=['a','e','i','o','u']
count=0
for ch in N:
    if ch not in vowels:
        count+=1
print(count)

#24. Count Vowels and Consonants
N = input("Enter the String:")
vowels = ['a','e','i','o','u']
Vowel_count = 0
Constant_count = 0
for ch in N:
    if ch in vowels:
        Vowel_count+=1
    else:
        Constant_count+=1
print(Vowel_count)
print(Constant_count)

#25. Perfect Number Check
N = int(input("Enter the number: "))
sum_div = 0

for i in range(1, N):
    if N % i == 0:
        sum_div += i

if sum_div == N:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

#26. Neon Number Check
N = int(input("Enter the value:"))
sq=N*N
count=0
while sq>0:
    digit = sq%10
    count+=digit
    sq//=10
if count==N:
    print("Neon Number")
else:
    print("Not Neon Number")


#27. Strong Number Check
N = int(input("Enter the value:"))
temp = N
count=0
while temp>0:
    digit = temp%10
    fact=1
    for i in range(1,digit+1):
        fact*=i
    count+=fact
    temp//=10
if count == N:
    print("Strong Number")
else:
    print("Not strong Number")
 
#28. Harshad Number Check
N = int(input("Enter the number: "))
temp = N
sum_digits = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    temp //= 10

if N % sum_digits == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")


#29. Fibonacci Series
n = int(input("Enter how many terms: "))

a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Nearsted prime
def n_p(N):
    if N<2:
        return False
    for i in range(2,int(N**0.5)+1):
        if N%i==0:
            return False
    return True
N = int(input("Enter the value:"))
if n_p(N):
    print("prime")
else:
    left=N-1
    right=N+1
    while True:
        if n_p(left):
            print(left)
            break
        if n_p(right):
            print(right)
            break
        left=left-1
        right=right+1