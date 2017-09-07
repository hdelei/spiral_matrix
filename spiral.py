'''
    Print Spiral Matrix

    given a two-dimensional array sizes, print
    a spiral matrix 
    
'''

class Matrix:
    def __init__(self, cols, rows):        
        self.current = [[0 for item in range(cols)]for i in range(rows)]
        self.current[0] = list(range(1, cols+1))

        self.next_row = 0
        self.next_item = self.current[0][-1] + 1 
        
    @property
    def current_matrix(self):
        return self.current
    
    def right(self):        
        for i in range(len(self.current)):            
            for j in range(len(self.current[i]))[::-1]:                
                if self.current[i][j] == 0:
                    self.current[i][j] = self.next_item
                    self.next_item += 1
                    self.next_row = i
                    break         

    def down(self):        
        for i in range(len(self.current[self.next_row]))[::-1]:
            if self.current[self.next_row][i] == 0:                
                self.current[self.next_row][i] = self.next_item
                self.next_item += 1        
        self.next_row -= 1
    
    def left(self):
        for i in range(len(self.current))[::-1]:            
            for j in range(len(self.current[i])):                
                if self.current[i][j] == 0:
                    self.current[i][j] = self.next_item
                    self.next_item += 1
                    self.next_row = i
                    break

    def up(self):
        for i in range(len(self.current[self.next_row])):
            if self.current[self.next_row][i] == 0:                
                self.current[self.next_row][i] = self.next_item
                self.next_item += 1
        self.next_row += 1

    def print_spiral(self):
        while True:
            if any(0 in row for row in self.current):
                matrix.right()
                matrix.down()
                matrix.left()
                matrix.up()
            else:
                break
        for item in self.current: print(item)
        
#create an empty two-dimensional matrix 
matrix = Matrix(6, 3)

#print an array of two spiral dimensions in ascending order from number 1
matrix.print_spiral()
