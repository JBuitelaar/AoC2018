from dataclasses import dataclass

@dataclass(frozen=True, order=True)
class Point:
    """Point. sorting based on 'reading order'"""
    y: int
    x: int

    def __add__(self,other):
        return Point(self.y+other.y,self.x+other.x)

    def up(self):
        return Point(self.y-1,self.x)

    def down(self):
        return Point(self.y+1,self.x)

    def left(self):
        return Point(self.y,self.x-1)

    def right(self):
        return Point(self.y,self.x+1)

    def neighbours(self):
        # order in line with the "reading order"
        return (
            self.up(),
            self.left(),
            self.right(),
            self.down()
        )


UP=Point(-1,0)
DOWN=Point(1,0)
LEFT=Point(0,-1)
RIGHT=Point(0,1)

