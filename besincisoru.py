#5.soru
#öncelikle import karışık sayı atıyoruz
import random

def liste_tanimla():
    liste=[]
    liste=[random.randint(0,100) for x in range(8)]
    return liste
def liste_kup(liste):#listenin içindeki sayıların küplerini alıyoruz
    return[x**3 for x in liste]
def liste_sort(liste):#listeyi sıralıyoruz
    liste.sort()
    return liste
def liste_ekle(liste,num):#listeye numara ekliyoruz
    num=int(num)
    liste.append(num)
    return liste
def main():#burada listeye giriş alıyoruz ve sonucu gösteriyoruz
    liste=liste_tanimla()
    print(liste)
    menu=int(input("MENU\n1-listenin küpünü hesapla\n2-listeyi sırala\n3-listeye sayı ekle"))
    if menu==1:
        print(liste_kup(liste))
    elif menu==2:
        print(liste_sort(liste))
    elif menu==3:
        num=input("Eklenecek sayiyi giriniz: ")
        print(liste_ekle(liste,num))


main() #fonksiyonu çağırıyoruz
  