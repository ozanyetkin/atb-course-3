#Size 2 tane tarih veriliyor. Aralarında kaç gün olduğunu bulun.
#Her ayı 30 gün kabul edin. Her yıl 360 gün kabul edin.
tarih_1=[12,4,2007]
tarih_2=[5,8,2012]
günfarki=tarih_1[0]-tarih_2[0]
ayfarki=(tarih_1[1]-tarih_2[1])*30
yilfarki=(tarih_1[2]-tarih_2[2])*360
günfarki+=(ayfarki+yilfarki)
print(günfarki)
# Günün pozitif olmasını sağla ve hangi tarih daha önce olduğunu söyle

