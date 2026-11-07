
import h5py
import numpy as np
import matplotlib.pyplot as plt

eps_h5file = h5py.File('nanobeam-eps-000621.20.h5','r')
eps_data = np.array(eps_h5file['eps'])
ey_h5file = h5py.File('nanobeam-ey-000621.20.h5','r')
ey_data = np.array(ey_h5file['ey'])
plt.figure(dpi=100)
plt.imshow(eps_data.transpose(), interpolation='spline36', cmap='binary')
plt.imshow(ey_data.transpose(), interpolation='spline36', cmap='RdBu', alpha=0.9)
plt.axis('off')
plt.show()
  