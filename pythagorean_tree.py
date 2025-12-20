import matplotlib.pyplot as plt
import numpy as np 

MAX_DERINLIK = 10  
ACI = np.pi / 4  
KUCULME = 0.7

# Bu fonksiyon kendi kendini çağırarak dalları çizer.
def dal_ciz(x_basla, y_basla, uzunluk, aci, anlik_derinlik):
    # Durma Koşulu
    if anlik_derinlik == 0:
        return

    # 1. Mevcut dalın bitiş noktasını hesapla 
    x_bitis = x_basla + uzunluk * np.cos(aci)
    y_bitis = y_basla + uzunluk * np.sin(aci)

    # 2. Dalı çiz (Başlangıçtan bitişe bir çizgi çek)
    plt.plot([x_basla, x_bitis], [y_basla, y_bitis], color='brown', lw=anlik_derinlik)

    # Recursion
    # Yeni dallar daha kısa olacak
    yeni_uzunluk = uzunluk * KUCULME
    
    # Sağ Dalı Çiz
    dal_ciz(x_bitis, y_bitis, yeni_uzunluk, aci - ACI, anlik_derinlik - 1)
    
    # Sol Dalı Çiz
    dal_ciz(x_bitis, y_bitis, yeni_uzunluk, aci + ACI, anlik_derinlik - 1)

# Grafiği Çizdirme
plt.figure(figsize=(8, 8))

# Konum (0,0), Uzunluk 100, Açı 90 derece (yukarı), Maksimum derinlik
dal_ciz(0, -100, 100, np.pi/2, MAX_DERINLIK)

plt.title("Rekürsif Pisagor Ağacı İskeleti")
plt.axis('equal') 
plt.axis('off')
plt.show()