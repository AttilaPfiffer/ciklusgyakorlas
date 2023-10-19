def feladat1():
    print("1. feladat")
    szam1: int = int(input("Adjon meg egy pozitív egész számot: "))
    szam2: int = 1
    while (szam2 <= szam1):
        if szam2 == szam1:
            print(f"{szam2}", end = " ")
        else:
            print(f"{szam2}", end = "; ")  
        szam2 += 1

def feladat2():
    print("\n")
    print("2. feladat")
    szam1: int = int(input("Adjon meg egy pozitív egész számot: "))
    i: int = 1
    osszeg:int = 0
    while(i <= szam1):
        if szam1 % i == 0:
            print(i)
            osszeg += i
        i += 1
    print("Az összeg: " + str(osszeg))

def feladat3():
    print("3. feladat")
    szam1:int = int(input("Adjon meg egy pozitív egész számot: "))
    szam2:int = int(input("Adjon meg még egy pozitív egész számot: "))
    i:int = szam1
    while (szam2 >= i):
        if i % 2 == 0:
            print(i)
        i += 1

def feladat4():
    print("4. feladat")

