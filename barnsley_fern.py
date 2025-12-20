import matplotlib.pyplot as plt
import random

iterasyon_sayisi = 500000  
x, y = 0, 0

# Koordinatları tutacak listeler
x_listesi = []
y_listesi = []

# Algoritma
for i in range(iterasyon_sayisi):
    
    # 1 ile 100 arasında rastgele bir sayı seç (Olasılık için)
    sans = random.randint(1, 100)
    
    if sans == 1:
        # %1 Olasılık: Gövde (Stem)
        next_x = 0
        next_y = 0.16 * y
        
    elif sans <= 86:
        # %85 Olasılık: Ana Yapraklar (Successively smaller leaflets)
        next_x = 0.85 * x + 0.04 * y
        next_y = -0.04 * x + 0.85 * y + 1.6
        
    elif sans <= 93:
        # %7 Olasılık: Sol Yaprak
        next_x = 0.20 * x - 0.26 * y
        next_y = 0.23 * x + 0.22 * y + 1.6
        
    else:
        # %7 Olasılık: Sağ Yaprak (Geriye kalan %7)
        next_x = -0.15 * x + 0.28 * y
        next_y = 0.26 * x + 0.24 * y + 0.44

    # Koordinatları güncelle
    x = next_x
    y = next_y
    
    # Listeye ekle
    x_listesi.append(x)
    y_listesi.append(y)

# Grafik Çizdirme
plt.figure(figsize=(6, 9)) 
plt.scatter(x_listesi, y_listesi, s=0.2, color='green') 
plt.title("Barnsley Fern - Olasılıksal Fraktal")
plt.axis('off')
plt.show()