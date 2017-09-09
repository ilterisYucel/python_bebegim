
#çekoslovakyalılaştıramadıklarımızdanmısınız
#harf dizisinde her harften kaç tane olduğunu
#bulan ve '... harfinden ... tane vardır.'
#şeklinde yazdıran aşağıdaki programı tamamlayınız.
def harf_sayici(kelime):
    veri_sozlugu = {}
    for harf in kelime:
        if harf in veri_sozlugu.keys():
            veri_sozlugu[harf] += 1
        else:
            veri_sozlugu[harf] = 1
    for sozcuk, sayisi in veri_sozlugu.items():
        print("{} harfinden {} tane vardır.".format(sozcuk, sayisi))
harf_sayici("çekoslovakyalılaştıramadıklarımızdanmısınız")