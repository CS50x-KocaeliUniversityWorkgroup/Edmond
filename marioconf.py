from cs50 import get_int
# get function from CS50 library
# cs50 kutuphanesinden fonksiyon al

# make function for the pyramid
# piramidin yazdirilmasi icin fonksiyon
def print_func(char, iteration):
    for i in range(iteration):
        print(char,end="")

pyramide_height = get_int("Height: ")
#get input
#girdi al
while pyramide_height < 1 or pyramide_height > 8:
    pyramide_height = get_int("Height: ")

asterix = 1
space = pyramide_height-1

# make output
# cikti yazdir
for i in range(pyramide_height):
    print_func(" ",space)
    print_func("#",asterix)
    print("  ",end="")

    print_func("#",asterix)
    print()

    space -= 1
    asterix += 1
