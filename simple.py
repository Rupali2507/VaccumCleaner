import random
import time

class VaccumCleaner:
  def __init__(self,rows,cols):
    self.rows =rows
    self.cols= cols
    self.grid = []
    for i in range(rows):
      row=[]
      for j in range(cols):
        data=random.choice([0,1])
        row.append(data)
      self.grid.append(row)
    self.agent_Position = (0,0)  

  def displayGrid(self):
    for i in range(self.rows):
      for j in range(self.cols):
        if (i,j) == self.agent_Position:
          print("VC",end="")
        elif self.grid[i][j] ==1:
          print(" D ",end="")
        else:
          print(" . ",end="")
      print()

  def clean(self):
    x,y =self.agent_Position
    if self.grid[x][y]==1:
      self.grid[x][y]=0
      print(f"Cleaned dirt at ({x},{y})")   

  def move(self):
    x, y = self.agent_Position

    if y < self.cols - 1: 
        self.agent_Position = (x, y + 1)
    elif x < self.rows - 1:  
        self.agent_Position = (x + 1, 0)
    else:  
        self.agent_Position = (0, 0)
    
    print(f"Moved to {self.agent_Position}")


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
vaccum = VaccumCleaner(row,col)
vaccum.run(row*col)                    