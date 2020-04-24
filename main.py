from email_receiver import getEmail
from email_sender import postEmail


def main():
    print("1 - Inbox")
    print("2 - New")
    q = input("Seçim = ")
    if q == "1":
        getEmail()
    elif q == "2":
        postEmail()
    else:
        print("Yanlış tercih")


main()
