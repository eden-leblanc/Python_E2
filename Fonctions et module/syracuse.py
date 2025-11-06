def syracuse(p):
    pass 

    suite = []
    if p <= 0: 
        print("Le nombre doit être strictement positif")
        return
    if p % 2 == 0:
        p = p / 2
        suite.append(p)
    else:
        p = 3 * p + 1
        suite.append(p) 
    


def main():
    n = 15
    tv, tva, am = syracuse(n)
    print(n, tv, tva, am)

if __name__ == "__main__":
    main()    