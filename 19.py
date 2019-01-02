from src.operators import *
import re

input="""#ip 0
seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5""".splitlines()
input = open('19.txt').read().splitlines()
operators = [addr, addi, mulr, muli, banr, bani, bori, borr, setr, seti,
             gtir, gtri, gtrr, eqir, eqri, eqrr]

names=[f.__name__ for f in operators]
operator_map=dict(zip(names,operators))

instruction_reg=int(input[0][-1])
instructions=[]
for row in input[1:]:
    [name,a,b,c]=row.split(" ")
    instructions.append((operator_map[name],int(a),int(b),int(c)))

ip=0
registers=[0]*6
registers[0]=1
#registers=[0, 0, 3, 10551374, 1, 10551374]
#registers=[1, 0, 3, 10551374, 2, 5275687]

#registers=[1, 0, 3, 10551374, 2, 5275687]
#registers=[1, 0, 3, 10551374, 3, 10551374]
#registers=[1, 0, 3, 10551374, 10551374, 10551374]
#while 0<=ip<len(instructions) and j<10000000:
for j in range(10_000_000):
    ip=registers[instruction_reg]
    if not 0<=ip<len(instructions):
        break

    if ip==8:
        n=registers[3]
        print(sum(j for j in range(1,n+1) if not n%j))
        break

    #if j<200:#>7593280:#j%1_000_000<200:
    #    print(f'{ip:02},{registers},{input[1+ip]}({j})')
    (op,a,b,c)=instructions[ip]

    registers=op(registers,a,b,c)
    registers[instruction_reg]+=1
    #j+=1

print(registers)

print(registers[0],j)


# 1464

#> 1464 7_593_315

"""the code is equivalent tO:
for r[4] in range(1,N+1):
    for r[5] in range(1,N+1):
        if r[4]*r[5]==N:
            r[0]+=r[4]
So basically we're just getting all divisors
"""

n=10551374
n=974
print(sum(j for j in range(1,n+1) if not n%j))
