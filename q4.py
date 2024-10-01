class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    # Make the class iterable by defining the __iter__ method
    def __iter__(self):
        # Yield length as a dictionary
        yield {'length': self.length}
        # Yield width as a dictionary
        yield {'width': self.width}

# Example usage:
rect = Rectangle(10, 5)

# Iterating over the instance of Rectangle
for dim in rect:
    print(dim)
