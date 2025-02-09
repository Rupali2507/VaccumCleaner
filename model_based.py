import random
import time

class Model_based_VaccumCleaner:
  def __init__(self,rows,cols):
    self.rows =rows
    self.cols=cols
    self.grid=[]
    for _ in range(rows):
      row=[]
      for _ in range(cols):
        data=random.choice([0,1])
        row.append(data)
      self.grid.append(row)
    self.VC_Position= ((0,0))
    self.visited = set()

  def displayGrid(self):
    for i in range(self.rows):
      for j in range(self.cols):
        if(i,j)==self.VC_Position:
          print("VC",end="")
        elif self.grid[i][j]==1:
          print(" D ",end="")
        else:
          print(" . ",end="")
      print()

  def clean(self):
    x,y = self.VC_Position
    if self.grid[x][y]==1:
      self.grid[x][y]=0
      print(f"Cleaned dirt at ({x},{y})")

  def possible_moves(self):
        x, y = self.VC_Position
        possible_moves = []

        if x > 0:
            possible_moves.append((x - 1, y)) 
        if x < self.rows - 1:
            possible_moves.append((x + 1, y))  
        if y > 0:
            possible_moves.append((x, y - 1))  
        if y < self.cols - 1:
            possible_moves.append((x, y + 1))  
        
        return possible_moves    


  def move(self):
    x,y=self.VC_Position
    possible_moves=self.possible_moves()

    dirty_moves = [i for i in possible_moves if self.grid[i[0]][i[1]]==1] 
    unvisited_moves = [i for i in possible_moves if i not in self.visited] 

    if dirty_moves:
      next_move = random.choice(dirty_moves)
      
    elif unvisited_moves:
      next_move = random.choice(unvisited_moves)
      
    else:
      next_move = random.choice(possible_moves)

    self.VC_Position=next_move  
    print(f"Moved to {self.VC_Position}")  

  def run(self,steps):
    for _ in range(steps):
      self.displayGrid()
      self.clean()
      self.move()
      time.sleep(1)


print("Enter no of rows of the grid")
row=int(input())
print("Enter no of columns of the grid")
col=int(input())
vaccum = Model_based_VaccumCleaner(row,col)
vaccum.run(row*col)                 

        