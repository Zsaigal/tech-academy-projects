class Protected:
    def __init__(self):
        # Define a protected attribute
        self._protectedX = 999
        # Define a private attribute
        self.__privateZ = 213  # Double underscore makes it private

    # Method to access the private attribute
    def getPrivate(self):
        print(self.__privateZ)

    # Method to modify the private attribute
    def setPrivate(self, private):
        self.__privateZ = private

# Create an instance of the Protected class
y = Protected()

# Access and modify the protected attribute directly
y._protectedX = 1000
print(y._protectedX)  # Output: 1000

# Call the setPrivate method to modify the private attribute
y.setPrivate(44)

# Call the getPrivate method to access the private attribute
y.getPrivate()  # Output: 44
