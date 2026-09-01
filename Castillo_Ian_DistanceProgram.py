import math

## Ask for the abscissa and the ordinate of the first point
point_x1 = float(input('Enter point_x1 value: '))
point_y1 = float(input('Enter point_y1 value: '))

## Ask for the abscissa and the ordinate of the second point
point_x2 = float(input('Enter point_x2 value: '))
point_y2 = float(input('Enter point_y2 value: '))

## Finding the differences of the second abscissa/ordinate and the first abscissa/ordinate.
difference1 = ((point_x2) - (point_x1))
difference2 = ((point_y2) - (point_y1))

## Below provided the distance formula rewritten with math library functions.
distance = (math.sqrt(pow(difference1,2) + pow(difference2,2)))

## Displays your four values, then the final calculated distance.
print('x1 Entered:', point_x1)
print('y1 Entered:', point_y1)
print('x2 Entered:', point_x2)
print('y2 Entered:', point_y2)
print('The distance between the two points is:', round(distance, 2))