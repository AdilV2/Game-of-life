import random

class State():
    ''' Give you the state of the grid '''

    def __init__(self, size_x = 10 , size_y = 10, random_init = False):
        self.size_x = size_x
        self.size_y = size_y
        self.grid = self.empty_grid()
        if random_init == True:
            self.add_random_star()
        else:
            self.add_glider()

    def empty_grid(self):
        matrix = []
        for row in range(self.size_y):
            row_tmp = []
            for col in range(self.size_x):
                row_tmp.append(" ")

            matrix.append(row_tmp)

        return matrix


    def add_glider(self):
        self.grid[0][2] = "*"
        self.grid[1][2] = "*"
        self.grid[1][0] = "*"
        self.grid[2][1] = "*"
        self.grid[2][2] = "*"

    def add_random_star(self):
        for row in range(self.size_y):
            for column in range(self.size_x):
                rand_cell = random.randint(0,1)
                if rand_cell == 0:
                    self.grid[row][column]= "*"
                
        
    def __repr__(self):

        top = "_" * (self.size_x +2)

        down = "-" * (self.size_x + 2)
    
        body = ""
        
        for row in self.grid:
            body = body + str('|' +''.join(str(r) for r in row) + '|\n')
 
        return str(top) + "\n" + str(body) + str(down)

s = State(size_x=3, size_y=3, random_init=True)

#print(s.grid)

print(s)