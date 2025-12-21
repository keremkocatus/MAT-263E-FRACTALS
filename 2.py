import random
import math
import os
from PIL import Image, ImageDraw, ImageFont

class FinalLogoGenerator(object):
    def __init__(self, height=4000, color=(0, 180, 0), narrow_factor=0.55):
        # NOT: Height'i 4000 yaptık (Ultra Yüksek Çözünürlük)
        self.height = height
        self.width = int(height * 1.5) 
        self.color = color 
        self.narrow_factor = narrow_factor
        
        # Arka plan KOYU ANTRASİT (#1a1a1a)
        self.bg_color = (26, 26, 26, 255) 
        self.image = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
        self.pix = self.image.load()

    def scale_point(self, x, y):
        # Fractal çizim alanı margin'i (İç hesaplama için)
        margin = int(self.height * 0.05) 
        draw_w = self.width - (2 * margin)
        draw_h = self.height - (2 * margin)
        
        scale_x = (draw_w / 7.0) * self.narrow_factor 
        scale_y = draw_h / 10.0
        
        h = (self.width / 2.6) + (x * scale_x)
        k = (self.height - margin) - (y * scale_y)
        return int(h), int(k)

    def generate_fern(self, iterations=10000000, tilt_angle=-20):
        print(f"Master Kalite Render Başlıyor... ({iterations} nokta, {self.height}px yükseklik)")
        theta = math.radians(tilt_angle)
        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)
        
        # --- DEĞİŞİKLİK BURADA ---
        # Sap kalınlığı için değişken (Değeri artırırsan sap daha da kalınlaşır)
        stem_thickness = 0.04 
        # -------------------------

        x, y = 0, 0
        for i in range(iterations):
            if i % 1000000 == 0:
                print(f"İlerleme: {i // 1000000}M / {iterations // 1000000}M")

            rand = random.uniform(0, 100)
            
            # 1. DÖNÜŞÜM (SAP KISMI)
            if rand < 1:
                # Eski hali: x, y = 0, 0.16 * y  (Bu kılı gibi ince yapıyordu)
                # Yeni hali: x'e rastgele bir kalınlık veriyoruz
                x = random.uniform(-stem_thickness, stem_thickness)
                y = 0.16 * y
            
            elif rand < 86:
                x_new = 0.85 * x + 0.04 * y
                y = -0.04 * x + 0.85 * y + 1.6
                x = x_new
            elif rand < 93:
                x_new = 0.2 * x - 0.26 * y
                y = 0.23 * x + 0.22 * y + 1.6
                x = x_new
            else:
                x_new = -0.15 * x + 0.28 * y
                y = 0.26 * x + 0.24 * y + 0.44
                x = x_new
            
            x_rot = x * cos_theta - y * sin_theta
            y_rot = x * sin_theta + y * cos_theta
            
            px, py = self.scale_point(x_rot, y_rot)
            if 0 <= px < self.width and 0 <= py < self.height:
                self.pix[px, py] = (self.color[0], self.color[1], self.color[2], 255)

    def create_layout(self, text_part1="cod", text_part2="app", font_path="arial.ttf"):
        # 1. Şekli Kırp
        bbox = self.image.getbbox()
        fern_cropped = self.image.crop(bbox)
        fern_w, fern_h = fern_cropped.size
        
        # 2. Font Yükleme
        font_size = int(fern_h * 0.45) 
        try:
            font = ImageFont.truetype(font_path, font_size)
            print(f"Başarılı: '{font_path}' fontu kullanılıyor.")
        except IOError:
            print(f"UYARI: '{font_path}' bulunamadı! Varsayılan fonta dönülüyor.")
            font = ImageFont.load_default()

        # 3. Metin Boyutlarını Ölç
        dummy_draw = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
        
        w1 = dummy_draw.textlength(text_part1, font=font)
        bbox1 = dummy_draw.textbbox((0, 0), text_part1, font=font)
        h1 = bbox1[3] - bbox1[1]
        
        w2 = dummy_draw.textlength(text_part2, font=font)
        total_text_w = w1 + w2
        
        # --- AYARLAR ---
        scale_ratio = self.height / 1000.0
        
        # Yazı kaydırma
        manual_x_offset = int(-216 * scale_ratio)
        
        # Margin (Padding) Ayarı
        padding = int(200 * scale_ratio)

        # Final Genişlik: Sol Padding + İçerik + Sağ Padding
        final_w = int(fern_w + total_text_w + manual_x_offset + (padding * 2))
        final_h = max(fern_h, int(h1 * 1.5)) + (padding * 2)
        
        final_img = Image.new('RGBA', (final_w, final_h), self.bg_color)
        
        # 5. Çizim
        
        # İkonu Yerleştir
        icon_y = (final_h - fern_h) // 2
        final_img.paste(fern_cropped, (padding, icon_y), fern_cropped)
        
        draw = ImageDraw.Draw(final_img)
        
        # Yazı Y Konumu
        vertical_offset = int(fern_h * 0.10)
        text_y = ((final_h - h1) // 2) - bbox1[1] + vertical_offset
        
        # Yazı X Konumu
        start_x = padding + fern_w + manual_x_offset
        
        # "cod" -> Parlak Yeşil
        draw.text((start_x, text_y), text_part1, font=font, fill=self.color)
        
        # "app" -> Beyaz
        draw.text((start_x + w1, text_y), text_part2, font=font, fill=(255, 255, 255, 255))
        
        return final_img

# --- ÇALIŞTIRMA ---

# 1. AYAR: Yüksek Çözünürlük (4000px)
gen = FinalLogoGenerator(height=4000, color=(0, 180, 0), narrow_factor=0.55)

# 2. RENDER: 20 Milyon Nokta
gen.generate_fern(iterations=20000000, tilt_angle=-20)

# 3. FONT:
my_font = "./JetBrainsMono-ExtraBold.ttf" 

final_logo = gen.create_layout(text_part1="cod", text_part2="app", font_path=my_font)

# 4. KAYDETME
final_logo.save("codapp_MASTER_LOGO_ThickStem.png")
print("Logo tamamlandı: codapp_MASTER_LOGO_ThickStem.png")

# Önizleme
final_logo.resize((1000, int(1000 * final_logo.height / final_logo.width))).show()