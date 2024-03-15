Types = input("Sélectionnez un type en minuscule : ")

if Types == "plante":
    print("C'est un Pokémon de type Plante.")
    print("Je vous conseille Florizard, qui est un excellent Pokémon de type Plante.")
elif Types == "feu":
    print("C'est un Pokémon de type Feu.")
    print("Je vous conseille Dracaufeu, qui est un excellent Pokémon de type Feu et Vol.")
elif Types == "eau":
    print("C'est un Pokémon de type Eau.")
    print("Je vous conseille Tortank, qui est un excellent Pokémon de type Eau.")
else:
    print("Type non reconnu. Veuillez choisir parmi les types suivants : plante, feu, eau.")
