toplam=5
liste=[]
for i in range(toplam):
    deger = int(input("sayı gir"))
    if deger % 3 == 0:
        liste.insert(0,deger)
    else:
        liste.append(deger)
print("listenin son hali",liste)

class Kisi:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} {self.age}"
k1=Kisi(name="sefa",age=15)
print(k1)

class Soru:
    def __init__(self,soru,cevap):
        self.soru = soru
        self.cevap = cevap 
    def dogru_mu(self,tahmin):
        return self.cevap == tahmin  
soru1 = Soru("en panelci kim?:","PEKKA")
soru2 = Soru("en kalabalık şehir:","istanbul")
soru3 = Soru("en güzel şehir:","samsun")
dogru_cevaplar = 0
sorular=[soru1,soru2,soru3]
for i in sorular:
     cevap = input(i.soru)
     if i.dogru_mu(cevap):
        dogru_cevaplar +=1
print(f"doğru cevap sayısı: {dogru_cevaplar}")
