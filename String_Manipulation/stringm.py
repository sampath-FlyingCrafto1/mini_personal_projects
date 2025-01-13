class StringManipulator:
    def __init__(self, string):
        self.string = string

    def concatenate(self, other_string):
        return self.string + other_string

    def length(self):
        return len(self.string)

    def slice(self, start, end):
        return self.string[start:end]

    def repeat(self, times):
        return self.string * times

    def uppercase(self):
        return self.string.upper()

    def lowercase(self):
        return self.string.lower()

    def strip(self):
        return self.string.strip()

    def split(self, separator):
        return self.string.split(separator)

    def format(self, *args):
        return self.string.format(*args)

    def interpolate(self, **kwargs):
        return self.string.format(**kwargs)
my_string = "Hello, World!"
manipulator = StringManipulator(my_string)

print("Concatenated string:", manipulator.concatenate(" Goodbye"))
print("Length of the string:", manipulator.length())
print("Sliced string:", manipulator.slice(7, None))
print("Repeated string:", manipulator.repeat(3))
print("Uppercase:", manipulator.uppercase())
print("Lowercase:", manipulator.lowercase())
print("Stripped string:", manipulator.strip())
print("Split string:", manipulator.split(","))
print("Formatted string:", manipulator.format("Alice", 30))
print("Interpolated string:", manipulator.interpolate(name="Bob", age=25))