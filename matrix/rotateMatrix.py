def task1(matrix):
  newList = []
  for d in range(len(matrix)): # по горизонтали
      if(len(matrix) > len(matrix[d])):
        matrix[d].append(0)
      elif((len(matrix) < len(matrix[d]))):
        matrix.append([0]*len(matrix[d]))
  for i in range(len(matrix)): # по вертикали
    for j in range(i, len(matrix[i])): # по горизонтали
      if(len(matrix) > len(matrix[i])):
        matrix[i].append(0)
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

  for i in range(len(matrix)):
    if matrix[i] == [0]*len(matrix[0]):
      matrix.pop()
      continue
    elif matrix[i][len(matrix[i])-1] == 0:
      newList.append(matrix[i][0:len(matrix[i])-1])
      continue
  
  if (newList): return newList
  return matrix

if __name__ == "__main__":
  matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10,11, 12],
  ] 
  matrix2 = [
    [1, 2, 3],
    [5, 6, 7],
    [9, 10,11],
  ] 
  matrix3 = [
    [1, 2],
    [3, 4],
    [5, 6]
  ]
  print(task1(matrix))
  print("-----------------------------")
  print(task1(matrix2))
  print("-----------------------------")
  print(task1(matrix3))
  pass