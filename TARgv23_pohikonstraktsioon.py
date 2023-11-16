from math import *
from xml.etree.ElementTree import PI

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
print("Summa {0} + {1}={2}".format(arv1,arv2,arv1+arv2))
print("Summa {0} - {1}={2}".format(arv1,arv2,arv1+arv2))
print("Summa {0} * {1}={2}".format(arv1,arv2,arv1+arv2))
print("Summa {0} / {1}={2}".format(arv1,arv2,arv1+arv2))
print("Summa {0} astmes {1} = {2}".format(arv1,arv2,arv1+arv2))
print("Summa {0} ja {1} jääk = {2}".format(arv1,arv2,arv1+arv2))
print("Summa {0} ja {1} jagamise täis osa {2}".format(arv1,arv2,arv1+arv2))

tehe=input("Mida teha: ")
v=eval(str(arv1)+tehe+str(arv2))
print(v)


print("Tere maailm")
nimi = input("Mis on sinu nimi")
print("Tere maailm! Tervitan sind {nimi}!".format(nimi)) #{переменная}

vanus = input("Kirjuta vanus")
print("Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana".format(nimi, vanus))

#2
vanus = 18 #int
eesnimi = "Jaak" #str
pikkus = 16.5 #float
kes_kaib_koolis = True #bool 

#3
komm = 3
qua = input("how many komm?")
print("laua peal on {komm}".format(komm))
komm = qua
print("nüüd laua peal on {komm}".format(qua))

#4
c=float(input("ümbermõtt"))
d=c/pi 
print("Läbimõtt",d)

#5
a=float(input("Esimene kateet"))
b=float(input("Teine kateet"))
d1=hypot(a,b)
print("d=",d)
print("d1=",d1)

try:
    a=int(input("a"))
except:
    print("Andmetüübi viga!") #если неверно, то...

#7
a1=randint(1,10)
a2=randint(1,10)
a3=randint(1,10)
a4=randint(1,10)
a5=randint(1,10)
print("arvude {a1},{a2},{a3},{a4} ja aretmeetiline keskmine {a5}".format({a1},{a2},{a3},{a4},{a5}))

#8
print("    @..@")
print("   (----)")
print("  ( \__/ )")
print(" ^^ "" ^^ ")

#9

#10
