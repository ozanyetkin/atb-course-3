# Size verilen tamsayı listesinden azalan sayıların olduğu indexlere
#  yerinde "-" yazan artanlara ise "+" , sabit kalanlara 0 yeni bir liste oluştur.
# Sonrada değişim olan yerleri tepe,mono,yamaç veya çukur yazarak işaretle.
# + dan - ye geçmişse tepe durumudur.
# - den + ya geçmişse çukurdur
# Herhangi biri 0 ise yamaçtır.
# 0 yoksa be değişimde olmamışsa mono yazmalıyız.
girdi=[3,4,5,4,4,2,4,5]
# cevap=[+,+,-,0,-,+,+]
#cevap_2=["mono","tepe","yamaç","yamaç","çukur","mono"]
monocitiy=[]
for i in range(len(girdi)-1):
    if girdi[i]<girdi[i+1]:
        monocitiy.append("+")
    if girdi[i]==girdi[i+1]:
        monocitiy.append("0")
    if girdi[i]>girdi[i+1]:
        monocitiy.append("-")
landmark=[]
for e in range(len(monocitiy)-1):
    if monocitiy[e]=="0" or monocitiy[e+1]=="0":
        landmark.append("yamaç")
    elif monocitiy[e]==monocitiy[e+1]:
        landmark.append("mono")
    elif monocitiy[e]=="+" and monocitiy[e+1]=="-":
        landmark.append("tepe")
    else:
        landmark.append("çukur")
print(landmark)
    