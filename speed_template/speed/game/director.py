from time import sleep
from game import constants
from game.score import Score
from game.word import Word
from game.buffer import Buffer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        food (Food): The snake's target.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        snake (Snake): The player or snake.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.buffer = Buffer()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._words = Word()
        self._buffer_text
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """
        letter = input_service.get_letter()
        if letter == '*':
            buffer.empty_word()
        else:
            buffer.prep_display(letter)
        

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        _compare_word()
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actor(self.buffer)
        self._output_service.draw_actors(self.words.get_words)
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()

    def _compare_word(self):
        """Compares the word typed in the buffer and words on the screen for a match.

        Args:
            self (Director): An instance of Director.
        """
        list_of_words = self.words.get_words()
        compare = buffer.get_typed_word()
        for n in len(list_of_words):
            words = list_of_words[n]
            word = words.get_text()
            if word == compare:
                self._words.remove_word(n)
                self.score.add_points(1)

        
