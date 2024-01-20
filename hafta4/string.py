isim = "sefa"
soyad = "calis"
yas = "15" 
karsilama = "Benim Adim" +" "+" "+isim +" "+ soyad + " " + " " + "yasim" +" "+str(yas)+" "+ "hosgeldin"
print(karsilama)

uzunluk = len(karsilama)
print(uzunluk)

print(karsilama[36])
print=(uzunluk [-1])

print(karsilama[0:10])
print(karsilama[0:42])
print(karsilama[10:22])
print(karsilama[0:22])
print(karsilama[10:])
 print(karsilama[2:25:3])
print(karsilama[:-9])
print(karsilama[::-1])
print(karsilama[::-2])
karsilama_lower=karsilama.lower()
print(karsilama_lower)

karsilama_strip = karsilama.strip()
print(karsilama_strip)

karsilama_split = karsilama.split()
print(karsilama_split)
print(karsilama_split[2])

karsilama_join = "-".join(karsilama)
print(karsilama_join)

karsilama_find = karsilama.find("sefa")
print(karsilama_find)

karsilama_startswith = karsilama.startswith("s")
print(karsilama_startswith)

karsilama_endswith = karsilama.endswith("s")
print(karsilama_endswith)

karsilama_replace = karsilama.replace("sefa","calis")
print(karsilama_replace)
