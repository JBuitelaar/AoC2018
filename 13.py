# (shamelessly borrowed from someone else)
from collections import defaultdict
from typing import List, Tuple, Dict
from copy import deepcopy

lines=open('13.txt','r').read().splitlines()

class Cart:
    def __init__(self, pos: complex, di: complex):
        self.position = pos
        self.direction = di
        self.cross = 0 # left, straight, right
        self.dead = False

cart_direction = {
    "<": -1,
    "v": +1j,
    ">": +1,
    "^": -1j,
}

cart_replacement = {
    "<": "-",
    "v": "|",
    ">": "-",
    "^": "|",
}

tracks = defaultdict(lambda: "")  # only store important tracks: \ / +. The others don't change direction
carts = []
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char in "<v>^":
            direction = cart_direction[char]
            carts.append(Cart(x + y * 1j, direction))  
            part=cart_replacement[char]
        else:
            part = char
        if part in "\\/+":
            tracks[(x + y * 1j)] = part

def turn_cart(cart: Cart, part: str):
    """This space uses a downwards-facing Y axis, which means all calculations
    must flip their imaginary part. For example, rotation to the left
    (counterclockwise) would be multiplying by -1j instead of by +1j."""
    if not part:  # empty track is impossible, and | or - don't matter
        return
    if part == "\\":
        if cart.direction.real == 0:
            cart.direction *= -1j  # ⮡ ⮢
        else:
            cart.direction *= +1j  # ⮧ ⮤
    if part == "/":
        if cart.direction.real == 0:
            cart.direction *= +1j  # ⮣ ⮠
        else:
            cart.direction *= -1j  # ⮥ ⮦
    if part == "+":
        cart.direction *= -1j * 1j ** (cart.cross%3)  # rotate left, forward, or right
        cart.cross +=1

def part1(carts):
    while True:
        carts.sort(key=lambda c: (c.position.imag, c.position.real))
        for ci, cart in enumerate(carts):
            cart.position += cart.direction
            if any(c2.position == cart.position for c2i, c2 in enumerate(carts) if c2i != ci):
                return str(int(cart.position.real)) + "," + str(int(cart.position.imag))
            part = tracks[cart.position]
            turn_cart(cart, part)

print(part1(deepcopy(carts)))

# Part II

def part2(carts):
    while len(carts) > 1:
        carts.sort(key=lambda c: (c.position.imag, c.position.real))
        for ci, cart in enumerate(carts):
            if cart.dead:
                continue
            cart.position += cart.direction
            for ci2, cart2 in enumerate(carts):
                if ci != ci2 and cart.position == cart2.position and not cart2.dead:
                    cart.dead = True
                    cart2.dead = True
                    break
            if cart.dead:
                continue
            part = tracks[cart.position]
            turn_cart(cart, part)
        carts = [c for c in carts if not c.dead]
    if not carts:
        raise Exception("There's an even number of carts, there's isn't 1 cart left at the end!")
    cart = carts[0]
    return str(int(cart.position.real)) + "," + str(int(cart.position.imag))

print(part2(deepcopy(carts)))

