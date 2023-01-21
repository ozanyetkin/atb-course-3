# Bir stringin içinde başka bir altstringin kaç kere görüldüğünü bulan fonksiyon yazalım.
# örneğin alalala içinde ala 3 kere var. lal 2 kere.
def substring(main,sub):
    count=0
    for i in range(len(main)-len(sub)+1):
        if main[i:i+len(sub)]==sub:
            count+=1
    return count
print(substring("alalala","ala"))
