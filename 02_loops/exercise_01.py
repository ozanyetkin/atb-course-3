# Al bu takatukaları takatukacıya götür. Takatukacı bu taka tukaları
#  takatukalatmazsa al bu takatukaları takatukacıdan takatukalatmadan geri getir.
#Tekerlemesindeki t ve k harflerinin sayısını bul.
t_sayı=0
k_sayı=0
tekerleme="Al bu takatukaları takatukacıya götür. Takatukacı bu taka tukaları takatukalatmazsa al bu takatukaları takatukacıdan takatukalatmadan geri getir."
for harf in tekerleme:
    if harf=="t":
        t_sayı+=1
    elif harf=="k":
        k_sayı+=1
print("t harfinden bu kadar var : "+str(t_sayı))
print("k harfinden bu kadar sayıda var: "+str(k_sayı))
