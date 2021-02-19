from game import constants
import random 
from game.actor import Actor
from game.point import Point
class Word:
    """
    Keeps track of a word and displays it on the screen
    """

    def __init__(self):
        """
        The Class Constructor
        """
        super.__init__()
        self.prepare_words()
        self._list_of_words = []

    def prepare_words(self):
        for x in range(constants.STARTING_WORDS):
            word = (random.choice(constants.LIBRARY))
            position = Point(random.randint(0, constants.MAX_X), constant.MAX_Y)
            velocity = Point(0, -1)
            self.add_word(word, position, velocity)
    
    def add_word(self, word, position, velocity):
        words = Actor()
        words.set_text(word)
        words.set_position(position)
        words.set_velocity(velocity)
        self._list_of_words.append(words)

