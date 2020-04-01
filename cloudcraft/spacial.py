# SPACIAL.PY
#
# Simple maths on spacial coordinates - this section is massively WIP


class Grid:
    
    """Class to define the limits of a normal drawing"""
    
    TOP_LEFT = (0, 0)
    TOP_RIGHT = (11, 0)
    BOTTOM_LEFT = (0 , 14)
    BOTTOM_RIGHT = (11, 14)
    
class Edges(Grid):
    
    """Inherited class to define the lengths of the diagram space in relation to the Grid class."""
    
    RIGHT_LENGTH = Grid.BOTTOM_RIGHT[1] - Grid.TOP_RIGHT[1]
    TOP_LENGTH = Grid.TOP_RIGHT[0] - Grid.TOP_LEFT[0]
    BOTTOM_LENGTH = TOP_LENGTH
    LEFT_LENGTH = BOTTOM_LENGTH

class Formation:

    """A class to help with spacial coordination of multiple objects in a group

       For instance, you might use this when reorganising the layout of some of the nodes on a diagram to group them correctly.
    
    """

    def __init__(self, count, shape, base_limit=100):

        # set count
        self.count = count

        # set shape
        self.shape = shape

        # set default width and height
        self.width = 0
        self.height = 0
        self.max = 0
        self.missing_slots = 0

        # set limit for the number of possible squares
        self.limit = base_limit

        # if the shape is square, calculate it's dimensions
        if self.shape == 'square':

            self.calculate_square_dimensions()

    def calculate_square_dimensions(self):

        """Calculates the correct width for the number of objects in the count in a sqaure shape"""
        
        # generate a list of numbers that we will use to square
        base_numbers = list(range(1, self.limit + 1 ))

        # update the list of numbers to square each of them
        square_numbers = [x*x for x in base_numbers]

        # zip the two together nicely in a list
        zipped = list(zip(base_numbers, square_numbers))

        # now perform some maths to figure out our square
        
        # iterate over all the elements
        for item in zipped:

            # if the first element (the square) is greater than or equal to our count
            if item[1] >= self.count:

                # we have found the correct side width and height
                self.width = item[0]
                self.height = item[0]
                self.max = item[1]

                # calculate missing slots
                self.missing_slots = item[1] - self.count

                # stop the iteration
                break
    
    def draw_square(self, node_character, space_character):

        """Draws a square using the width and count data, to fill it as much as possible"""

        # set a total character count to 0
        character_total_count = 0

        # set a character line count to 0
        character_line_count = 0

        # start iterating for the count
        for x in range(0, self.max):
            
            # if the count is less than the total count, we have nodes to print
            if character_total_count < self.count:

                # set character to denote a node
                character_to_print = node_character

            # otherwise it's time to draw spaces
            else:
                character_to_print = space_character

            # if we should continue printing on the same line
            if character_line_count  < self.width:

                # print the character
                print(character_to_print, end="")

                # don't forget to increment counters
                character_line_count = character_line_count + 1
                character_total_count = character_total_count + 1
                
            
            # otherwise
            else:
                # reset the line character counter
                character_line_count = 0

                # time to print a new line
                print('\r')

                
                # print the character
                print(character_to_print, end="")

                # don't forget to increment counters
                character_line_count = character_line_count + 1
                character_total_count = character_total_count + 1






    def show(self):

        """
        Shows the classes current count and shape values.

        Has some nutty features which draw the formation of the square, with maximumised squareness.
        
        """

        # show the object count and shape
        print('Count:', self.count, '\nShape:', self.shape, '\n')
        
        # show the current width and height of the shape
        print('Current width:', self.width, '\nCurrent height:', self.height, '\nMissing slots:', self.missing_slots, '\n')
        
        # log to declare the drawing
        print('Formation diagram:')

        # if we can draw it
        if self.shape == 'square':
            
            # draw a square
            self.draw_square(
                node_character='X ',
                space_character='O '
            )
                    
