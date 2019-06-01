import numpy as np
import parametri as p

A = np.array([[1., p.TC, (p.TC**2)/2, 0., 0.,   0.,          0., 0.,   0.],
              [0., 1.,   p.TC,        0., 0.,   0.,          0., 0.,   0.],
              [0., 0.,   1.,          0., 0.,   0.,          0., 0.,   0.],
              [0., 0.,   0.,          1., p.TC, (p.TC**2)/2, 0., 0.,   0.],
              [0., 0.,   0.,          0., 1.,   p.TC,        0., 0.,   0.],
              [0., 0.,   0.,          0., 0.,   1.,          0., 0.,   0.],
              [0., 0.,   0.,          0., 0.,   0.,          1., p.TC, (p.TC ** 2) / 2],
              [0., 0.,   0.,          0., 0.,   0.,          0., 1., p.TC],
              [0., 0.,   0.,          0., 0.,   0.,          0., 0., 1.]])

F = np.array([[0.5*(p.TC**2),     0,               0],
              [p.TC,         0,               0],
              [1,            0,               0],
              [0,            0.5*(p.TC**2),        0],
              [0,            p.TC,            0],
              [0,            1,               0],
              [0,            0,               0.5*(p.TC**2)],
              [0,            0,               p.TC],
              [0,            0,               1]])

Q = p.VAR_STATO * np.eye(3)

R = p.VAR_RSSI * np.eye(4)


P = np.eye(9)

#taylor
def clineare(x, y, z):
    return np.array([[(2*x - 2*p.BEACON[0, 0]), 0., 0., (2*y - 2*p.BEACON[0, 1]), 0., 0., (2*z - 2*p.BEACON[0, 2]), 0., 0.],
                     [(2*x - 2*p.BEACON[1, 0]), 0., 0., (2*y - 2*p.BEACON[1, 1]), 0., 0., (2*z - 2*p.BEACON[1, 2]), 0., 0.],
                     [(2*x - 2*p.BEACON[2, 0]), 0., 0., (2*y - 2*p.BEACON[2, 1]), 0., 0., (2*z - 2*p.BEACON[2, 2]), 0., 0.],
                     [(2*x - 2*p.BEACON[3, 0]), 0., 0., (2*y - 2*p.BEACON[3, 1]), 0., 0., (2*z - 2*p.BEACON[3, 2]), 0., 0.]])


def cnonlineare(x, y, z):
    return np.array([(x - p.BEACON[0, 0])**2 + (y - p.BEACON[0, 1])**2 + (z - p.BEACON[0, 2])**2,
                     (x - p.BEACON[1, 0])**2 + (y - p.BEACON[1, 1])**2 + (z - p.BEACON[1, 2])**2,
                     (x - p.BEACON[2, 0])**2 + (y - p.BEACON[2, 1])**2 + (z - p.BEACON[2, 2])**2,
                     (x - p.BEACON[3, 0])**2 + (y - p.BEACON[3, 1])**2 + (z - p.BEACON[3, 2])**2])







#calcolo la distanza dall'antenna rispetto alle ancore
def distanze(x, y, z):
    return np.array([(x - p.BEACON[0, 0])**2 + (y - p.BEACON[0, 1])**2 + (z - p.BEACON[0, 2])**2,
                     (x - p.BEACON[1, 0])**2 + (y - p.BEACON[1, 1])**2 + (z - p.BEACON[1, 2])**2,
                     (x - p.BEACON[2, 0])**2 + (y - p.BEACON[2, 1])**2 + (z - p.BEACON[2, 2])**2,
                     (x - p.BEACON[3, 0])**2 + (y - p.BEACON[3, 1])**2 + (z - p.BEACON[3, 2])**2])


