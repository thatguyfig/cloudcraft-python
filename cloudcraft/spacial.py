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

    def __init__(self, count, shape):

        # set count
        self.count = count

        # set shape
        self.shape = shape

    def show(self):

        """Shows the classes current count and shape values"""

        print('Count:', self.count, 'Shape:', self.shape)
        

