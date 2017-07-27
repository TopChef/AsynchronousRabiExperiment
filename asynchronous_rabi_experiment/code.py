"""
Flips the state of the object
"""
class Flippable(object): 
    
    STATE_1 = "STATE_1"
    STATE_2 = "STATE_2"
    
    def __init__(self, initial_state: str) -> None:
        """
        The initializer. This is the first method called by the class in order
        to create an object. It behaves very similarly to the ```setUp`` method
        that we defined in tests. However, instead of running before every
        test, it runs every time we create a new object of this type.
        """
        self.state = initial_state
    
    def flip(self) -> None:
        """
        Flips the state of a bistate object 
        """
        if self.state == self.STATE_1:
            self.state = self.STATE_2
        elif self.state == self.STATE_2:
            self.state =  self.STATE_1
