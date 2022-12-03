#Kullanıcıdan bir pozitif tam sayı al. Diyelimki n.
"""
Terminale bunu yazdır:
1
22
333
....
nnnnnnn --> n tane
....
333
22
1
"""
"""
n=int(input("Tekrar sayısını giriniz:"))
for birim in range(1,n+1):
    satır=""
    for _ in range(birim):
        print(birim,end="")
    print("")
for birim in range(n-1,0,-1):
    satır=""
    for _ in range(birim):
        print(birim,end="")
    print("")
"""
n=int(input("Tekrar sayısını giriniz:"))
for birim in range(1,n+1):
    print(str(birim)*birim)
for birim in range(n-1,0,-1):
    print(str(birim)*birim)
