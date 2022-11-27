#Kullanıcıdan pozitif tamsayı alın.
#Bu sayının bölenlerini yazdırın.Bölen sayısını bulup çift mi tekmi yazdırın
sayı=int(input("Sayıyı ver"))
bölsayı=0
for i in range(1,sayı):
    if sayı%i==0:
        print(i)
        bölsayı+=1
if bölsayı%2==0:
    print("Bölen sayısı çifttir")
else:
    print("Tektir")