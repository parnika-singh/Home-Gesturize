import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.pyplot import imread 
from mpl_toolkits.mplot3d import Axes3D 

 
imageFile = r'C:\Users\dell\Desktop\faltu\photo.jpg' 
mat = imread(imageFile) 
mat = mat[:,:,0] # get the first channel 
rows, cols = mat.shape 
xv, yv = np.meshgrid(range(cols), range(rows)[::-1]) 
 
fig = plt.figure(figsize=(6,6)) 
 
ax = fig.add_subplot(221) 
ax.imshow(mat, cmap='gray') 
 
ax = fig.add_subplot(222, projection='3d') 
ax.elev= 75 
ax.plot_surface(xv, yv, mat) 
plt.show()
