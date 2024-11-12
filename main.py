def kelimelerOlusturma(harfSayisi):
    import random
    harfler="abcdefghıijklmnoöprsştuüvyzABCDEFGHIİJKLMNOÖPRSŞTUÜVYZ"
    kelime=""
    for i in range(1, harfSayisi + 1):
        secilenHarf=random.sample(harfler,1)
        kelime+=secilenHarf[0]
    return kelime

for i in range(1, 6):
    rastgeleKelimeler=kelimelerOlusturma(10)
    print(rastgeleKelimeler)