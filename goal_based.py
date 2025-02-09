import random
import time

class goalBasedVaccumCleaner:
  def __init__(self,rows,cols):
    self.rows = rows
    self.cols=cols
    self.grid =[]
    for _ in range(rows):
      row=[]
      for _ in range(cols):
        data=random.choice([0,1])
        row.append(data)
      self.grid.append(row)
    self.VC_Position = (0,0)

  def display_grid(self):
    for i in range(self.rows):
      for j in range(self.cols):
        if(i,j)== self.VC_Position:
          print("VC",end="")
        elif self.grid[i][j] == 1:
          print(" D ",end="")
        else:
          print(" . ",end="")

      print()


  def clean(self):
    x,y = self.VC_Position
    if self.grid[x][y]==1:
      self.grid[x][y]=0
      print(f"Cleaned dirt at ({x},{y})")

  def is_clean(self):
    for rows in self.grid:
      for  cell in rows :
         if cell !=0:
           return False
    return True

 

  def possible_moves(self):
        x, y = self.agent_position
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
  def dirty_positions(self):
    dirty_positions = []
    for i in range(self.rows):
        for j in range(self.cols):
            if self.grid[i][j] == 1:
                dirty_positions.append((i, j))
    return dirty_positions

  def find_nearest_dirtyTile(self):
    dirty_positions = self.dirty_positions()
    if not dirty_positions:
        return None

    x, y = self.VC_Position
    nearest_dirty = None
    min_distance = float('inf')

    for i, j in dirty_positions:
        distance = abs(i - x) + abs(j - y)
        if distance < min_distance:
            min_distance = distance
            nearest_dirty = (i, j)

    return nearest_dirty

  

  def move(self):
    goal = self.find_nearest_dirtyTile()
    if not goal :
      return
    
    x,y =self.VC_Position

    gx,gy=goal
    if x<gx:
      self.VC_Position=(x+1,y)
    elif x>gx:
      self.VC_Position=(x-1,y)
    elif y<gy:
      self.VC_Position=(x,y+1)
    elif y>gy:
      self.VC_Position=(x,y-1)

    print(f"Moved to {self.VC_Position}")        


  def run(self):
    steps =0
    while not self.is_clean():
      self.display_grid()
      self.clean()
      self.move()
      steps+=1
      time.sleep(1)

    print(f"Cleaning complete in {steps} steps!!")

print("Enter no of rows of the grid")
row=int(input())
print("Enter no of columns of the grid")
col=int(input())

vaccum = goalBasedVaccumCleaner(row,col)
vaccum.run()