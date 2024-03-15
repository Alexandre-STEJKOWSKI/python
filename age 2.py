age = input("Entrez un age :")
age = int(age)

if (age <= 18):
    print("Tu es trop jeune")
elif (age <= 50):
    print("tu es vieux")
elif (age >= 90):
    print("Tu va bientot mourir")