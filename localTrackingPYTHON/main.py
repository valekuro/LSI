import Ex_Kalman_Filter as kalman
import sistema as s
import numpy as np
import parametri as pa
import traiettoria
import vrep
import time

# Inizializzo variabili - v e a non so quali sono
#al filtro lo stato iniz è esatto perchè gli do il punto di partenza
x = np.array([traiettoria.pos[0, 0], 0, 0,
              traiettoria.pos[0, 1], 0, 0,
              traiettoria.pos[0, 2], 0, 0])
P = np.eye(9)

print('Program started')
# just in case, close all opened connections
vrep.simxFinish(-1)
# Connect to V-REP
clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
if clientID != -1:
    print('Connected to remote API server')
    time.sleep(2)
    returnCode, handle = vrep.simxGetObjectHandle(clientID, 'Quadricopter_target', vrep.simx_opmode_oneshot_wait)#muovi secondo traiettoria
    returnCode, handle1 = vrep.simxGetObjectHandle(clientID, 'Sphere', vrep.simx_opmode_oneshot_wait)#il filtro ma serve solo per il grafico

    for jk in range(1):
        for i in range(0, 750):
            pos_real = [traiettoria.pos[i, 0], traiettoria.pos[i, 1], traiettoria.pos[i, 2]]
            err = vrep.simxSetObjectPosition(clientID, handle, -1, pos_real, vrep.simx_opmode_blocking) #setting position

            distanza = s.distanze(traiettoria.pos[i, 0], traiettoria.pos[i, 1], traiettoria.pos[i, 2])
            misure = np.array([distanza[0] + np.random.normal(0, pa.VAR_RSSI),
                               distanza[1] + np.random.normal(0, pa.VAR_RSSI),
                               distanza[2] + np.random.normal(0, pa.VAR_RSSI),
                               distanza[3] + np.random.normal(0, pa.VAR_RSSI)])
            x, P = kalman.kalman(x, P, misure)
            pos_stima = [x[0], x[3], x[6]]

            err = vrep.simxSetObjectPosition(clientID, handle1, -1, pos_stima, vrep.simx_opmode_blocking)

            #input("Press Enter to continue...")
    vrep.simxFinish(clientID)
else:
    print('Failed connecting to remote API server')



print ('Program ended')