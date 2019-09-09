def f(x):
    return x**2


def integral(startingX, endingX, numberOfRectangles):

    widthOfOneRectangle = (float(endingX) - float(startingX)) / numberOfRectangles
    sumAreaOfRectangles = 0

    for i in range(1, numberOfRectangles + 1):                                    # +1 for the whole n number (starts from 1)
        heightOfOneRectangle = f(startingX + i * widthOfOneRectangle)
        areaOfOneRectangle = heightOfOneRectangle * widthOfOneRectangle
        sumAreaOfRectangles += areaOfOneRectangle                          # adding the area of each one rectangle together in one variable
    return sumAreaOfRectangles                                             # return the sum of the area of all rectangles together


print(integral(5, 10, 1000000))


# trapezoidal Rule
