# module traiettoria.py
import numpy as np

#la traiettoria evolve ogni 30 secondi, prendo un pezzo di traiettoria ogni TC secondi
pos = np.zeros((750, 3)) #1500

j=0
#il tempo varia da 0 a 30 sec con un passo di 0.04 (tempo di campionamento)
for tempo in np.arange(0, 30, 0.04):
    pos[j, 0] = np.cos(tempo)
    pos[j, 1] = np.sin(tempo)
    pos[j, 2] = 1 + 0.5*np.sin(tempo*2)
    j = j + 1
