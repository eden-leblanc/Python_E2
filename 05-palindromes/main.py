"""Programme principal pour tester la fonction ispalindrome."""
#### Fonction secondaire


def ispalindrome(p: str) -> bool:
    """Renvoie True si la chaîne p est un palindrome, False sinon."""
    if p[::-1] == p:
        return True
    return False



def main() -> None:
    """appel main pour tester la fonction ispalindrome."""

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
