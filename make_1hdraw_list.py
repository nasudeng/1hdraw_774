import random
import pickle
import statistics
import itertools

def makelist():
  lis = [[random.randint(0,len(talents)-1) for i in range(3)] for i in range(100)]

  lis_notdup = []

  for ii in lis:
    if ii[0]!=ii[1] and ii[1]!=ii[2] and ii[2]!=ii[0]:
      lis_notdup.append(sorted(ii))
  lis_fin = [lis_notdup[0]]

  for ii in lis_notdup:
    flag = 0
    for tt in range(3):
      flag += int(ii[tt] in lis_fin[-1])

    if flag<1:
      lis_fin.append(ii)

  return lis_fin[0:31]

if __name__=="__main__":


    while(True):
      liss = makelist()
      std = statistics.stdev(itertools.chain.from_iterable(liss))
      d = 0.00001
      if (std < (6.493586579592718*(1+d))) and (std > (6.493586579592718*(1-d))):
        break

    with open("May2020",mode="wb") as file:
        pickle.dump(liss,file)
    with open("May2020.txt",mode="w") as file:
        file.write(str(liss))

    print("\007")
