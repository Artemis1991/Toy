# x and y are integers that relate to a location on the grid. 
# Values that are outside the boundary of the grid should not be allowed.
# facing is a string referencing the direction the robot is facing. 
# Values NORTH, SOUTH, EAST or WEST are allowed.
def place(x, y, facing):
  x = [x,y,facing.casefold()]
  x = checkloc(x)
  return x  

# Moves the robot 1 grid unit in the direction it is facing unless 
# that movement will cause the robot to fall off the grid.
def move(x):  
  if x==None:
    print('Failed')
    return None
  elif x[2] == 'north':
    x[0] = x[0] + 1
  elif x[2] == 'south':
    x[0] = x[0] - 1  
  elif x[2] == 'east':
    x[1] = x[1] + 1
  elif x[2] == 'west':
    x[1] = x[1] - 1  
  x = checkloc(x)
  return x
  
# Rotate the robot 90° anticlockwise/counterclockwise.
def left(x):
  if x==None:
    print('Failed')
    return None
  elif x[2] == 'north':
    x[2] = 'west'
  elif x[2] == 'south':
    x[2] = 'east'  
  elif x[2] == 'east':
    x[2] = 'north'
  elif x[2] == 'west':
    x[2] = 'south'
  x = checkloc(x)
  return x
  
# Rotate the robot 90° clockwise.
def right(x):
  if x==None:
    print('Failed')
    return None
  elif x[2] == 'north':
    x[2] = 'east'
  elif x[2] == 'south':
    x[2] = 'west'  
  elif x[2] == 'east':
    x[2] = 'south'
  elif x[2] == 'west':
    x[2] = 'north'
  x = checkloc(x)
  return x
  
# # Outputs the robot's current grid location and facing direction.
def report(x):
  if x==None:
    print('Failed')
  else:
    print(x[0],",",x[1],",",x[2])

# Check location within 5x5 table
def checkloc(x):
  if x[0]>=0 and x[0]<6 and x[1]>=0 and x[1]<6:
    print('Success')
    return x
  elif x==[None, None, None]:
    print('Failed')
  else:
    print('Failed')
  return 

def runThis():
  x = place(0, 0, 'NORTH')
  x = right(x)
  x = move(x)
  x = move(x)  
  x = right(x)
  report(x)

runThis()
