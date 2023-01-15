#Alfabeden alfabeye rastgele bir permütasyon (bire bir örten fonksyion) üreten bir fonksiyon yazınız.
alfabe=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import random
#permu_1=permu(alf)
#permu_1(alf[3])-->alf[19]
def permu_s(alf):
    uzunluk=len(alf)
    realperm=[i for i in range(uzunluk)]
    for _ in range(uzunluk):
        realperm.append(realperm.pop(random.randint(0,uzunluk-1)))
    def permutasyon(index):
        return realperm[index]
    return permutasyon

def permu(alf):
    permutasyon_s=permu_s(alf)
    def permutasyon(s):
        return alfabe[permutasyon_s(alf.index(s))]
    return permutasyon
rast_1=permu(alfabe)
uzunluk=len(alfabe)
print([alfabe.pop(random.randint(0,len(alfabe)-1)) for _ in range(uzunluk)])
#Verilen bir yazıyı bu permütasyona göre şifreleyen bir fonksiyon yazınız.
#Verilen yazıdaki karakterlerin frekanslarını bulan bir fonksiyon yazınız.
#Verilen yazıyı eşit parçalayan ve her parçayı rastgele bir permütasyonla şifreleyen bir fonksiyon yazınız.
#Verilen yazının şifrelenmiş halindeki karakter frekansları eşit olacak şekilde şifreleyen bir fonksiyon yazınız.

