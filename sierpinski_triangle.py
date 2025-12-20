import matplotlib.pyplot as plt
import random

iterasyon_sayisi = 100000

# 1. Üçgenin Köşelerini Tanımla (x, y)
# Sol alt, Sağ alt ve Tepe noktası
koseler = [(0, 0), (10, 0), (5, 8.66)] 

# Başlangıç noktası (Üçgenin içinde rastgele bir yer)
x, y = 5, 4 

# Koordinatları saklamak için listeler
x_listesi = []
y_listesi = []

# Chaos Game Algoritması
for i in range(iterasyon_sayisi):
    # 1. Rastgele bir köşe seç
    secilen_kose = random.choice(koseler)
    
    # 2. Mevcut nokta ile o köşe arasındaki "orta noktaya" git
    # Formül: (Eski_X + Köşe_X) / 2
    x = (x + secilen_kose[0]) / 2
    y = (y + secilen_kose[1]) / 2
    
    # 3. Yeni noktayı kaydet
    x_listesi.append(x)
    y_listesi.append(y)

# Grafiği çizdirme
plt.figure(figsize=(10, 8))
plt.scatter(x_listesi, y_listesi, s=0.2, color='blue') 
plt.title("Sierpinski Üçgeni - Chaos Game Yöntemi")
plt.axis('off')
plt.show()