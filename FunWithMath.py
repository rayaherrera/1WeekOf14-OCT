# Starting off
print(22 / 7)
print(355 / 113)
import math

print(9801 / (2206 * math.sqrt(2)))

def archimedes (numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygonCircumference = numSides * sideS
    pi = polygonCircumference / 2
    return pi


print(archimedes(8))
print(archimedes(16))

for sides in range(8, 100, 8):
    print(sides, archimedes(sides))

# experiment with the loop above alongside the actual value of Pi. How many
# sides does it take to make the two close?

# Modify the Archimedes function to take the radius of a circle as a parameter as a parameter
# Can you get a better answer more quickly using a larger circle?

# Accumulators
acc = 0
for x in range(1, 6):
    acc = acc + x

print(acc)

# compute the sum of the first 100 even numbers
# compute the sum of the first 50 odd numbers
# compute the average of the first 100 odd numbers
# write a function that returns the average of the first N numbers, where
#   N is a parameter
# write a function called factorial that computes the product of the first N
#    numbers where N is a parameter
# Each number in the Fibonacci sequence is the sum of the previous two numbers
# The first 2 numbers in the sequence are 1 and 1. Compute the 10th
#    Fibonacci number
# Write a function to compute the Nth Fibonacci number, where N is a parameter.
#   You may assume that N will be greater than or equal to 3


# A Monte Carlo Simulation
import random

print(random.random())

# Boolean expressions
# > greater than
# >= greater than or equal to
# < less than
# <= less than or equal to
# == the same as [ equal to ]
# != NOT equal to

dogWeight = 25
print(dogWeight <= 25)
catWeight = 15

# compound Boolean operators
# and (both have to be true or else it will give you a false answer)
# or (only one has be true to make a true answer)
# not

print(not catWeight < 20)


# Decision Making -- Selection statements
a = 5
b = 10
c = 75

if a > b:
    c = 45

print(c)

if a > b:
    c = 45
    if b > c:
        a = 25
    else:
        a = -25
else:
    c = 1050
    if b == a:
        c = 25

print(a, b, c)


d = 85
e = 72
f = 44
ans = 0


if d > e:
    ans = 12
else:
    if d == e:
        ans = 50
    else:
        if f < d * e:
            ans = 100
        else:
            ans = 75
print(ans)

def montePi(numDarts):

    inCircle = 0

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:
            inCircle = inCircle + 1

    pi = inCircle / numDarts * 4
    return pi

print(montePi(99999))

import turtle

def showMontePi(numDarts):
    scn = turtle.Screen()
    t = turtle.Turtle()
    t.speed(50)
    scn.setworldcoordinates(-2, -2, 2, 2)

    t.penup()
    t.goto(-1, 0)
    t.pendown()
    t.goto(1, 0)

    t.penup()
    t.goto(0, 1)
    t.pendown()
    t.goto(0, -1)

    inCircle = 0
    t.penup()

    for i in range(numDarts):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        distance = math.sqrt(x**2 + y**2)

        t.goto(x, y)

        if distance <= 1:
            inCircle = inCircle + 1
            t.color("blue")
        else:
            t.color("red")

        t.dot()

    pi = inCircle / numDarts * 4
    scn.exitonclick()
    return pi
showMontePi(100)
showMontePi(99999)

#  Your Task:
#  Modify the simulation to plot points in the entire circle.  You will have to
#    adjust the calculated value of pi accordingly.
