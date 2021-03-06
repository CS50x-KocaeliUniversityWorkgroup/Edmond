# Muhammed Zahid arkadasimizin kodu
# define the function
# fonksiyonu tanimla
def card_control(card_number):
    a, b = 0, 0
    flag = True
    for i in range(len(card_number)-1, -1, -1):
        if (flag):
            a += int(card_number[i])
            flag = False
        else:
            c = int(card_number[i])*2
            b += c // 10
            b += c % 10
            flag = True
    return (a+b)%10 == 0

# get and check input
# girdi al ve kontrol et
card_number = input("Card: ")
if card_number[0] == "-":
    card_number = input("Try again: ")
# if input is wrong ask for new input
# girdi yalnissa yeni bir girdi talep et
len_card = len(card_number)
# take card length
# kartin uzunlugunu al

# find the card's company
# kartin cinsiyetini bul
if (len_card < 13 or len_card > 16 or len_card == 14 or not card_control(card_number)):
    print("INVALID")
else:
    character = int(card_number[0:2])
    if character >= 50:
        print("MASTERCARD")
    elif character >= 40:
        print("VISA")
    elif character == 37:
        print("AMEX")
    else:
        print("AMERICAN EXPRESS")
