#Size 2 tane tarih veriliyor. Aralarında kaç gün olduğunu bulun.
#Her ayı 30 gün kabul edin. Her yıl 360 gün kabul edin.
tarih_1=[12,4,2007]
tarih_2=[5,8,2012]
günfarki=tarih_1[0]-tarih_2[0]
ayfarki=(tarih_1[1]-tarih_2[1])*30
yilfarki=(tarih_1[2]-tarih_2[2])*360
günfarki+=(ayfarki+yilfarki)

# Günün pozitif olmasını sağla ve hangi tarih daha önce olduğunu söyle
if günfarki<0:
    print(f"Tarih 2 tarih 1'den {günfarki*(-1)} gün ilerde.")
elif günfarki==0:
    print("Bu iki tarih aynı")
else: 
    print(f"Tarih 1 tarih 2'den {günfarki} gün ilerde.")
    




