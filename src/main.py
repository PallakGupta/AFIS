from parser.parser import Parser
from optimizer.constant_folding import (
    constant_fold
)

parser = Parser()

program = parser.parse_file(
    "samples/example.ir"
)

print("Before Folding")
print()

for inst in program:
    print(inst)

optimized = constant_fold(
    program
)

print()
print("After Folding")
print()

for inst in optimized:
    print(inst)