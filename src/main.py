from parser.parser import Parser
from optimizer.optimizer import optimize
from verifier.interpreter import Interpreter

parser = Parser()

program = parser.parse_file(
    "samples/example.ir"
)

optimized = optimize(program)

original_output = (
    Interpreter().execute(program)
)

optimized_output = (
    Interpreter().execute(
        optimized
    )
)

print("Original Output:")
print(original_output)

print()

print("Optimized Output:")
print(optimized_output)

print()

if original_output == optimized_output:

    print("PASS")

else:

    print("FAIL")