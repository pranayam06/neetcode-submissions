from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.byx = defaultdict(set)
        self.byy = defaultdict(set)
        self.all_points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.byx[x].add(y)
        self.byy[y].add(x)
        self.all_points[(x,y)] += 1
        

    def count(self, point: List[int]) -> int:
        x,y = point
        arr_x = list(self.byx[x])
        res = 0

        for cand_y in arr_x:  
            if y == cand_y: 
                continue
            side = cand_y - y 
            # up left 
            points = [self.all_points[(x-side, y)], self.all_points[(x, y+side)], self.all_points[(x-side, y+side)]]
            res+= math.prod(points)
            #up right
            points = [self.all_points[(x+side, y)], self.all_points[(x, y+side)], self.all_points[(x+side, y+side)]]
            res+= math.prod(points)
            #bottomleft
            points = [self.all_points[(x-side, y)], self.all_points[(x, y-side)], self.all_points[(x-side, y-side)]]
            res+= math.prod(points)
            #bottom right
            points = [self.all_points[(x+side, y)], self.all_points[(x, y-side)], self.all_points[(x+side, y-side)]]
            res+= math.prod(points)
        return res


                

