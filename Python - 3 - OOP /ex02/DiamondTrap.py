from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Represents King Joffrey Baratheon,
    inheriting characteristics from the Baratheon and Lannister families.
    """

    def __init__(self, first_name):
        """
        Initializes a King object with a first name,
        inheriting properties from the Baratheon and Lannister families.

        :param first_name: The first name of the king.
        """
        super().__init__(first_name)
        self.family_name = "Lannister"  # The king's family name is Lannister
        self._eyes = self.eyes  # Initializes the private attribute for eyes
        self._hairs = self.hairs  # Initializes the private attribute for hairs

    @property
    def eyes(self):
        """
        Returns the king's eye color.

        :return: The eye color of the king.
        """
        return self._eyes

    @eyes.setter
    def eyes(self, value):
        """
        Sets the king's eye color.

        :param value: The new eye color.
        """
        self._eyes = value

    @property
    def hairs(self):
        """
        Returns the king's hair color.

        :return: The hair color of the king.
        """
        return self._hairs

    @hairs.setter
    def hairs(self, value):
        """
        Sets the king's hair color.

        :param value: The new hair color.
        """
        self._hairs = value

    def set_eyes(self, color):
        """
        Changes the king's eye color.

        :param color: The new eye color.
        """
        self.eyes = color

    def set_hairs(self, color):
        """
        Changes the king's hair color.

        :param color: The new hair color.
        """
        self.hairs = color

    def get_eyes(self):
        """
        Gets the current eye color of the king.

        :return: The eye color of the king.
        """
        return self.eyes

    def get_hairs(self):
        """
        Gets the current hair color of the king.

        :return: The hair color of the king.
        """
        return self.hairs
