# Verilen tam sayı listesinden en küçük ve en büyük sayıları bulunuz.
"""
listem=input("Sayıları virgüller ayırarak giriniz").split(",")
en_büyük=int(listem[0])
en_küçük=int(listem[0])
for i in listem:
    if en_küçük>int(i):
        en_küçük=int(i)
    if en_büyük<int(i):
        en_büyük=int(i)
print(f"En büyük {en_büyük}, En küçük: {en_küçük}")
"""


listem=input("Sayıları virgüller ayırarak giriniz").split(",")
uzun=len(listem)
for i in range(uzun):
    listem[i]=int(listem[i])
en_büyük=listem[0]
en_küçük=listem[0]
for i in range(1,uzun):
    if en_küçük>listem[i]:
        en_küçük=listem[i]
    if en_büyük<listem[i]:
        en_büyük=listem[i]
print(f"En büyük {en_büyük}, En küçük: {en_küçük}")
