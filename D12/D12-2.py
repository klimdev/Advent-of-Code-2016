
from Compiler import Program


inputFile = open('D12.txt', 'r')
program2 = Program([0,0,1,0])

program2.compile(inputFile)
program2.run()

print(program2.reg['a'])