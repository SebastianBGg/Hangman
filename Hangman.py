ord = input("Write a word\n").upper()
strek = ["- "] * len(ord)
w = 0
liv = 6
y = 1
b = -1
while y == 1:
    tap = 0
    print("Du har",liv,"liv\n")
    b = -1
    if liv == 6:
        print("  +---+\n"
        "  |   |\n"
        "      |\n"
        "      |\n"
        "      |\n"
        "      |\n")
    if liv == 5:
        print("  +---+\n"
        "  |   |\n"
        "  O   |\n"
        "      |\n"
        "      |\n"
        "      |\n")
    if liv == 4:
        print("  +---+\n"
        "  |   |\n"
        "  O   |\n"
        "  |   |\n"
        "      |\n"
        "      |\n")
    if liv == 3:
        print("  +---+\n"
        "  |   |\n"
        "  O   |\n"
        " /|   |\n"
        "      |\n"
        "      |\n")
    if liv == 2:
        print("  +---+\n"
        "  |   |\n"
        "  O   |\n"
        " /|\  |\n"
        "      |\n"
        "      |\n")
    if liv == 1:
        print("  +---+\n"
        "  |   |\n"
        "  O   |\n"
        " /|\  |\n"
        "   \   |\n"
        "      |\n")
    if liv == 0:
        print("  +---+\n"
        "  |   |\n"
        "  O   |\n"
        " /|\  |\n"
        " / \   |\n"
        "      |\n")
    svar = input("Si en bokstav\n").upper()
    if len(svar) <= 2:
        print(strek)
        print()
        for x in ord:
            b = b + 1
            if  x == svar:
                strek[b] = svar
                print("Du fikk riktig!\n")
                print(strek)
                w = w + 1
                if w == len(ord):
                    y = 0
            if x != svar:
                tap = tap + 1
                if tap == len(ord):
                    liv = liv - 1
                    print("Feil bokstav")
                    if liv == 0:
                        y = 0
       
    else:
        print("for mange bokstaver\n")
if w == len(ord):
    print("DU VANT!")
if liv == 0:
    print("Du tapte\n")