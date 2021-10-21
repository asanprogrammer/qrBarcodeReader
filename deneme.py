#Kullanacağımız dosyaları import edelim
import cv2
from pyzbar.pyzbar import decode

def BarcodeReader():
    ## Kamerayı Başlatalım
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    #Döngüye Alalım ki Programı sonlandırabilelim veya devam edebilelim
    while True:
        ## Kameradaki Görüntüyü anlık olarak yakalaylım ve img'e çevirelim
        s, img = cam.read()

        """
        Burada ise istersek kamerayı ekrana verelim ama barkod okuyucu yaptığımızdan dolayı tercih etmiyoruz
        cv2.namedWindow("barcode", 1)
        cv2.imshow("barcode", img)
        cv2.waitKey(2)
        cv2.destroyWindow("barcode")
        """

        #Burada img olarak aldığımız görüntüyü decode methodu ile işleme alalım
        detectedbarcodes = decode(img)

        #Burada ise decode komutundan dönen sonuca göre barkod tespit edilmedi ise continue komutu ile devam edelim
        if not detectedbarcodes:
            continue
        #Burada barkod tespit edildi ise döngüye sokalım.
        else:
            for barcode in detectedbarcodes:
                (x, y, w, h) = barcode.rect
                #Burada ise tesip edilen barkod kodunu ekrana yazdıralım
                print(barcode.data)
            #Buradaki ;continue komutu ile {white True} döngümüzü başa alalım ki yeni barkodlar okutabilelim
            continue

#Aşağıdaki koşul ise dosyayı bir nevi korumalı yaparak başka bir dosya içine import edildiğinde çalışmamasını sağlar
if __name__ == "__main__":
    #Burada ise oluşturduğumuz fonksiyonu çağırarak programımızı başlatıyoruz
    BarcodeReader()

#asanprogrammer



