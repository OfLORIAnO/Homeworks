from itertools import product

def getMaxRoute(l):
  max = l[0]
  for i in range(1,len(l)):
    elem = l[i]
    if max[0] <= elem[0]:
      max = elem
  return max

def banks1():
  banksList = []

  n = int(input("Введите кол-во банков:"))
  for i in range(n):
    name = input("Введите название банка: ") 
    money = int(input("Введите деньги банка: "))
    banksList.append(tuple([name,money]))

  # banksList = [("bank1", 1),("bank2", 2),("bank3", 3),("bank4", 4),("bank5", 5),("bank6", 6),("bank7", 7),("bank8", 8)]
  # banksList = [("sber1", 100),("Tin1", 5),("Vol1", 4),("Ker1", 150),("Tin2", 3),("Vol2", 10)]
  
  validMasks = []
  for elem in product('01', repeat=len(banksList)):
    if '11' not in ''.join(elem) and not '000' in ''.join(elem):
      validMasks.append(''.join(elem))
  vhodAfter = []
  print("len", len(validMasks))
  for i in range(len(validMasks)):
    mask = validMasks[i]
    totalSum = 0
    route = []
    for j in range(len(mask)):
      if mask[j] == "1":
        totalSum += banksList[j][1]
        route.append(tuple([banksList[j][0], j+1]))
    vhodAfter.append([totalSum, route])
  print(getMaxRoute(vhodAfter))


def banks2():
  banksList = []

  n = int(input("Введите кол-во банков:"))
  for i in range(n):
    name = input("Введите название банка: ") 
    money = int(input("Введите деньги банка: "))
    banksList.append(tuple([name,money]))
  
  if len(banksList) == 2:
    if banksList[0][1] > banksList[1][1]:
      print([banksList[0][1], (banksList[0][0],0)])
    else:
      print([banksList[1][1], (banksList[1][0],1)])
    return
  
  sumBanks = [] #? Накапливаем тут только сумму
  visitedBanks = [] 
  for i in range(0, len(banksList)):

    if i < 2:
      sumBanks.append(max(banksList[0][1], banksList[1][1]))
      if i == 0:
        if banksList[0][1] > banksList[1][1]:
          visitedBanks.append(tuple([banksList[0][0], 1]))
        else:
          visitedBanks.append(tuple([banksList[1][0], 2]))
      continue

    curBank = banksList[i]

    prevBank= sumBanks[i-2]
    visBank = sumBanks[i-1]
    if visBank > curBank[1] + prevBank: #? Тут мы не заходим в банк
      sumBanks.append(visBank)
    else: #? Тут мы заходим в банк
      if(i == visitedBanks[len(visitedBanks)-1][1] and i > 2):
        # print(i+1)
        # visitedBanks.pop()
        pass
      visitedBanks.append(tuple([banksList[i][0], i+1]))
      sumBanks.append(curBank[1] + prevBank)
    
  print([sumBanks[len(sumBanks)-1]] + [visitedBanks])


if __name__ == '__main__':
  banks1()
  banks2()