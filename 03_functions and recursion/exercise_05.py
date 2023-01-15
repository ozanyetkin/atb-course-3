# İki sayıyı * işaretini kullanmadan çarpan bir fonksiyon yazınız.
def çarp(a,b):
    sonuc=0
    for _ in range(b):
        sonuc+=a
    return sonuc
#Recursive çözüm
def fok(x,y):
	if y == 0:
		return 0

	if y > 0 :
		return x + fok(x, y - 1)

	if y < 0 :
		return -fok(x, -y)
	
print(fok(-5, 25))