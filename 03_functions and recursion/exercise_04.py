# 4 nokta verildiğinde p1,p2,p3,p4  (p1,p2) nin tanımladıgı dogru (p3,p4) tanımladığı
#  doğruya dik ise True veren değilse False veren bir fonksiyon yazınız.
#fonk((0,0),(0,12),(0,0),(6,0)) gives True
#İpucu: (a,b),(x,y) nin tanımladığı vektörler ancak ve ancak a*x+b*y=0 ise diktirler.
def dot(p1,p2):
    return p1[0]*p2[0]+p1[1]*p2[1]
def dik(p1,p2):
    if dot(p1,p2)==0:
        return True
    else:
        return False
def fonk(p1,p2,p3,p4):
    vekt1=(p2[0]-p1[0],p2[1]-p1[1])
    vekt2=(p4[0]-p3[0],p4[1]-p3[1])
    return dik(vekt1,vekt2)
print(fonk((4,0),(0,12),(0,0),(6,0)))
