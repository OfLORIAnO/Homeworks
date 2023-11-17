def checkPair(a):
  d = dict() 
  for elem in a:
    key = ''.join(sorted(elem))
    if (key in d.keys()):
      d.get(key).append(elem) #? Я афигел, когда узнал, что ссылку при get() отдаёт
    else: 
      d[key] = [elem]
  return list(d.values())

if __name__ == "__main__":

  a = [
  'wqe','qwe', "ewq", 'dsa', 
  'dsas','asd' , 'qwee', 'zxc', 'cxz', 
  'xxz','z','s', 'qweasdzxc', 
  'zzxc'
  ]

  print(checkPair(a))