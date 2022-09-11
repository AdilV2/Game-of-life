import random
import copy


class State():
    ''' Gives you the state of the grid '''

    def __init__(self, size_x = 10 , size_y = 10, random_init = False):
        self.size_x = size_x
        self.size_y = size_y
        self.grid = self.empty_grid()
        if random_init == True:
            self.add_random_star()
        else:
            self.add_glider()

    def empty_grid(self):
        '''Allows you to create an empty grid '''
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

    def count_neighbours(self, x, y):
        ''' Allows you to count the number of neighbours of a specific point (x,y) '''
        count = 0

        # Case n°1
        if self.grid[self.cross_the_walls_y_axis(y-1)][self.cross_the_walls_x_axis(x-1)] == "*":
            count = count + 1
        # Case n°2 
        if self.grid[self.cross_the_walls_y_axis(y-1)][self.cross_the_walls_x_axis(x)] == "*":
            count = count + 1
        # Case n°3
        if self.grid[self.cross_the_walls_y_axis(y-1)][self.cross_the_walls_x_axis(x+1)] == "*":
            count = count + 1
        # Case n°4
        if self.grid[self.cross_the_walls_y_axis(y)][self.cross_the_walls_x_axis(x-1)] == "*":
            count = count + 1
        # Case n°5
        if self.grid[self.cross_the_walls_y_axis(y)][self.cross_the_walls_x_axis(x+1)] == "*":
            count = count + 1
        # Case n°6
        if self.grid[self.cross_the_walls_y_axis(y+1)][self.cross_the_walls_x_axis(x-1)] == "*":
            count = count + 1
        # Case n°7
        if self.grid[self.cross_the_walls_y_axis(y+1)][self.cross_the_walls_x_axis(x)] == "*":
            count = count + 1
        # Case n°8
        if self.grid[self.cross_the_walls_y_axis(y+1)][self.cross_the_walls_x_axis(x+1)] == "*":
            count = count + 1
        
        return count
        
    def cross_the_walls_x_axis(self, value):
        ''' it allows you to go through walls x axis'''

        if value > (self.size_x - 1):
            return 0
        elif value < 0:
            return (self.size_x - 1)
        else:
            return value

    def cross_the_walls_y_axis(self, value):
            ''' it allows you to go through walls y axis'''

            if value > (self.size_y - 1):
                return 0
            elif value < 0:
                return (self.size_y - 1)
            else:
                return value

    def next(self):
        ''' Calculating a stage in the game of life '''

        new_step = copy.deepcopy(self)

        for col in range(self.size_y):
            for row in range(self.size_x):
                neighbours_number = self.count_neighbours(col, row)

                if neighbours_number == 3:
                    new_step.grid[row][col] = "*"
                elif neighbours_number < 2 or neighbours_number > 3:
                    new_step.grid[row][col] = " "
                else:
                    new_step.grid[row][col] = self.grid[row][col]

        return new_step

    def __repr__(self):

        top = "_" * (self.size_x +2)

        down = "-" * (self.size_x + 2)
    
        body = ""
        
        for row in self.grid:
            body = body + str('|' +''.join(str(r) for r in row) + '|\n')
 
        return str(top) + "\n" + str(body) + str(down)


s = State(size_x=6, size_y=6)
for _ in range(5):
    print(s)
    s = s.next()
