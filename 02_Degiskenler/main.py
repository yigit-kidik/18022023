# Yorum satırı

# Bu sistem berbat çalışıyor(Yorum)

"""
Yorum satırı çok satırlı

DEĞİŞKENİN ADI = DEĞER  => SAYI KARAKTER YAZI MANTIKSAL İFADE VE VERİ TİPİ
"""

# DEĞİŞKEN TANIMLAMA KURALLARI
"""
1 - DEĞİŞKENİN_ADI
2 - CASE  ahmet Ahmet
3 - if print while ... gibi
4 - Sayı ile başlayamaz (5adi => adi5)
5-  Aralarda boşluk olamaz (ad soyad  => ad_soyad , adSoyad adsoyad)   
"""

# TODO Burası sonra yapılacak

# İsimlendirme Standartları

"""
1- camelCase => C# Java
2- snake_case => Python , JS ,TS
3- PascalCase => C#, Java
4- UPPERCASE => UPPER_CASE => Bütündillerde ama sadece sabitler için
5- kebap-case => her dilde kullanılabilir
"""
### VERİ Tipleri
# Tam sayılar, noktalı sayılar, mantıksal ifadeler, listeler, sözlükler
# demetler ...vb.

#
# yas: int = 30  # Tam sayı (int) Tipi belirtme
#
# isim = "Mehmet Nuri"  # Karakter listesi (str) Tip otomatik algılansın
#
# karakter: str = 'A'
#
# print(yas)
# print(isim)
# print(karakter)


# # TAM SAYI (INT)

# - sonsuz   => +sonsuz

"""
sayi = 12
print(sayi)

sayi_2 = 999
print(sayi_2)

sayi_3: int = 1450
print(sayi_3)

# Tip öğrenme
tip = type(sayi_2)
print(tip)
"""
"""

# NOKTALI SAYILAR (Float, Double)
sayi_1 = 20.05
print(sayi_1)
print(type(sayi_1))

sayi_2: float = 14.2
print(sayi_2)

sayi = int("12")  # TİP Dönüştürme
print(type(sayi))

sayi_3 = float("12.2")
print(type(sayi_3))
"""

# # # Metinsel Veri Tipi (STRING)
#
# ad = "Mehmet Nuri"
# soyad = 'Öztürk'
# meslek = """
#         Mühendis
# """
# print(ad)
# print(soyad)
# print(meslek)
# print(type(ad))
#
# """
# Yorum
# """

# # Mantıksal Veri Tipi (Boolean -> bool ) True False
# araba_var_mi = True  # Doğru 1
# ucagi_var_mi = False  # Yanlış 0
# i_phone_sahip_mi: bool = False
# print(type(araba_var_mi))

### '=' değer atama operatörümüzdür.

# Özel Notlar
# a = b = c = 12  # birden fazla değişken tanımlama ve tek değer atama yöntemi
# print(a)
# print(b)
# print(c)
#
# c, d, e = 13, 14.2, "Elma"  # birden fazla değişken tanımlama ve farklı değer atama yöntemi
# print(c)
# print(d)
# print(e)
#
# print(id(a)) # değişkenin ramdeki adresini belirtir
# print(id(b))
# print(id(c))
#
# print(id(c))
# print(id(d))
# print(id(e))
#
"""
a = 6
b = a
a = 7
b = a

print(b)
print(a)
"""
# Kullanıcıdan bilgi almak

ad = input("Adınız:")  # Önemli not!!! input değerleri sürekli str gelir
print(ad)

yas = int(input("Yaşınız:"))
print(yas)

maas = float(input("Maaşınız: "))
print(maas)
