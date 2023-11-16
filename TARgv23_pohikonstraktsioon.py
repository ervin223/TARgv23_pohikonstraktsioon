print("Tere tulemast".center(50))
kool = input("\tMis koolis sa opid?: ").capitalize()  # str Kool
kursus = int(input("\tMis kuursusel?: "))  # int kursus
print("Tere tulemast kooli " + kool.upper() + "\nOle hea " + str(kursus) + ".kursuse opilaseks!")  # kool on KOOL
print("Tere tulemast kooli", kool.lower(), "!\nOle hea", kursus, ".kursuse opilaseks!")  # kool="tthk"
print("Tere tulemast kooli {0}!\nOle hea {1}. kuursuse opetajaks!".format(kool, kursus))  # kool="tthk"
print(type(kool))
print(type(kursus))

arv1=float(input("Arv 1: "))
arv2=float(input("Arv 2: "))