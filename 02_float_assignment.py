# FLOAT DATATYPE ASSIGNMENT
# =========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the area of a circle with radius 5.5
print("SOLVED EXAMPLE:")
print("Calculate the area of a circle with radius 5.5")
import math
radius = 5.5
area = math.pi * radius ** 2
print(f"Radius: {radius}")
print(f"Area: {area:.2f}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577
print("Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577")
# Your code here
a = 3.14, 2.718, 1.618, 0.577
b = sum(a)/len(a)
print(b)
2.01325

# Question 2: Convert 98.6 Fahrenheit to Celsius (F = C * 9/5 + 32)
print("\nQuestion 2: Convert 98.6 Fahrenheit to Celsius")
# Your code here
F = 98.6
C = (F - 32)*5/9
print(C)
37.0

# Question 3: Calculate the compound interest on $1000 at 5.5% for 3 years
print("\nQuestion 3: Calculate compound interest on $1000 at 5.5% for 3 years")
# Your code here
P,R,T = 1000,5.5,3
Amount = P * (1+R/100)**T 
CI = Amount - P
print(CI)
174.24137499999983

# Question 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2
print("\nQuestion 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2")
# Your code here
import math
a,b = 3.5,4.2
c = math.sqrt(a**2 + b**2)
print(round(c,1))
5.5

# Question 5: Calculate the volume of a sphere with radius 7.8
print("\nQuestion 5: Calculate the volume of a sphere with radius 7.8")
# Your code here
r = 7.8
V = (4/3)*math.pi * r**3
print(V)
1987.798769261791

# Question 6: Round 3.14159 to 3 decimal places
print("\nQuestion 6: Round 3.14159 to 3 decimal places")
# Your code here
R = 3.14159
print(round(R,3))
3.142

# Question 7: Calculate the percentage: 45 out of 67
print("\nQuestion 7: Calculate the percentage: 45 out of 67")
# Your code here
a = 45
b = 67
PER = (a/b)*100
print(PER)
67.16417910447761

# Question 8: Find the square root of 23.456
print("\nQuestion 8: Find the square root of 23.456")
# Your code here
import math
a = 23.456
b = math.sqrt(a)
print(b)
4.843139477652899

# Question 9: Calculate the simple interest: Principal=2500, Rate=6.5%, Time=2.5 years
print("\nQuestion 9: Calculate simple interest: Principal=2500, Rate=6.5%, Time=2.5 years")
# Your code here
p,r,t = 2500,6.5,2.5
si = p*r*t/100 
print(si)
406.25

# Question 10: Convert 45.7 degrees to radians
print("\nQuestion 10: Convert 45.7 degrees to radians")
# Your code here 
import math
D = 45.7
R = math.radians(D)
print(R)
0.7976154681614086