#Gereklilikleri import edelim
import cv2
from pyzbar.pyzbar import decode
import time


#Fonksiyonumuzu Oluşturalım
def BarcodeReader():
    while True:
       #Kameramızı başlatalım
        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        
        while True:    
            #Kameramızdaki görüntüyü anlık olarak alalım
            s, img = cam.read()

            #Aldığımız görüntüyü decode mothodu ile parçalayalım
            detectedbarcodes = decode(img)

            #Barkod yoksa pass geçelim 
            if not detectedbarcodes:
                pass

            #Barkod var ise döngüye alalım ve veriyi ve tipini yazdıralım
            else:
                for barcode in detectedbarcodes:
                    print(barcode.data)
                    print(barcode.type)
                #Yeni taramalar yapabilmek için continue ile başa saralım
                continue
        

#Buradaki koşul ile bu dosyanın başka dosyalara import edildiğinde çalışmamasını sağlayalım
if __name__ == "__main__":
    #Oluşturduğumuz fonksiyonu çağıralım
    BarcodeReader()



