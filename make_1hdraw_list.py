import random
import pickle
import statistics
import itertools
import collections

def makelist():

  while(True):
    lis = [[random.randint(0,len(talents)-1) for i in range(3)] for i in range(3)]
    chk_lis =  list(itertools.chain.from_iterable(lis))
    c = collections.Counter(chk_lis)
    if (max(c.values())) == 1:
      break

  lis_3days = lis.copy()

  while(True):


    while(True):
      lis_new = [random.randint(0,len(talents)-1) for i in range(3)]
      if lis_new[0]!=lis_new[1] and lis_new[1]!=lis_new[2] and lis_new[2]!=lis_new[0]:
        break

    lis_flat = list(itertools.chain.from_iterable(lis_3days))

    if not((lis_new[0] in lis_flat) or (lis_new[1] in lis_flat) or (lis_new[2] in lis_flat)):
      lis.append(lis_new)

      lis_3days.pop(0)
      lis_3days.append(lis_new)

    if len(lis) >= 31:
      break

  return lis



if __name__=="__main__":

    talents = []

    talents = ["日ノ隈らん","因幡はねる","宗谷いちか","風見くく","柚原いづみ","灰原あかね","白宮みみ","羽柴なつみ","黒猫ななし","堰代ミコ","周防パトラ","島村シャルロット","西園寺メアリ","灰猫ななし","獅子王クリス","龍ヶ崎リン","虎城アンナ","三毛猫ななし","杏戸ゆげ","鴨見カモミ","季咲あんこ","花奏かのん","銀猫ななし"]

    while(True):
      liss = makelist()
      chk_lis =  list(itertools.chain.from_iterable(liss))
      c = collections.Counter(chk_lis)

      if max(c.values())<=5 and min(c.values())>=3:
        break


    with open("June2020",mode="wb") as file:
        pickle.dump(liss,file)
    with open("June2020.txt",mode="w") as file:
        file.write(str(liss))

    print("\007")
