import numpy as np
import matplotlib.pyplot as plt
import os

# 1. Parámetros Físicos para Régimen Caótico
g = 9.78          # Gravedad
L = 1.0           # Longitud
gamma = 0.5       # Fricción
A = 10.5          # Amplitud de la fuerza externa
omega = 2/3       # Frecuencia de la fuerza externa

dt = 0.01         # Paso de tiempo
t_max = 2000      # Aumentamos el tiempo para generar miles de puntos
n_steps = int(t_max / dt)

# 2. Condiciones Iniciales
theta_0 = 0.2
omega_0 = 0.0

t = np.linspace(0, t_max, n_steps)
theta = np.zeros(n_steps)
w = np.zeros(n_steps)

theta[0] = theta_0
w[0] = omega_0

# 3. Integración Numérica por el método de Euler-Cromer
for i in range(n_steps - 1):
    acc = -(g / L) * np.sin(theta[i]) - gamma * w[i] + A * np.cos(omega * t[i])
    w[i + 1] = w[i] + acc * dt
    theta[i + 1] = theta[i] + w[i + 1] * dt
    
    # Mantener el ángulo en [-pi, pi]
    theta[i + 1] = (theta[i + 1] + np.pi) % (2 * np.pi) - np.pi

# 4. Selección de puntos para la Sección de Poincaré
# Periodo de la fuerza impulsora T = 2*pi / omega
T = 2 * np.pi / omega
steps_per_period = int(round(T / dt))

# Tomamos un punto exactamente cada período completo T, descartando el inicio (transitorio)
start_step = int(100 / dt)  # Descartamos los primeros 100 segundos
indices_poincare = range(start_step, n_steps, steps_per_period)

theta_poincare = theta[indices_poincare]
w_poincare = w[indices_poincare]

# 5. Visualización
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))

# Gráfico 1: Evolución temporal
ax1.plot(t[:2000], theta[:2000], color='navy', lw=0.8)
ax1.set_title("Evolución temporal $\\theta(t)$", fontsize=11)
ax1.set_xlabel("Tiempo [s]")
ax1.set_ylabel("Ángulo $\\theta$ [rad]")
ax1.grid(True, linestyle='--', alpha=0.5)

# Gráfico 2: Espacio de fases continuo
ax2.plot(theta, w, color='darkred', lw=0.1, alpha=0.4)
ax2.set_title("Espacio de fases (Trayectoria)", fontsize=11)
ax2.set_xlabel("Ángulo $\\theta$ [rad]")
ax2.set_ylabel("Velocidad $\\omega$ [rad/s]")
ax2.grid(True, linestyle='--', alpha=0.5)

# Gráfico 3: Sección de Poincaré (Estructura Fractal)
ax3.scatter(theta_poincare, w_poincare, color='crimson', s=3, alpha=0.7)
ax3.set_title("Sección de Poincaré (Atractor Fractal)", fontsize=11)
ax3.set_xlabel("Ángulo $\\theta$ [rad]")
ax3.set_ylabel("Velocidad $\\omega$ [rad/s]")
ax3.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()

# Guardar figura
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, "poincare_pendulo.svg"), format="svg")
plt.savefig(os.path.join(output_dir, "poincare_pendulo.png"), dpi=300)
print("¡Sección de Poincaré generada e imágenes guardadascon éxito!")
plt.show()
