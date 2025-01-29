import matplotlib.pyplot as plt, numpy as np
from mpl_toolkits.mplot3d import Axes3D

arr1= np.array([[2,9,4], [3,3,10], [7,4,8]])
new_val = plt.figure()
result = new_val.add_subplot(122, projection='3d')
result.plot(arr1[:,0],arr1[:,1],arr1[:,2])
plt.show()
