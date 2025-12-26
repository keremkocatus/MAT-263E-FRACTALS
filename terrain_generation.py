import matplotlib.pyplot as plt
import numpy as np


N = 6  # Detay seviyesi (2^N + 1 boyutunda bir ızgara oluşturur). Örn: N=6 -> 65x65
size = 2**N + 1
roughness = 0.4   # Pürüzlülük (0-1 arası)
initial_scale = 100 # Başlangıçtaki rastgelelik miktarı

# Basitleştirilmiş Midpoint Displacement
terrain = np.zeros((size, size))

# Köşeleri rastgele başlat
terrain[0, 0] = np.random.uniform(-initial_scale, initial_scale)
terrain[0, size-1] = np.random.uniform(-initial_scale, initial_scale)
terrain[size-1, 0] = np.random.uniform(-initial_scale, initial_scale)
terrain[size-1, size-1] = np.random.uniform(-initial_scale, initial_scale)

step_size = size - 1
current_scale = initial_scale

while step_size > 1:
    half_step = step_size // 2
    
    # Diamond Adımı (Karelerin merkezi)
    for x in range(half_step, size, step_size):
        for y in range(half_step, size, step_size):
            avg = (terrain[x - half_step, y - half_step] +
                   terrain[x - half_step, y + half_step] +
                   terrain[x + half_step, y - half_step] +
                   terrain[x + half_step, y + half_step]) / 4.0
            terrain[x, y] = avg + np.random.uniform(-current_scale, current_scale)

    # Square Adımı (Kenarların merkezi)
    for x in range(0, size, half_step):
        for y in range((x + half_step) % step_size, size, step_size):
            avg = (terrain[(x - half_step) % size, y] +
                   terrain[(x + half_step) % size, y] +
                   terrain[x, (y - half_step) % size] +
                   terrain[x, (y + half_step) % size]) / 4.0
            terrain[x, y] = avg + np.random.uniform(-current_scale, current_scale)

    step_size //= 2
    current_scale *= roughness # Her adımda değişim miktarını azalt

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

X = np.arange(size)
Y = np.arange(size)
X, Y = np.meshgrid(X, Y)

surf = ax.plot_surface(X, Y, terrain, cmap='terrain', linewidth=0, antialiased=False)
ax.set_title("3D CGI Fractal Terrain (Diamond-Square App.)")
ax.set_zlim(-initial_scale*1.5, initial_scale*1.5)
ax.axis('off') 
ax.view_init(elev=40, azim=-45) 

plt.show()