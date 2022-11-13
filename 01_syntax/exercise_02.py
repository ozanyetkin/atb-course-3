# Kullanıcıdan adını ve soyadını aralarında bir boşluk olarak alıcaz.
#  ters sırada yazdırmak istiyoruz.
isimsoy=input("İsminizi soyisminizi aralarında bir boşluk bırakarak yazınız.")
ayrılmıs=isimsoy.split(" ")
ad=ayrılmıs[0]
soy=ayrılmıs[1]
print(soy+" "+ad)