def rotateMatrix(matrix):
  matrix.reverse() #? reverse horiaontal
  for i in range(len(matrix)): matrix[i].reverse() #? reverse vertical 

def spiral(matrix):
  string = ''
  mode = 'hor'
  while len(matrix):
    if mode == 'hor':
      for x in matrix[0]:
        string += x
      matrix.remove(matrix[0])
      mode = 'vert'
    elif mode == 'vert':
      for y in range(len(matrix)):
        string += matrix[y].pop()
      rotateMatrix(matrix)
      mode = 'hor'
  return string


if __name__ == "__main__":
  matrix = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']
  ]
  print(spiral(matrix))