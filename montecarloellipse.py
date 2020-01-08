# Carolyn Stienen
# DSC 430
# 11/05/2019
# I have not given or received any unauthorized assistance on this assignment
#YT Link: https://youtu.be/nojJ92Uhp5E

import random
import math

NUMBER_OF_POINTS = 10000

class Point():

    def __init__(self,xcoord,ycoord):
        """initialize new Point

        Args:
            xcoord: x coordinate
            ycoord: y coordinate
        """

        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        """Set x coordinate

        Args:
            xcoord: x coordinate
        """

        self.x = xcoord

    def sety(self, ycoord):
        """Set y coordinate

        Args:
            xcoord: y coordinate
        """

        self.y = ycoord

    def get(self):
        """Get current point

        Returns:
            current point's x and y coordinates as a tuple
        """

        return(self.x, self.y)

    def getx(self):
        """Get x coordinate of current point

        Returns:
            x coordinate of current point as int
        """

        return(self.x)

    def gety(self):
        """Get y coordinate of current point

        Returns:
            y coordinate of current point as int
        """

        return self.y

class Box():

    def __init__(self,p1,p2,p3,p4):
        """Initialize box. Assumes p1 p2 p3 and p4 are in clockwise order

        Args:
            p1: lower left most point
            p2: upper left most point
            p3: upper right most point
            p4: lower right most point
        """

        self.pointOne = p1
        self.pointTwo = p2
        self.pointThree = p3
        self.pointFour = p4

    def getLengthX(self):
        """Gets horizontal length of box

        Returns:
            length as int or float
        """

        return self.pointFour.getx() - self.pointOne.getx()

    def getLengthY(self):
        """Gets vertical length of box

        Returns:
            length as int or float
        """

        return self.pointTwo.gety() - self.pointOne.gety()

    def getArea(self):
        """Gets area of box

        Returns:
            area as int or float
        """

        return self.getLengthX() * self.getLengthY()


class Ellipse():

    def __init__(self,p1,p2,w):
        """Initialize Ellipse

        Args:
            p1: Focal point
            p2: Focal point
            w: width of long axis
        """

        self.pointOne = p1
        self.pointTwo = p2
        self.width = w

    def setPointOne(self, p1):
        """Set first focal point

        Args:
            p1: focal point
        """

        self.pointOne = p1

    def setPointtwo(self, p2):
        """Set first focal point

        Args:
            p2: focal point
        """

        self.pointTwo = p2

    def setWidth(self,w):
        """Set width of ellipse's long axis

        Args:
            w: width of long axis
        """

        self.width = w

    def getPointOne(self):
        """Gets first focal point

        Returns:
            focal point as Point
        """

        return(self.pointOne)

    def getPointTwo(self):
        """Gets second focal point

        Returns:
            focal point as Point
        """

        return(self.pointTwo)

    def getWidth(self):
        """Gets width of long axis

        Returns:
            width as int or float
        """

        return(self.width)

    def isIn(self,point):
        """Determines if a point is inside the ellipse

        Args:
            point: point to determine if is inside the ellipse

        Returns:
            True if point is in ellipse, False if not
        """

        #calculate distance between passed in point and the focal points
        distance_from_p1 = self.distanceBetweenPoints(point,self.pointOne)
        distance_from_p2 = self.distanceBetweenPoints(point,self.pointTwo)

        #if the sum of the two previous distances is less than the width then the point
        # is in the ellipse
        if distance_from_p1 + distance_from_p2 <= self.width:

            return True

        else:

            return False

    def distanceBetweenPoints(self,p1,p2):
        """Calculates distance between two points

        Args:
            p1: point one
            p2: point two

        Returns:
            distance between two points as float
        """

        #get squared x and y differences
        x = (p1.getx() - p2.getx())**2
        y = (p1.gety() - p2.gety())**2

        #return sum of square root
        return math.sqrt(x+y)

    def __repr__(self):
        """String representation of Ellipse

        Returns:
            String stating Ellipse's focal points
        """

        return("Point one is ({},{}). Point two is ({},{}).".format(self.pointOne.getx,self.pointOne.gety,self.pointTwo.getx,self.pointTwo.gety))



def main():

    """first_x_one = 1
    first_y_one = 1

    first_x_two = 1
    first_y_two = 1

    second_x_one = 1
    second_y_one = 1

    second_x_two = 1
    second_y_two = 1

    first_w = 2
    second_w = 2"""

    first_x_one = 3.5
    first_y_one = 4

    first_x_two = 6
    first_y_two = 8

    second_x_one = -1.5
    second_y_one = -2

    second_x_two = 0
    second_y_two = -1

    first_w = 10
    second_w = 11

    first_p1 = Point(first_x_one, first_y_one)
    first_p2 = Point(first_x_two, first_y_two)

    second_p1 = Point(second_x_one, second_y_one)
    second_p2 = Point(second_x_two, second_y_two)

    first_ellipse = Ellipse(first_p1, first_p2, first_w)
    second_ellipse = Ellipse(second_p1, second_p2, second_w)

    box = generateBox(first_ellipse, second_ellipse)

    #drawPoints needs to return percentage
    result = drawPoints(box, first_ellipse, second_ellipse, NUMBER_OF_POINTS)

    area_of_box = box.getArea()

    print("result is " + str(result))

    print("Area between ellipses is " + str(result * area_of_box))

def generateBox(first_ellipse, second_ellipse):
    """Create box encompassing both ellipse

    Args:
        first_ellipse: ellipse object
        second_ellipse: ellipse object

    Returns:
        Box object whose area encludes all of both ellipses
    """

    #Determine various mins and maxs
    largest_width = max(first_ellipse.width,second_ellipse.width)

    smallest_x = min(first_ellipse.getPointOne().getx(), first_ellipse.getPointTwo().getx(), second_ellipse.getPointOne().getx(), second_ellipse.getPointTwo().getx())
    largest_x = max(first_ellipse.getPointOne().getx(), first_ellipse.getPointTwo().getx(), second_ellipse.getPointOne().getx(), second_ellipse.getPointTwo().getx())

    smallest_y = min(first_ellipse.getPointOne().gety(), first_ellipse.getPointTwo().gety(), second_ellipse.getPointOne().gety(), second_ellipse.getPointTwo().gety())
    largest_y = max(first_ellipse.getPointOne().gety(), first_ellipse.getPointTwo().gety(), second_ellipse.getPointOne().gety(), second_ellipse.getPointTwo().gety())

    #make the smallest coordinates slightly smaller
    smallest_x -= largest_width/2
    smallest_y -= largest_width/2

    #make the largest coordinates slightly larger
    largest_x += largest_width/2
    largest_y += largest_width/2

    #defining points 1,2,3,4 from bottom left corner then clockwise
    box_p1 = Point(smallest_x,smallest_y)
    box_p2 = Point(smallest_x,largest_y)
    box_p3 = Point(largest_x,largest_y)
    box_p4 = Point(largest_x,smallest_y)

    #create Box object
    box = Box(box_p1,box_p2,box_p3,box_p4)

    return box

def drawPoints(box, first_ellipse, second_ellipse, n):
    """Draw n number of points in box and determine how many are in both ellipse to find success rate

    Args:
        first_ellipse: Ellipse object
        second_ellipse: Ellipse object
        n: number of points to make within the box

    Returns:
        success rate of point drawing as float
    """

    success_count = 0


    for i in range(0,n):
        #make random point and find out whether it's in or out of both ellipse
        result = makeRandomPoint(box,first_ellipse,second_ellipse)

        #increment success counter if necessary
        if result:
            success_count += 1

    print("Number of successesss is {}".format(success_count))

    print("n is {}".format(n))

    #returns float representing percent of successes
    return(success_count/n)



def makeRandomPoint(box,first_ellipse,second_ellipse):
    """Create a random point within box using passed in RNG

    Args:
        box: the Box object holding both ellipses
        first_ellipse: ellipse object
        second_ellipse: ellipse object
        rng: Random Number Generator to use

    Returns:
        True if random point is in both ellipse, False if not
    """

    random_x = random.random()
    random_y = random.random()

    #use random numbers to generate coordinates
    x_coordinate = (random_x * box.getLengthX()) + box.pointOne.getx()
    y_coordinate = (random_y * box.getLengthY()) + box.pointOne.gety()

    target_point = Point(x_coordinate,y_coordinate)

    #Determine if point is in both ellipse
    if first_ellipse.isIn(target_point) and second_ellipse.isIn(target_point):

        return True

    else:

        return False


main()