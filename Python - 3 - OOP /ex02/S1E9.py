from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract class for creating a character with a first name and health state.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Constructor to initialize the character's first name and health status.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        Method to change the character's health state to dead
        (is_alive = False).
        """
        self.is_alive = False

    @abstractmethod
    def __str__(self):
        """Abstract method that must be implemented in subclasses."""
        pass


class Stark(Character):
    """Class representing a Stark character, which inherits from Character."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Stark class."""
        super().__init__(first_name, is_alive)

    def __str__(self):
        """String representation of the Stark character."""
        return f"Stark: {self.first_name}, Alive: {self.is_alive}"
