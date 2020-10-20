from cs50 import get_float
# get the function from library
# fonksiyonu al

#define the new function
#yeni fonk tanimla
def get_coin(money, coins):
    count = 0
    for coin in coins:
        count += money // coin
        money %= coin
    return int(count)

#take input
#girdi al
money = get_float("Owed: ")
while money < 0:
    money = get_float("Owed: ")
money *= 100
# mutliply by 100 to get coin money
# demir para elde etmek icin 100 ile carp

coins = [25,10,5,1]
# coins array 
# demir para dizisi

#print
#yazdir
print(get_coin(money, coins))
