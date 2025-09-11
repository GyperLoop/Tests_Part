# Gifs creation
import matplotlib.pyplot as plt                     # Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python
import matplotlib.animation as animation
import numpy as np                                  # NumPy is the fundamental package for scientific computing with Python     

# Parameters
frames = 100 # number of frames in the gif
interval = 100  # milliseconds between frames
circle_radius = 0.1  # relative to the plot size

# Diamond layout positions and colors
positions = [(1, 0), (0.7, 0.7), (0, 1), (-0.7, 0.7), (-1, 0), (-0.7, -0.7), (0, -1), (0.7, -0.7)]
colors = [(173/255, 216/255, 230/255), (0/255, 0/255, 139/255)]

def get_color(T: float) -> tuple:
    """Get color based on time T"""
    return tuple(colors[0][i] * (1 - T) + colors[1][i] * T for i in range(3))

# Setup figure 
fig, ax = plt.subplots(figsize=(6,6))
ax.set_aspect('equal')
ax.axis('off')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Transparent background
fig.patch.set_alpha(0.0)
ax.patch.set_alpha(0.0)

# Create circles
circles = [plt.Circle(pos, circle_radius, color=colors[0]) for pos in positions]
for circle in circles:
    ax.add_patch(circle)

def animate(frame: int):
    for i, circle in enumerate(circles):
        T = ((frame + i * 10) % frames) /  frames
        circle.set_color(get_color(T))
        # Pulsing effect
        pulse = 0.1 + 0.05 * np.sin(2 * np.pi * T)
        circle.set_radius(pulse)
    return circles

ani = animation.FuncAnimation(fig, animate, frames=frames, interval=interval, blit=True)

# Save as GIF
ani.save('animated_diamond.gif', writer='pillow', savefig_kwargs={"transparent": True}, fps=35)

print("GIF saved as 'animated_diamond.gif'")