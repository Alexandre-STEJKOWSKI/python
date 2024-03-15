identifiant = "Alexandre"
MDP = "2004"

print ("En connection")

user_id = input("Entrez votre indentifiant : ")
user_MDP = input("Entrez votre mot de passe : ")

    
    if user_MDP == MDP and identifiant == user_id :
        print("Accés Autorisé")
        print("Bienvenue" " " + user_id )
    else:
        MDP != user_MDP and identifiant != user_id # type: ignore
        print("Accés non Autorisé")
        print("Mot de passe ou identifiant incorecte")
        