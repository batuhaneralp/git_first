def getEmail():
    print("Email received...")


def postEmail():
    # .....

    print("Email sent...")


def main():
    print("1 - Ünbox")
    print("2 - New")
    q = int(input("Seçim = "))
    if q == 1:
        getEmail()
    elif q == 2:
        postEmail()
    else:
        print("Yanlış tercih")


main()
