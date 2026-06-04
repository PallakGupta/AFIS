from parser.parser import Parser
from cfg.cfg_builder import build_cfg

parser = Parser()

program = parser.parse_file(
    "samples/example.ir"
)

graph = build_cfg(program)

print("Nodes:")
print(
    list(graph.nodes())
)

print()

print("Edges:")
print(
    list(graph.edges())
)