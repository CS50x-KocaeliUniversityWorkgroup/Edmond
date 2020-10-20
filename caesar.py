from sys import argv
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# get the whole alphabet and get the lowercase letters too
# tum alfabeti dizi seklinda tanimla ve alfabetin kucukleri de al
alphabet_lower = [letter.lower() for letter in alphabet]

# change the text
# sifrele
def convert(plain, num):
    ciphertext = []
    for letter in plain:
        if letter in [".", "," ," ", "!"]:
            ciphertext.append(letter)
            continue
        if not letter.islower():
            index = (alphabet.index(letter) + num) % 26
            ciphertext.append(alphabet[index])
        else:
            index = (alphabet_lower.index(letter) + num) % 26
            ciphertext.append(alphabet_lower[index])
    return ("".join(ciphertext))

def main():
    # be sure of right usage
    # dogru kullanimdan emin olun
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: ./caesar key")
        exit(1)

    plain = input("plaintext: ")
    # get input
    # girdi al

    ciphertext = convert(plain, int(argv[1]))
    print("ciphertext:", ciphertext)
    # print output
    # cikti yazdir

    exit(0)

if __name__ == "__main__":
    main()
