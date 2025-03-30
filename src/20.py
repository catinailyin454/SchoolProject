class MyClass:
    def __init__(self):
        self.data = ["This is line 1", "This is line 2", "This is line 3"]

    def print_data(self):
        for line in self.data:
            print(line)

# Create an instance of MyClass and call the print_data method
my_instance = MyClass()
my_instance.print_data()
