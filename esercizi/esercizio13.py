from enum import Enum

# Define an Enum class

# The Enum class is a class that contains a set of constants
class ExampleEnum(Enum):
    FIRST_MEMBER = 1
    SECOND_MEMBER = 2
    THIRD_MEMBER = 3


# Iterate over the Enum members and print their names and values
for member in ExampleEnum:
    print(f"Member: {member.name}, Value: {member.value}")
