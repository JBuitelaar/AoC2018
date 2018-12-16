from dataclasses import dataclass
import enum
import collections
import itertools

class Team(enum.Enum):
    ELF='E'
    GOBLIN='G'

@dataclass(frozen=True,order=True)
class Point:
    y: int
    x: int

    def neighbours(self):
        return (
            Point(self.y-1,self.x),
            Point(self.y,self.x-1),
            Point(self.y,self.x+1),
            Point(self.y+1,self.x)
        )

@dataclass
class Unit:
    team: Team
    location: Point
    hp: int
    attack_power: int = 3

    @property
    def is_alive(self):
        return self.hp>0

class ElfDied(Exception):
    pass

class NoMoreEnemies(Exception):
    pass

class Grid:
    def __init__(self,input:str,elf_power:int=3,no_deaths=False):
        power = { 'E': elf_power, 'G': 3}
        self.no_deaths=no_deaths
        lines = input.splitlines()
        units=[]
        walls=[]
        cols=max(len(r) for r in lines)
        self.size=(len(lines),cols)

        for y,line in enumerate(lines):
            for x,ch in enumerate(line):
                pt=Point(y,x)
                if '#'==ch:
                    walls.append(pt)
                elif ch in 'EG':
                    units.append(Unit(Team(ch),pt,200,power[ch]))
                else:
                    assert '.'==ch, f"a{ch}a"
        self.units=units
        self.walls=set(walls)

    def __str__(self):

        units=sorted(self.units,key=lambda u: u.location)
        (rows,cols)=self.size
        out=[[['.']*cols,[]] for _ in range(rows)]
        for pt in self.walls:
            out[pt.y][0][pt.x]='#'
        for u in units:
            pt=u.location
            out[pt.y][0][pt.x]=u.team.value
            out[pt.y][1].append(f"{u.team.value}({u.hp})")

        
        #for row in out:
        return "\n".join("".join(row) +" "+ ",".join(info) for [row,info] in out)

    def move_unit(self,unit):
        enemy_locs={u.location: u for u in self.units if u.team!=unit.team and u.is_alive}

        if not enemy_locs:
            raise NoMoreEnemies()
        friend_locs=set(u.location for u in self.units if u.team==unit.team and u!=unit and u.is_alive)

        # move:
        # the second element refers to the move we would make
        to_visit=collections.deque([(unit.location, unit.location)])

        visited = set([unit.location])
        while to_visit:
            (pt,next_loc)=to_visit.popleft()
            for nb in pt.neighbours():
                
                if nb in enemy_locs:
                    unit.location=next_loc
                    return # nothing else to do
                if nb in self.walls or nb in friend_locs:
                    continue # not a valid move
                if nb in visited:
                    continue
                else:
                    visited.add(nb)
                    to_visit.append((nb,nb if next_loc is unit.location else next_loc)) # looking futher
        return



    def play_unit(self,unit):
        self.move_unit(unit)
        nbs=unit.location.neighbours()
        enemies=[u for u in self.units if u.team!=unit.team and u.is_alive and u.location in nbs]
        if enemies:
            enemies.sort(key=lambda u: (u.hp,u.location))
            target=enemies[0]
            target.hp-=unit.attack_power
            if self.no_deaths and target.team == Team.ELF and target.hp <=0:
                raise ElfDied()


    def play_round(self):
        self.units.sort(key=lambda u: u.location)

        for unit in self.units:
            if unit.is_alive:
                self.play_unit(unit)
        self.units=[u for u in self.units if u.is_alive]

    def play(self):
        try:
            #print('playing')
            for r in itertools.count():
                #print(r)
                self.play_round()
                #res=[u.hp for u in self.units if u.is_alive]
                #print(r,sum(res),sorted(res))
                
        except NoMoreEnemies:
            #res=[u.hp for u in self.units if u.is_alive]
            #print(r,sum(res),sorted(res))
            print(r*sum(u.hp for u in self.units if u.is_alive))



filename='15_map.txt'
#filename='15_test5.txt'

print('Part I')
input=open(filename).read()
grid=Grid(input)
grid.play()

print('Part II')
for power in itertools.count(4):
    #print(power)
    grid = Grid(input,power,True)
    
    try:
        grid.play()
        #print(grid)
        #print(power)
        break
    except ElfDied:
        continue
