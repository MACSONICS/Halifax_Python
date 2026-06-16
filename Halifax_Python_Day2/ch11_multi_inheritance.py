# Define the first superclass
class Painter:
    def paint(self):
        print("Can paint a picture.")

# Define the second superclass
class Writer:
    def write(self):
        print("Can write a book.")

# Define the subclass that inherits from both Painter and Writer
class ArtisticGenius(Painter, Writer):
    def create(self):
        print("Creating art and literature.")

# Create an instance of ArtisticGenius
genius = ArtisticGenius()

# Access methods from the superclasses
genius.paint()  # Output: Can paint a picture.
genius.write()  # Output: Can write a book.

# Access method from the subclass
genius.create()  # Output: Creating art and literature.
