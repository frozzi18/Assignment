import math

print('Hello world!')

def multi(x,y):
    # Multiply two number and return the sum
    return x*y

def square(x):
    # Square the number and return the value
    return x*x

def sum(x,y):
    # Add two number and return the sum
    return x+y

def object_after(a, b, c ):
    print("The object's position after " + str(a) + " seconds is " + str(b) + " m.")
    print("The object's velocity after " + str(a) + " seconds is " + str(c) + " m/s.")


gravity = -9.81
fallingTime = 10
initialVelocity = 0.0
finalVelocity = 0.0
initialPosition = 0.0
finalPosition = 0.0
finalVelocity = multi(gravity, fallingTime)
finalVelocity = sum(finalVelocity, initialVelocity)

finalPosition = square(fallingTime)
finalPosition = 0.5 * multi(gravity, finalPosition)
finalPosition = sum(finalPosition, sum(multi(initialVelocity, fallingTime), initialPosition))

object_after(fallingTime, finalPosition, finalVelocity)
