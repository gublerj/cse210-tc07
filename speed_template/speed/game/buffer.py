from game.actor import Actor
from game.point import Point

class Buffer(Actor):
    """
        prep_display
        displays user input over the dashes

        get_typed_word
        return the typed word (without dashes)

        empty_word
        resets string to be empty
    """

    def __init__(self):
    """
        Initializes the word to be an empty string
        Sets position of buffer to bottom of the screen
    """
        super().__init__()
        self._word = ""
        # Sets position to the bottom of the terminal (top left is 0,0)
        position = Point(1, 20)
        self.set_position(position)
        self.set_text(f"Buffer: {self._word}")
    
    def empty_word(self):
    """
        Called when player hits enter to reset the string to be empty
    """
        self._word = ""

    def prep_display(self, letter):
    """
        Each letter is added to the string '_word' and then displayed over the dashes
    """
        self._word += letter
        self.set_text(f"Buffer: {self._word}")

    def get_typed_word(self):
    """
        Return the string '_word' with the letters the user has typed
    """
        return self._word