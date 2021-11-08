import math
while True:
    n1 = input("Anna ensimmäinen luku: ")
    try:
        n1 = int(n1)
        break
    except Exception:
        print("ei kirjaimia")
while True:
    n2 = input("Anna toinen luku: ")
    try:
        n2 = int(n2)
        break
    except Exception:
        print("ei kirjaimia")

while True:
    print("(1) + \n(2) - \n(3) * \n(4) / \n(5)sin(luku1/luku2) \n(6)cos(luku1/luku2) \n(7)Vaihda luvut \n(8)Lopeta")
    print("Valitut luvut: ", n1, n2)
    ch = int(input("Tee valinta (1-8): "))
    if ch == 8:
        break
    elif ch == 1:
        print("Tulos on: ", n1 + n2)
        pass
    elif ch == 2:
        print("Tulos on: ", n1 - n2)
    elif ch == 3:
        print("Tulos on: ", n1 * n2)
    elif ch == 4:
        print("Tulos on: ", n1 / n2)
    elif ch == 5:
        print(math.sin(n1/n2))
    elif ch == 6:
        print(math.cos(n1/n2))
    elif ch == 7:
        while True:
            n1 = input("Anna ensimmäinen luku: ")
            try:
                n1 = int(n1)
                break
            except Exception:
                print("ei kirjaimia")
        while True:
            n2 = input("Anna toinen luku: ")
            try:
                n2 = int(n2)
                break
            except Exception:
                print("ei kirjaimia")

