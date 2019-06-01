# modulo parametri.py
import numpy as np

# tempo di campionamento
#TC = 0.02
TC = 0.04 #25 pachetti al secondo

# varianza rumore di stato
#VAR_STATO = 1
VAR_STATO = 0.01

# varianza misura distanza da RSSI
#VAR_RSSI  = 0.1
VAR_RSSI  = 1

# numero di ancore
N_BEACON = 4

# configurazione spaziale ancore [x, y, z]
BEACON = np.array([[-2.45, -2.15, -1.4],
                   [-1.9, 2.3, -1.4],
                   [1.6, 2.3, -1.4],
                   [2.4, -2.07, -1.4]])


