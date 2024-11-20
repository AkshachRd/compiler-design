from LL1 import *

# RULES = [
#     ["Z", ["E $"]],
#     ["E", ["E + T"]],
#     ["E", ["T"]],
#     ["T", ["T * F"]],
#     ["T", ["F"]],
#     ["F", ["id"]],
#     ["F", ["( E )"]],
# ]
# word = ["(", "id", "+", "id", ")"]


RULES = [
    ["Z", ["F $"]],
    ["F", ["f I ( I ) S ; I = E end"]],
    ["S", ["I = E S"]],
    ["S", ["e"]],
    ["E", ["E * I"]],
    ["E", ["E + I"]],
    ["E", ["I"]],
    ["I", ["a"]],
    ["I", ["b"]]
]
word = ["f", "a", "(", "b", ")", "a", "=", "a", "*", "b", ";", "a", "=", "b", "end"]


# RULES = [
#     ["Z", ["S $"]],
#     ["S", ["a A B b"]],
#     ["A", ["c"]],
#     ["A", ["e"]],
#     ["B", ["d"]],
#     ["B", ["e"]],
# ]
# word = "acb"

# RULES = [
#     ["Z", ["S $"]],
#     ["S", ["T C"]],
#     ["T", ["a T b"]],
#     ["T", ["e"]],
#     ["C", ["C c"]],
#     ["C", ["c c c"]],
# ]
# word = "abccc"


table = Run(RULES, "LR", "FR", show_all=True )

runner = Runner_cl(1, table, "$")


for i in range(len(word)):
    runner.Run(word[i], i)

is_end = runner.Run("$", "end_end")
print("СТРОКА: ", word)

if is_end:
    print("ПРОХОДИТ✅")
else:
    print("НЕ ПРОХОДИТ❌")

