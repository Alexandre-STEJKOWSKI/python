mdp = 2004
tentative = 0

while tentative < 3 :
    mdp = input("sasir mdp :")
    if mdp == mdp :
        print("accés autorisé")
        break
    else :
        print("Accés non autorisé")

    if tentative <= 3 :
        print("compte bloqué")

mdp(tentative)







