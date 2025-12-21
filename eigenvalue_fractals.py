import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# --- CONFIGURATION ---
# Initial shape: A unit square
# Represented as a 2xN matrix for linear transformation
square = np.array([
    [1, 1], [1, -1], [-1, -1], [-1, 1], [1, 1]
]).T 

# --- CORE FUNCTIONS ---
def compute_transformation_matrix(eigenvalue, angle_deg=15):
    """
    Creates a transformation matrix combining scaling (eigenvalue) and rotation.
    The 'eigenvalue' determines the convergence or divergence of the system.
    """
    theta = np.radians(angle_deg)
    c, s = np.cos(theta), np.sin(theta)
    
    # Rotation Matrix * Scaling Factor (Eigenvalue)
    rotation_matrix = np.array([[c, -s], [s, c]])
    return eigenvalue * rotation_matrix

# --- VISUALIZATION SETUP ---
fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(bottom=0.25) # Space for the slider

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_title("Eigenvalue Analysis: Convergence vs. Divergence")
ax.set_aspect('equal')

# Storage for dynamic plot objects
plots = []
colors = ['#1f77b4', '#17becf', '#2ca02c', '#bcbd22', '#9467bd']

def update_simulation(val):
    """
    Updates the iterative transformation based on the slider's eigenvalue.
    """
    ev = slider_eigenvalue.val 
    
    # Clear previous frames
    for p in plots:
        p.remove()
    plots.clear()
    
    current_shape = square.copy()
    transformation_matrix = compute_transformation_matrix(ev)
    
    # Perform 10 iterations
    for i in range(10):
        # Safety break for divergent systems
        if np.max(np.abs(current_shape)) > 100:
            break
            
        # Linear Transformation: X_new = M @ X_old
        current_shape = transformation_matrix @ current_shape 
        
        # Style: Red for divergence (ev > 1), Blue tones for convergence
        color = 'crimson' if ev > 1.0 else colors[i % len(colors)]
        alpha = max(0.2, 1.0 - (i * 0.08))
        
        line, = ax.plot(current_shape[0, :], current_shape[1, :], 
                        color=color, linewidth=2, alpha=alpha)
        plots.append(line)
        
    fig.canvas.draw_idle()

# --- INTERACTIVE SLIDER ---
ax_slider = plt.axes([0.2, 0.1, 0.65, 0.03])
slider_eigenvalue = Slider(
    ax_slider, 'Eigenvalue (λ)', 0.5, 1.2, valinit=0.85, valfmt='%.2f'
)

slider_eigenvalue.on_changed(update_simulation)

# Initial execution
update_simulation(0.85)

print("Simulation active. Use the slider to analyze system stability.")
plt.show()
