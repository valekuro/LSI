# modulo Ex_Kalman_Filter.py
# filtro di kalman esteso
import numpy as np
import sistema as s

def kalman( x, P, misure):

    x_pred = s.A @ x.T #X(k+1|k)

    p_new = s.A @ P @ s.A.T + s.F @ s.Q @ s.F.T #P(k+1|k)

    C = s.clineare(x_pred[0], x_pred[3], x_pred[6])

    PCT = p_new@C.T

    K = PCT @ np.linalg.inv(C@PCT+s.R) #K(k+1)
    x_pred = x_pred + K@(misure.T - s.cnonlineare(x_pred[0], x_pred[3], x_pred[6]).T)#X(k+1)
    p_new = (np.eye(9) - K@C)@ p_new#p(k+1)
    return x_pred, p_new

