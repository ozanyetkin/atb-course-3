# Verilen tam sayı listesini [0,1] arasına taşıyan ve sıkıştıran
# bir fonksiyon yazınız.
def rescale(lst):
    lst.sort()
    minim=lst[0]
    shift=[x-minim for x in lst]
    maxim=shift[-1]
    scaled=[x/maxim for x in shift]
    return scaled
print(rescale([1,3,5,7,11,101,34,56]))