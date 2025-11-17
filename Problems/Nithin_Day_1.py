#1. Area of Square
side = 5
area_square = side * side       
print(area_square)
# o/p: 25 

#2. Area of Rectangle
length = 10
breadth = 5 
area_rectangle = length * breadth
print(area_rectangle)
# o/p: 24 

#3. Area of Triangle
base = 8
height = 6
area_triangle = 0.5 * base * height
print(area_triangle)
# o/p: 20.0 

#4. perimeter of Square
perimeter_square = 4 * side 
print(perimeter_square)
# o/p: 24 

#5. perimeter of Rectangle
perimeter_rectangle = 2 * (length + breadth)
print(perimeter_rectangle)
# o/p: 16 

#6. perimeter of Triangle
side1 = 5
side2 = 6
side3 = 7
perimeter_triangle = side1 + side2 + side3
print(perimeter_triangle)
# o/p: 18    

#7. Break Amount
n = 3700
a = n//1000
b = n%1000
c = b//500
d = n%500
print(a,c,d)
# o/p: 1000s: 3 - 500s: 1 - Remaining: 200

#8. Convert Hours Mintues Seconds
s = 3672
hours = s//3600
rem = s%3600
minutes = rem//60
seconds = rem%60
print(hours,minutes,seconds)
# o/p: Hours: 1 - Minutes: 1 - Seconds: 12 

#9. Sum
M = 85
P = 90
C = 88
print(M+P+C)
# o/p: 263 

#10 Average
avg = (M + P + C) / 3
print(f"{avg:.2f}")
# o/p: avg: 87.67 