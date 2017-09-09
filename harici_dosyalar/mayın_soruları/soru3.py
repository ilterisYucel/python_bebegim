
#Bir yılın artık yıl olup olmadığını bulan ve
#2017 ile 2000 yıllarının artık olup olmadığını
#yazdıran aşağıdaki programı tamamlayınız.
def artik_yil(yil):
    if (yil % 4) == 0:
        if (yil % 100) == 0:
            if (yil % 400) == 0:
                print("{} artık yıldır.".format(yil))
            else:
                print("{} artık yıl değildir".format(yil))
        else:
            print("{} artık yıldır".format(yil))
    else:
        print("{} artık yıl değildir.".format(yil))
artik_yil(2017)
artik_yil(2000)