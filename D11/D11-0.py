
from Solver import Floor, Generator, Chip, Solver

floors = [ Floor(2) for i in range(0 ,4) ]
# f0
#floors[0].gens.setdefault('promethium', Generator('promethium'))
#floors[0].chips.setdefault('promethium', Chip('promethium'))

# f1
#floors[1].gens.setdefault('cobalt', Generator('cobalt'))
#floors[1].gens.setdefault('curium', Generator('curium'))
#floors[1].gens.setdefault('ruthenium', Generator('ruthenium'))
#floors[1].gens.setdefault('plutonium', Generator('plutonium'))

# f2
#floors[2].chips.setdefault('cobalt', Chip('cobalt'))
#floors[2].chips.setdefault('curium', Chip('curium'))
#floors[2].chips.setdefault('ruthenium', Chip('ruthenium'))
#floors[2].chips.setdefault('plutonium', Chip('plutonium'))

# f0
floors[0].chips.setdefault(0, Chip(0))
floors[0].chips.setdefault(1, Chip(1))

# f1
floors[1].gens.setdefault(0, Generator(0))

# f2
floors[2].gens.setdefault(1, Generator(1))

#print(floors)
solver = Solver(floors)
solver.solve()