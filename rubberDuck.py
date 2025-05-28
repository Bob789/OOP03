class RubberDuck:
    # Private class variable (shared across all instances)
    __color: str = "yellow"

    def __init__(self, quack_volume=5):
        # Private instance variable (unique to each object)
        self.__quack_volume = quack_volume

    @staticmethod
    def squeak()->None:
        # Static method: does not use 'self' or 'cls'
        # Useful for utility functions related to the class
        print("Squeak!")

    @classmethod
    def get_color(cls) ->str:
        # 'cls' refers to the class itself (not an instance)
        # Allows access to class-level variables like '__color'
        return cls.__color

    @classmethod
    def set_color(cls, new_color: str) -> None:
        # set
        if not new_color:
            raise ValueError("Color cannot be empty")
        cls.__color = new_color
    # Regular methode
    def boost_volume(self) ->None:
        self.__quack_volume += 1

    @property
    def quack_volume(self) ->int:
        # Getter for the private instance variable '__quack_volume'
        return self.__quack_volume

    @quack_volume.setter
    def quack_volume(self, value) ->int:
        # Setter with validation for '__quack_volume'
        if value < 0:
            raise ValueError("Volume must be a non-negative integer")
        self.__quack_volume = value

    def __str__(self):
        # Special method dunder that defines the string representation of the object
        return f"RubberDuck(quack_volume={self.__quack_volume}, color={RubberDuck.__color})"

