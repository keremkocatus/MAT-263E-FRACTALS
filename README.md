# 🌀 Fractals & Linear Algebra Applications

Bu proje, **Lineer Cebir** dersi **Module 2: Direct Methods** kapsamında hazırlanan "Fraktallar" konulu Learning Station (Öğrenme İstasyonu) projesinin yazılım ayağıdır.

Proje, matris dönüşümleri, özdeğerler (eigenvalues), iteratif yöntemler ve özyinelemeli (recursive) algoritmaların fraktal geometri oluşturmadaki gücünü görselleştirmek amacıyla Python diliyle geliştirilmiştir.

## 📂 İçerik ve Kodlar

Bu depoda (repository), 4 farklı fraktal üretim tekniğini gösteren Python scriptleri bulunmaktadır:

### 1. `sierpinski_chaos.py` (Sierpinski Üçgeni)

* **Yöntem:** Chaos Game (Kaos Oyunu).
* **Mantık:** Rastgele seçilen noktalar ve orta nokta kuralı ile kaostan düzenli bir geometrik yapı oluşturulması.
* **Lineer Cebir Kavramı:** İteratif nokta hesaplama.

### 2. `barnsley_fern.py` (Barnsley Eğrelti Otu)

* **Yöntem:** Probabilistic Affine Transformations (Olasılıksal İlgil Dönüşümler).
* **Mantık:** 4 farklı dönüşüm matrisinin belirli olasılık ağırlıklarıyla (%1, %85, %7, %7) seçilerek doğal bir bitki formunun simüle edilmesi.
* **Lineer Cebir Kavramı:** Matris çarpımı, vektör toplama ve olasılık ağırlıklı seçim.

### 3. `pythagorean_tree.py` (Pisagor Ağacı)

* **Yöntem:** Recursive Functions (Özyinelemeli Fonksiyonlar).
* **Mantık:** Bir karenin üzerine belirli açılarla küçülen karelerin (veya çizgilerin) eklenmesiyle oluşan ağaç yapısı.
* **Lineer Cebir Kavramı:** Dönme matrisleri (Rotation matrices - sin/cos) ve ölçeklendirme.

### 4. `koch_snowflake.py` (Koch Kar Tanesi)

* **Yöntem:** Vektörel Bölünme ve Rekürsiyon.
* **Mantık:** Düz bir çizginin her adımda 3'e bölünüp ortasına bir üçgen eklenmesi. Sonsuz çevre ve sonlu alan paradoksunu gösterir.
* **Lineer Cebir Kavramı:** Vektör öteleme ve 60 derece vektör döndürme işlemleri.

---

## 🚀 Kurulum ve Çalıştırma

Kodları çalıştırmak için bilgisayarınızda **Python 3** ve aşağıdaki kütüphanelerin yüklü olması gerekmektedir.

### Gereksinimler

Terminal veya komut satırına şu komutu yazarak kütüphaneleri yükleyebilirsiniz:

```bash
pip install matplotlib numpy

```

### Kodları Çalıştırma

Proje dizininde terminali açıp aşağıdaki komutları kullanabilirsiniz:

```bash
python sierpinski_chaos.py
python barnsley_fern.py
python pythagorean_tree.py
python koch_snowflake.py

```

---

## 🎯 Öğrenim Çıktıları (Learning Outcomes)

Bu proje, aşağıdaki akademik kazanımları desteklemektedir:

* **LObj2 (Computational):** Develop computational algorithms to generate fractal structures using iterative loops and recursive functions, and visually demonstrate the impact of matrix probability weights on geometric patterns.
* **LObj3 (Real-World):** Analyze the efficiency of fractal geometry in engineering, specifically evaluating its role in multi-band signal reception (antennas) and realistic digital terrain modeling (CGI).

### Main Module Outcome

> *"Design and implement computational algorithms to visualize fractal structures—including the Sierpinski triangle, Barnsley fern, and Pythagorean tree—using iterative loops and recursive methods, while evaluating the real-world efficiency of fractal geometry in optimizing telecommunication systems and generating realistic digital environments."*
