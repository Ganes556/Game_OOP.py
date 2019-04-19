from time import sleep
import random
import sys
import time
def mengetik(s,d1):
    print(d1)
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
    print(d1)
kalimat = "^_- Ini adalah game attack By Ganes semoga terhibur -_^"

decor = "="*len(kalimat)
mengetik(kalimat,decor)
sleep(1)
class Hero:
    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
    def serang(self,musuh):
        serangan = "-" + self.name + " menyerang " + musuh.name + "-"
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
print("1) kenji : " + str(kenji.__dict__)+"" )
print("2) zymeth : "+ str(zymeth.__dict__) +"")
pilih = input("masukan pilihan >> ")
sleep(2)
def client(pilih):
    global kenji , zymeth
    if pilih == "1" or pilih == "01":
        serangan = input("serang sekarang ?(Tekan enter) ")
        kenji.serang(zymeth)
        while True:
            if zymeth.health <= 0:
                print("zymeth mati")
                break
            serangan = input("serang lagi ?(Tekan enter) ")
            kenji.serang(zymeth)
        
    elif pilih == "2" or pilih == "02":
        serangan = input("serang sekarang ?(Tekan enter) ")
        zymeth.serang(kenji)
        while True:
            if kenji.health <= 0:
                print("kenji mati")
                break
            serangan = input("serang lagi ?(Tekan enter) ")
            zymeth.serang(kenji)
client(pilih)
