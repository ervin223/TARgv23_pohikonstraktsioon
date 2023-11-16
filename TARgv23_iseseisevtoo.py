#1 ülesanne
print("Tere, maailm!")
name = input("Kirjuta oma nimi: ").capitalize()
print(f'Tere, maailm! Tervitan sind {name}')

age = input("Kui vana sa oled? ").strip()
print(f'Tere, maailm! Tervitan sind {name}! Sa oled {age} aastat vana.')

#2 ülesanne
vanus = 18 #int
eesnimi = "Jaak" #str
pikkus = 16.5 #float
kas_käib_koolis = True #bool


#3 ülesanne

count = int(input("Kui palju kommi on laua peal?"))
ate = int(input("Kui palju kommi sa sõid?"))
new = count - ate
print(f'Laua peal on veel {new} kommi.')


#4 ülesanne


c = int(input("Mis on puu läbimõõdu? "))
d = (c/(math.pi))
print(d)


#5 ülesanne

n = int(input())
m = int(input())
d = ((n**2)+(m**2))**0.5
print(d)


#6 ülesanne


aeg = int(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg

print("Sinu kiirus oli", int(kiirus), "km/h")


#7 ülesanne


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
avg = (a+b+c+d+e)/5
print(avg)


#8 ülesanne


print("    @..@")
print("   (----)")
print("  ( \__/ )")
print('  ^^ "" ^^' )


#9 ülesanne


a = int(input())
b = int(input())
c = int(input())

p = a + b +c 
print(p)


#10 ülesanne
cost = 12.9
print((cost*1.1)/2)


from math import *
print("Ruudu karakteristikud")
a=int(input('Sisesta ruudu kulje pikkus => '))
S=float(a**2)
print("Ruudu pindala", S)
P=float(4*a)
print("Ruudu umbermoot", P)
di=(2*(a**2))**0.5
print("Ruudu diagonaal", round(di,2))
print()
print("Ristkuliku karakteristikud")
b=int(input("Sisesta ristkuliku 1. kulje pikkus => "))
c=int(input("Sisesta ristkuliku 2. kulje pikkus => "))
S=b*c
print('Ristkuliku pindala', S)
P=2*(b+c)
print("Ristkuliku umbermoot", P)
di=(b**2+c**2)**0.5
print("Ristkuliku diagonaal", round(di, 1))
print()
print("Ringi karakteristikud")
r=float(input('Sisesta ringi raadiusi pikkus => '))
d=2*r
print("Ringi labimoot", d)
S = math.pi*(r**2)
print("Ringi pindala", round(S,2))
C= math.pi * r * 2
print("Ringjoone pikkus", round(C, 2))
