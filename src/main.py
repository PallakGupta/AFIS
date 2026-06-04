from parser.parser import Parser
from dependency.graph_builder import build_graph
from shuffler.scheduler import random_topological_sort
from verifier.interpreter import Interpreter
from renamer.renamer import rename_program

parser = Parser()

program = parser.parse_file(
    "samples/example.ir"
)

graph = build_graph(program)

order = random_topological_sort(
    graph
)

shuffled_program = [
    program[i]
    for i in order
]

renamed_program = rename_program(
    shuffled_program
)

print("Original Program")
print()

for inst in program:
    print(inst)

print()
print("------------------")
print()

print("Shuffled Program")
print()

for inst in renamed_program:
    print(inst)
    
print()
print("------------------")
print()

original_output = (
    Interpreter()
    .execute(program)
)

shuffled_output = (
Interpreter().execute(
    renamed_program
)
)

print(
    "Original Output:",
    original_output
)

print(
    "Shuffled Output:",
    shuffled_output
)

if original_output == shuffled_output:

    print()
    print(
        "Semantic Equivalence: PASS"
    )

else:

    print()
    print(
        "Semantic Equivalence: FAIL"
    )