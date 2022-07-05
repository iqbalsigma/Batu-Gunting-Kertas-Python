from random import randint

t = ["Gunting", "Batu", "Kertas"]

computer = t[randint(0,2)]

player = False
poin_p = 0
poin_c = 0

print("Permainan Gunting, Batu Kertas")
while player == False:
    player = input("Batu, Kertas, Gunting?")
    if player == computer:
        print("Seri!")
    elif player == "Batu":
        if computer == "Kertas":
            print("Anda kalah!")
            poin_c+=1
        else:
            print("Anda menang!")
            poin_p+=1
    elif player == "Kertas":
        if computer == "Gunting":
            print("Anda kalah!")
            poin_c+=1
        else:
            print("Anda menang!")
            poin_p+=1
    elif player == "Gunting":
        if computer == "Batu":
            print("Anda kalah!")
            poin_c+=1
        else:
            print("Anda menang!")
            poin_p+=1
    else:
        print("Itu bukan permainan yang valid. Periksa ejaan Anda!")
    player = False
    if poin_p > 2 or poin_c > 3:
        player = True
    computer = t[randint(0,2)]

print("Hasil akhir (Pemain - Komputer) : ", poin_p, "-", poin_c)
