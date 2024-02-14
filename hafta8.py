def faktöriyel(n):
    if n==0:
        return 1
    else:
        return n*faktöriyel(n-1)

sayi= 4
print(faktöriyel(sayi))


x = "global değişken"

def function ():
    x = "local değişken"
    print(x)
function()
print(x)


print(a) name error

int("a19") value error

print(10/0) sıfıra bolunme

print("hello"world)

try:
    x=int(input("x gir:"))
    y=int(input("y gir:"))
    print(x/y)
except ZeroDivisionError:
    print("sıfıra bolunmme hatası")
except ValueError:
    print("x ve y için sayısal değer gir")
else:

except Exception as ex:
    print("bilgiler yanlis",ex)


while True:
    try:
        x=int(input("x gir:"))
        y=int(input("y gir:"))
        print(x/y)
    except Exception as ex:
        print("bilgiler yanlis",ex)
    else:
        break
    finally:
        print("her sey yolunda")


try:
        x=int(input("x gir:"))
        y=int(input("y gir:"))
        print(x/y)
except ZeroDivisionError:
        print("sıfıra bölnme hatası")
import re
def parola_kontrol(parola):
    if len(parola)<8:
        raise Exception("parola en az 8 karakter")
    elif not re.search("[a-z]",parola):
        raise Exception("parola küçük haf içercek")
    elif not re.search("[A-Z]",parola):
        raise Exception("parola buyuk harf içercek")


password="1234"
try:
    parola_kontrol(password)
except Exception as ex:
    print(ex)
else:
    print("parola basarili")
