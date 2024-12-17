from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name):
        super().__init__(first_name)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return (
            f"<{self.__class__.__name__} of Vector: "
            f"('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        )

    def __repr__(self):
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name):
        super().__init__(first_name)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        return (
            f"<{self.__class__.__name__} of Vector: "
            f"('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        )

    def __repr__(self):
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        lannister = cls(first_name)
        lannister.is_alive = is_alive
        return lannister
