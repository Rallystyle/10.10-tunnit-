"""Matemaatilised tehted"""
import math

# küsime kasutajalt ujuvkomaarvu kujul kolmnurga kaatetid a ja b
#a = float(input("Sisesta oma a:"))
#b = float(input("Sisesta oma b:"))

# koosta muutuja a, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks
a = float(input("Sisesta oma a:"))
# koosta muutuja b, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks
b = float(input("Sisesta oma b:"))
# meie ülesandeks on leida hüpoteenus c, kolmnurga ümbermõõt ja pindala NB(vastused peavad olema ümardatud sajandikeni)

c = math.sqrt(a**2 + b**2)
p = (a +b + c)
S = (a * b)/2

print(f"Lahendid on: hüpotunuus={round(c,2)} ja ümbermõõt={round(p,2)} ja pindala={round(S,2)}")
