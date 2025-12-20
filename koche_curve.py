import matplotlib.pyplot as plt

DERINLIK = 4 

# Recursive Fonksiyon
def koch_ciz(p1, p2, derinlik):
    if derinlik == 0:
        # Base Case
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='cyan', lw=1)
        return

    # Şimdiki çizginin vektör farkları
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    # Çizgiyi 3'e bölen noktalar (1/3 ve 2/3 noktaları)
    p3 = (p1[0] + dx / 3, p1[1] + dy / 3)
    p5 = (p1[0] + 2 * dx / 3, p1[1] + 2 * dy / 3)

    # Tepe noktası (p4) Hesabı - Lineer Cebir (Dönme)
    # Bir vektörü 60 derece döndürme formülü:
    # x' = x*cos(60) - y*sin(60)
    # y' = x*sin(60) + y*cos(60)
    # cos(60) = 0.5, sin(60) ~ 0.866
    
    vec_x = p5[0] - p3[0] 
    vec_y = p5[1] - p3[1] 
    
    p4_x = p3[0] + vec_x * 0.5 - vec_y * 0.866
    p4_y = p3[1] + vec_x * 0.866 + vec_y * 0.5
    p4 = (p4_x, p4_y)

    # Fonksiyon 4 yeni parça için kendini tekrar çağırır
    koch_ciz(p1, p3, derinlik - 1)
    koch_ciz(p3, p4, derinlik - 1)
    koch_ciz(p4, p5, derinlik - 1)
    koch_ciz(p5, p2, derinlik - 1)

# Grafiği Çizdirme
plt.figure(figsize=(8, 8)) 

# Kar tanesi oluşturmak için 3 tane Koch eğrisini üçgen şeklinde birleştiriyoruz
A = (0, 0)
B = (10, 0)
C = (5, 8.66)

koch_ciz(A, C, DERINLIK)
koch_ciz(C, B, DERINLIK)
koch_ciz(B, A, DERINLIK)

plt.title(f"Koch Kar Tanesi (Derinlik: {DERINLIK})")
plt.axis('equal')
plt.axis('off')
plt.show()