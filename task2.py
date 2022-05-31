import random

ShortageCost = 100
HoldingCost = 50
SellingPrice = 450

profitlist = list()
x = list()


def RandNum_From_0to1():
    return random.uniform(0, 1)

def get_x():
  RandomProbapility=RandNum_From_0to1()
  if RandomProbapility>=0 and RandomProbapility<0.2:
       x=0
  elif RandomProbapility>=0.2 and RandomProbapility<0.6:
       x=1
  elif RandomProbapility>=0.6 and RandomProbapility<0.8:
       x=2
  elif RandomProbapility>=0.8 and RandomProbapility<0.9:
       x=3
  else :
       x=4
  return x

for i in range (500) :      #i is the Order
    x.append(get_x ())

for Order in range(1,3):         #Order is 1 or 2
    Avail_PC = 1
    for Week in range(500):
        Avail_PC += Order
        if x[Week]<Avail_PC:
            sold_PC = x[Week]
            Avail_PC -= x[Week]
            loss = Avail_PC * HoldingCost
        elif x[Week] > Avail_PC:
            sold_PC = Avail_PC
            Avail_PC = 0
            loss = (x[Week] - sold_PC) * ShortageCost
        else :
            sold_PC = x[Week]
            Avail_PC = 0
            loss = 0
        revenue = sold_PC * SellingPrice
        profit = revenue-loss
        if profit >= 0:
            profitlist.append(profit)
    if Order == 1:
        Average_Profit1 = sum(profitlist) / 500
        profitlist.clear()
    else :
        Average_Profit2 = sum(profitlist) / 500
        profitlist.clear()


#Print Info:
print("The AVG_profit of 500 weeks :", "\n")
print("The Avrege Profit ,When the shop owner ordered 1 PC per week =", Average_Profit1, "LE", "\n")
print("The Avrege Profit ,When the shop owner ordered 2 PC per week =", Average_Profit2, "LE", "\n")


if Average_Profit1 > Average_Profit2:
    print("Best decision orders 1 PC per week")
elif Average_Profit1 < Average_Profit2:
    print("Best decision orders 2 PC per week")