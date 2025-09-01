import matplotlib.pyplot as plt
import os

print("🌍 İklim Değişikliği Anketine Hoşgeldiniz! 🌍\n")

# Önceki sonuçları saklayacak dosya
dosya_adi = "anket_sonuc.txt"

# Eğer dosya varsa eski cevapları oku
cevaplar = []
if os.path.exists(dosya_adi):
    with open(dosya_adi, "r") as f:
        for satir in f:
            cevaplar.append(satir.strip())

# Kendi cevaplarımızı tutacak liste
kendi_cevaplarim = []

# Sorular
s1 = input("Geri dönüşüm yapıyor musun? (Evet/Hayır): ")
cevaplar.append(s1.capitalize())
kendi_cevaplarim.append(s1.capitalize())

s2 = input("Arabayı mı yoksa bisikleti mi tercih edersin? (Araba/Bisiklet): ")
cevap2 = "Evet" if s2.lower() == "bisiklet" else "Hayır"
cevaplar.append(cevap2)
kendi_cevaplarim.append(cevap2)

s3 = input("Daha fazla ağaç dikmek ister misin? (Evet/Hayır): ")
cevaplar.append(s3.capitalize())
kendi_cevaplarim.append(s3.capitalize())

s4 = input("Boşuna açık lambaları kapatıyor musun? (Evet/Hayır): ")
cevaplar.append(s4.capitalize())
kendi_cevaplarim.append(s4.capitalize())

s5 = input("Pet şişe yerine matara kullanıyor musun? (Evet/Hayır): ")
cevaplar.append(s5.capitalize())
kendi_cevaplarim.append(s5.capitalize())

s6 = input("Plastik poşet yerine bez çanta kullanıyor musun? (Evet/Hayır): ")
cevaplar.append(s6.capitalize())
kendi_cevaplarim.append(s6.capitalize())

s7 = input("Evde tasarruflu ampul var mı? (Evet/Hayır/Bilmiyorum): ")
cevap7 = "Evet" if s7.lower() == "evet" else "Hayır"
cevaplar.append(cevap7)
kendi_cevaplarim.append(cevap7)

s8 = input("Çöpleri geri dönüşüm kutusuna atıyor musun? (Evet/Hayır): ")
cevaplar.append(s8.capitalize())
kendi_cevaplarim.append(s8.capitalize())

s9 = input("Çevreyi temiz tutuyor musun? (Evet/Hayır): ")
cevaplar.append(s9.capitalize())
kendi_cevaplarim.append(s9.capitalize())

s10 = input("Kağıtları önlü arkalı kullanıyor musun? (Evet/Hayır): ")
cevaplar.append(s10.capitalize())
kendi_cevaplarim.append(s10.capitalize())

s11 = input("Su tasarrufu yapmak doğayı korumak için önemli midir? (Evet/Hayır): ")
cevaplar.append(s11.capitalize())
kendi_cevaplarim.append(s11.capitalize())

# Sonuçları say
evet_sayisi = cevaplar.count("Evet")
hayir_sayisi = cevaplar.count("Hayır")

evet_sayim = kendi_cevaplarim.count("Evet")
hayir_sayim = kendi_cevaplarim.count("Hayır")

print("\nAnket Bitti! İşte sonuçlar:")
print("Tüm kullanıcılar - Evet:", evet_sayisi, "Hayır:", hayir_sayisi)
print("Kendi skorun - Evet:", evet_sayim, "Hayır:", hayir_sayim)

# ---- GRAFİKLER ----
etiketler = ["Evet", "Hayır"]

plt.figure(figsize=(12,5))

# 1. Grafik: Toplam sonuç
plt.subplot(1,2,1)
plt.bar(etiketler, [evet_sayisi, hayir_sayisi], color=['green', 'red'])
plt.title("Tüm Kullanıcıların Cevapları")
plt.xlabel("Cevaplar")
plt.ylabel("Kişi Sayısı")

# 2. Grafik: Kendi skorun
plt.subplot(1,2,2)
plt.bar(etiketler, [evet_sayim, hayir_sayim], color=['blue', 'orange'])
plt.title("Kendi Skorun")
plt.xlabel("Cevaplar")
plt.ylabel("Sayı")

plt.suptitle("🌱 İklim Değişikliği Anket Sonuçları 🌱")
plt.show()

# Güncel cevapları dosyaya kaydet
with open(dosya_adi, "w") as f:
    for cevap in cevaplar:
        f.write(cevap + "\n")


