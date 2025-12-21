import random
from PIL import Image

class BarnsleyFern(object):
    def __init__(self, img_width, img_height, paint_color=(0, 100, 0),
                 bg_color=(255, 255, 255), margin=50, narrow_factor=0.6):
        
        self.img_width, self.img_height = img_width, img_height
        self.paint_color = paint_color
        self.margin = margin
        self.narrow_factor = narrow_factor # 1.0 normal, 0.5 yarı yarıya dar
        
        self.x, self.y = 0, 0
        self.age = 0

        self.fern = Image.new('RGB', (img_width, img_height), bg_color)
        self.pix = self.fern.load()
        
        # İlk noktayı çiz
        h, k = self.scale(0, 0)
        self.safe_draw(h, k)

    def scale(self, x, y):
        # Çizilebilir alanın genişliği ve yüksekliği (Marginleri çıkarıyoruz)
        draw_width = self.img_width - (2 * self.margin)
        draw_height = self.img_height - (2 * self.margin)
        
        # Matematiksel koordinatları ekran koordinatlarına çevirme
        # Eğrelti otunun matematiksel yüksekliği yaklaşık 10 birimdir (0'dan 9.99'a)
        # Genişliği ise yaklaşık 5 birimdir (-2.18'den 2.65'e)
        
        scale_x = (draw_width / 5.0) * self.narrow_factor # Yatay sıkıştırma burada yapılıyor
        scale_y = draw_height / 10.0
        
        # X'i ekranın tam ortasına hizala
        h = (self.img_width / 2) + (x * scale_x)
        
        # Y'yi aşağıdan yukarı doğru hizala (Ekran koordinatlarında Y=0 en üsttür)
        # Margin kadar aşağıdan başlatıyoruz
        k = (self.img_height - self.margin) - (y * scale_y)
        
        return int(h), int(k)

    def transform(self, x, y):
        rand = random.uniform(0, 100)
        if rand < 1:
            return 0, 0.16*y
        elif 1 <= rand < 86:
            return 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6
        elif 86 <= rand < 93:
            return 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6
        else:
            return -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44
            
    def safe_draw(self, h, k):
        # Sadece resim sınırları içindeki noktaları boya (Hata almamak için)
        if 0 <= h < self.img_width and 0 <= k < self.img_height:
            self.pix[h, k] = self.paint_color

    def iterate(self, iterations):
        for _ in range(iterations):
            self.x, self.y = self.transform(self.x, self.y)
            h, k = self.scale(self.x, self.y)
            self.safe_draw(h, k)
        self.age += iterations

# --- Kullanım ---
# 600x600 piksel, 50px kenar boşluğu, 0.55 daraltma faktörü (Daha ince olması için)
fern = BarnsleyFern(img_width=600, img_height=600, margin=50, narrow_factor=0.55)

fern.iterate(2500000) 

# Göster ve Kaydet
fern.fern.show()
fern.fern.save("logo_fern_final.png") # Kaydetmek istersen bunu açabilirsin