from gomory_hu import GomoryHuTreeSolver

graph = [[0, 1, 7, 0, 0, 0],
         [1, 0, 1, 3, 2, 0],
         [7, 1, 0, 0, 4, 0],
         [0, 3, 0, 0, 1, 6],
         [0, 2, 4, 1, 0, 2],
         [0, 0, 0, 6, 2, 0]]

# Construct GomoryHuTree
solver = GomoryHuTreeSolver(graph)
solver.build()

# Print Tree Contents
print("TREE:", solver.tree)
print("CAPACITIES:", solver.capacity)


print()
print()

solver.prepare()
print("Prepared for query!")
print("CAPACITIES:", solver.capacity)
print("Query(2, 0): ", solver.query(2, 0))
print("Query(0, 2): ", solver.query(0, 2))
print("Query(1, 4): ", solver.query(1, 4))
print("Query(4, 1): ", solver.query(4, 1))


assert solver.query(2, 0) == 8
assert solver.query(0, 2) == 8
assert solver.query(1, 4) == 7
assert solver.query(4, 1) == 7
