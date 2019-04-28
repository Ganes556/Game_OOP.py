from time import sleep
import random
import sys

def mengetik(s,time):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(random.random() * time)
time = 0.1
kalimat = "^_- Ini adalah game attack By Ganes semoga terhibur -_^"
print("="*len(kalimat))
mengetik(kalimat,time)
print("="*len(kalimat))

sleep(1)
class Hero:
    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
    def serang(self,musuh):
        serangan = ">> " + self.name + " menyerang " + musuh.name + " <<"
        panjangDekor = len(serangan)
        print("="*panjangDekor)
        print(serangan)
        print("="*panjangDekor)
        musuh.diserang(self,self.power,musuh.armor)
    def diserang(self,musuh,attackPower_musuh,armor):
        print(self.name," diserang",musuh.name)
        attack_diterima = attackPower_musuh-armor
        print("serangan diterima : "+self.name+" " + "-"+str(attack_diterima)+"")
        self.health -= attack_diterima
        if self.health <=0:
            print("darah "+ self.name +" tersisa : 0 ")
        else:
            print("darah "+ self.name +" tersisa : ", self.health)
kenji = Hero("kenji",500,100,50)
zymeth = Hero("zymeth",300,200,25)
print("pilih karakter : ")
status = {"kenji":kenji.__dict__,"zymeth":zymeth.__dict__}
print("1). Kenji :")
for key,value in status["kenji"].items():
    if value != status["kenji"]["name"]:
        print("\t[*]",key,value )
print("2). zymeth :")
for key,value in status["zymeth"].items():
    if value != status["zymeth"]["name"]:
         print("\t[*]",key,value )
pilih = input("masukan pilihan >> ")
sleep(2)
def client(pilih):
    global kenji , zymeth
    kalimat = "Serang!........"
    time = 0.4
    if pilih == "1" or pilih == "01":
        serangan = input("serang sekarang ?(Tekan enter) ")
        mengetik(kalimat,time)
        kenji.serang(zymeth)
        print("\n")
        while True:
            if zymeth.health <= 0:
                print("zymeth mati")
                break
            serangan = input("serang lagi ?(Tekan enter)")
            mengetik(kalimat,time)
            print("\n")
            kenji.serang(zymeth)
       
        
    elif pilih == "2" or pilih == "02":
        serangan = input("serang sekarang ?(Tekan enter) ")
        mengetik(kalimat,time)
        print("\n")
        zymeth.serang(kenji)
        while True:
            if kenji.health <= 0:
                print("kenji mati")
                break
            serangan = input("serang lagi ?(Tekan enter) ")
            mengetik(kalimat,time)
            print("\n")
            zymeth.serang(kenji)
client(pilih)
