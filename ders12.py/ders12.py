class Person():
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        print("person oluştur")
    def ben_kimim(self):
        print("ben kişiyim")
class Teacher(Person):
    def __init__(self,lname,fname,branch):
        super().__init__(fname,lname)
        self.branch = branch
        print("teacher oluştu")
    def ben_kimim(self):
        print("ben öğretmenim")
class Student(Person):
    def __init__(self,fname,lname,number):
        self.number=number
        Person.__init__(self,lname,fname)
        print("student oluştu")
    def ben_kimim(self):
        print("ben öğrenci")
p1 = Person(fname="abdulkadir",lname="binan")
print(p1.lname)
t1 = Teacher(fname="fadimana",lname="aladağ",branch="sınıf ört")
print(t1)
s1 = Student(fname="ali",lname="koç",number=111)
print(s1)

p1.ben_kimim()
s1.ben_kimim()
t1.ben_kimim() #overrading

########################################

class Hesap:
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
    def sonucu_bul(self):
        pass
class Toplama(Hesap):
    def sonucu_bul(self):
        return self.sayi1+self.sayi2
class Cikarma(Hesap):
    def sonucu_bul(self):
        return self.sayi1-self.sayi2
class Carpma(Hesap):
    def sonucu_bul(self):
        return self.sayi1*self.sayi2
class Bolme(Hesap):
    def sonucu_bul(self):
        return self.sayi1/self.sayi2

t1 =  Toplama(sayi1=5,sayi2=3)
print(t1.sonucu_bul())
cikarma = Cikarma(sayi1=10,sayi2=3)
print(cikarma.sonucu_bul())
carpma = Carpma(16,12)
print(carpma.sonucu_bul())
bolme = Bolme(16,23333333)
print(bolme.sonucu_bul()
###################################
class Arac:
    def __init__(self,marka,model):
        self.marka = marka 
        self.model = model
    def arac_bilgisi(self):
    def bilgi(self):
        print(f"marka:{self.marka}madol:{self.model}")
class Motor:
    def __init__(self,motor_gucu):
        self.motor_gucu=motor_gucu
    def motor_bilgisi(self):
        print(f"motor gucu: {self.motor_gucu}")
class Araba(Arac,Motor):
    def __init__(self,marka,model,motor_gucu):
        Arac.__init__(self,marka,model)
        Motor.__init__(self,motor_gucu)
    def araba_bilgisi(self):
        self.motor_bilgisi()
        self.arac_bilgisi()
araba = Araba("toyoto","corollo",135)
araba.araba_bilgisi()

def ucgen(floyd):
    sayi = 1
    for i in range (1,sayi +1):
        for a in range (1,i +1):
            print (sayi, end=" ")
            sayi += 1
floyd=int(input("satır gir:"))
ucgen(floyd)


def floyd(satir):
    num=1
    for i in range(1,satir+1):
        for j in range (1,i+1):
            print(num,end=" ")
            num += 1
        print()
satir=int(input("satır gir:"))
floyd(satir)




