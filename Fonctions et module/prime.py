from math import sqrt

#### Fonction secondaire


def isprime(n):
    if n < 2 :
        return False
    for i in range (2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
            break
    return True
    pass

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
