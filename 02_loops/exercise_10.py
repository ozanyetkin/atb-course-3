# Kullanıcıdan iki tam sayı al. İlk sayının rakamlarına ikinci sayı kadar kez 1 ekleyerek yeni sayı oluştur ve yazdır.
# Mesela 746->857->968->1079->21810->32921->431032
"""
print("takatuka"[0:4])
print("takatuka"[2:4])
print("takatuka"[0:4:2])
print(["t","a","k","a","tuka"][0:4:2])
print(["taka","tuka"][1][0:3])
"""
girdi,tekrar=input("Sayıyı ve tekrar sayısını giriniz").split(",")
tekrar=int(tekrar)

for _ in range(tekrar):
    sonraki=""
    for harf in girdi:
        sonraki=sonraki+str(int(harf)+1)
    girdi=sonraki
print(girdi)
    


