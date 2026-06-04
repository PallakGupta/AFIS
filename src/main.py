from parser.parser import Parser

from optimizer.optimizer import (
    optimize
)

parser = Parser()

program = parser.parse_file(
    "samples/example.ir"
)

print("Before Optimization")
print()

for inst in program:
    print(inst)

optimized = optimize(
    program
)

print()
print("After Optimization")
print()

for inst in optimized:
    print(inst)