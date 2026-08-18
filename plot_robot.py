import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

L1, L2 = 5.0, 3.0
max_length = L1 + L2 + 1

# Caricamento dati generati dal C
data = np.loadtxt("traj_data.txt")
sing_max = np.loadtxt("sing_max.txt")
sing_min = np.loadtxt("sing_min.txt")

# Estrazione colonne: OA_x, OA_y, AP_x, AP_y, OP_x, OP_y
OA_x, OA_y = data[:, 0], data[:, 1]
AP_x, AP_y = data[:, 2], data[:, 3]
OP_x, OP_y = data[:, 4], data[:, 5]

# --- 1. ANIMAZIONE DEL MOVIMENTO ---
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')
ax.grid(True)
ax.set_xlim(-max_length, max_length)
ax.set_ylim(-max_length, max_length)
ax.set_title("Animazione Manipolatore Planare 2R")

# Elementi grafici per l'animazione
quiver1 = ax.quiver(0, 0, 0, 0, angles='xy', scale_units='xy', scale=1, color='r', linewidth=2)
quiver2 = ax.quiver(0, 0, 0, 0, angles='xy', scale_units='xy', scale=1, color='b', linewidth=2)
joint1, = ax.plot([], [], 'yo', markersize=8)
joint2, = ax.plot([], [], 'go', markersize=8)

# Disegna le traiettorie complete in background
ax.plot(OP_x, OP_y, 'g--', alpha=0.5, label='Traiettoria End-Effector')
ax.plot(OA_x, OA_y, 'y--', alpha=0.5, label='Traiettoria Giunto A')
ax.legend(loc='upper right')

def update(i):
    # Aggiorna i vettori (quiver)
    quiver1.set_offsets([0, 0])
    quiver1.set_UVC(OA_x[i], OA_y[i])
    
    quiver2.set_offsets([OA_x[i], OA_y[i]])
    quiver2.set_UVC(AP_x[i], AP_y[i])
    
    # Aggiorna i punti (giunti)
    joint1.set_data([OA_x[i]], [OA_y[i]])
    joint2.set_data([OP_x[i]], [OP_y[i]])
    return quiver1, quiver2, joint1, joint2

ani = animation.FuncAnimation(fig, update, frames=len(data), interval=50, blit=False)

# --- 2. CONFIGURAZIONI SINGOLARI (Figure separate) ---
def plot_singularity(sing_data, title):
    fig_sing, ax_sing = plt.subplots(figsize=(6, 6))
    ax_sing.set_aspect('equal')
    ax_sing.grid(True)
    ax_sing.set_xlim(-max_length, max_length)
    ax_sing.set_ylim(-max_length, max_length)
    ax_sing.set_title(title)

    oa_x, oa_y, ap_x, ap_y, op_x, op_y = sing_data

    ax_sing.quiver(0, 0, oa_x, oa_y, angles='xy', scale_units='xy', scale=1, color='r', linewidth=2)
    ax_sing.plot(oa_x, oa_y, 'go', markersize=8)
    ax_sing.quiver(oa_x, oa_y, ap_x, ap_y, angles='xy', scale_units='xy', scale=1, color='b', linewidth=2)
    ax_sing.plot(op_x, op_y, 'yo', markersize=8)

plot_singularity(sing_max, "Allineato Estensione Massima (Theta2 = 0)")
plot_singularity(sing_min, "Allineato Estensione Minima (Theta2 = pi)")

plt.show()

print("Fine!\n")