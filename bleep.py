# @muhammedzahit arkadasimizin kodu
from cs50 import get_string
from sys import argv
# get the functions / fonskiyonlari al

# make the new func / yeni fonk tanimla
def censoring(text):
    censor = []
    for i in range(len(text)):
        censor.append("*")
    return "".join(censor)

def main():

    if len(argv) != 2:
        print("Usage: python bleep.py dictionary")
        exit(1)

    with open(argv[1],"r") as file:
        string = input("What message would you like to censor: ")
        texts = string.split()
        for i in range(len(texts)):
            for j in file:
                if j.strip("\n") == texts[i].lower():
                    texts[i] = censoring(texts[i])
                    break
            # go back to the beginning of file / dosyanın basina donduk
            file.seek(0)
        print(" ".join(texts))

    exit(0)

if __name__ == "__main__":
    main()
