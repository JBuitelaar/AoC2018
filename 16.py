from src.operators import *
import re
input_raw = open('16.txt').read()

[input, tests] = input_raw.split('\n\n\n\n')
inputs = input.split('\n\n')
pattern = re.compile(r"Before: \[([\d, ]+)\]\n([\d ]+)\nAfter:  \[([\d, ]+)\]")
parsed = [pattern.match(line).groups() for line in inputs]

def parse(string, spl=', '):
    return [int(x) for x in string.split(spl)]

samples = [(parse(b), parse(op, ' '), parse(a)) for (b, op, a) in parsed]

operators = [addr, addi, mulr, muli, banr, bani, bori, borr, setr, seti,
             gtir, gtri, gtrr, eqir, eqri, eqrr]


print("Part I")

def matches(sample):
    (before, [_, a, b, c], after) = sample
    return sum(1 for op in operators if op(before, a, b, c) == after)


print(sum(1 for sample in samples if matches(sample) >= 3))

print("Part II")

code_to_op = {i: set() for i in range(16)}
for sample in samples:
    (before, [opcode, a, b, c], after) = sample
    for ix, op in enumerate(operators):
        if op(before, a, b, c) == after:
            code_to_op[opcode].add(ix)

code_map = [None]*16
while len(code_to_op):
    found = {k: v for (k, v) in code_to_op.items() if len(v) == 1}
    #print(found)
    if not found:
        raise Exception("no more unique maps") # we may need to try the inverse...
    to_remove = set()
    for opcode, opset in found.items():
        op = opset.pop()
        to_remove.add(op)
        code_map[opcode] = op
        del code_to_op[opcode]

    code_to_op = {k: v.difference(to_remove) for k, v in code_to_op.items()}

res = [0, 0, 0, 0]

test_lines = tests.splitlines()
for test in test_lines:
    (opcode, a, b, c) = [int(x) for x in test.split(" ")]
    res = operators[code_map[opcode]](res, a, b, c)
    # print(res)

print(res[0])