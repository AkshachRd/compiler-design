
from SLR1 import *

# RULES = [
#     ["Z", ["E $"]],
#     ["E", ["E + E"]],
#     ["E", ["i"]]
#     ]
# word = "i + i"

# RULES = [
#     ["Z", ["F $"]],
#     ["F", ["f I ( I ) S ; I = E end"]],
#     ["S", ["I = E S"]],
#     ["S", ["e"]],
#     ["E", ["E * I"]],
#     ["E", ["E + I"]],
#     ["E", ["I"]],
#     ["I", ["a"]],
#     ["I", ["b"]]
# ]
# word = ["f", "a", "(", "b", ")", "a", "=", "a", "*", "a", "+", "b", ";", "b", "=", "a", "end"]

# RULES = [
#    ["S", ["A B C $"]],
#    ["A", ["a A"]],
#    ["A", ["e"]],
#    ["B", ["b B"]],
#    ["B", ["b"]],
#    ["C", ["c C"]],
#    ["C", ["c"]]
#    ]
# word = "a b c"

# RULES = [
#     ["Z", ["E $"]],
#     ["E", ["E + T"]],
#     ["E", ["T"]],
#     ["T", ["T * F"]],
#     ["T", ["F"]],
#     ["F", ["( E )"]],
#     ["F", ["i"]]
#     ]
# word = "i * i + i"

RULES = [
    ["S", ["A B C $"]],
    ["A", ["a A"]],
    ["A", ["e"]],
    ["B", ["B b"]],
    ["B", ["e"]],
    ["C", ["C c"]],
    ["C", ["e"]],
    ]

word = "b a $"

print(First(RULES))
print()
print(Follow(RULES))
#
Print_2D_Table(SLR_Table(RULES))
CheckIfItSLR(SLR_Table(RULES))
Runner(SLR_Table(RULES), word, RULES)
print()
print("///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
print()
