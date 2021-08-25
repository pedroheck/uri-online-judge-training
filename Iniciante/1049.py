carac1 = input()
carac2 = input()
carac3 = input()

if carac1 == "vertebrado":
    if carac2 == "ave":
        if carac3 == "carnivoro":
            print("aguia")
        if carac3 == "onivoro":
            print("pomba")
    if carac2 == "mamifero":
        if carac3 == "onivoro":
            print("homem")
        if carac3 == "herbivoro":
            print("vaca")
if carac1 == "invertebrado":
    if carac2 == "inseto":
        if carac3 == "hematofago":
            print("pulga")
        if carac3 == "herbivoro":
            print("lagarta")
    if carac2 == "anelideo":
        if carac3 == "hematofago":
            print("sanguessuga")
        if carac3 == "onivoro":
            print("minhoca")
