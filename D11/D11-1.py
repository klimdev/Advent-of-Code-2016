
from Solver import Floor, Generator, Chip, Solver, Me

floors = [ Floor(5) for i in range(0 ,4) ]
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
floors[0].gens.setdefault(0, Generator(0))
floors[0].chips.setdefault(0, Chip(0))

# f1
floors[1].gens.setdefault(1, Generator(1))
floors[1].gens.setdefault(2, Generator(2))
floors[1].gens.setdefault(3, Generator(3))
floors[1].gens.setdefault(4, Generator(4))

# f2
floors[2].chips.setdefault(1, Chip(1))
floors[2].chips.setdefault(2, Chip(2))
floors[2].chips.setdefault(3, Chip(3))
floors[2].chips.setdefault(4, Chip(4))

start = Me(floors)
#print(floors)
solver = Solver(start)

done = [ Floor(5) for i in range(0 ,4) ]
for i in range(0,5):
    done[3].gens.setdefault(i, Generator(i))
    done[3].chips.setdefault(i, Chip(i))
done = Me(done,3)

solver.solve(done)