from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = plt.axes(projection='3d')

plt.rcParams['legend.fontsize'] = 10


# First constraint
g2 = np.linspace(-5,5,2)
g3 = np.linspace(-5,5,2)
G2,G3 = np.meshgrid(g2,g3)
G4_1 = -1.18301270189222 - 0.5*G2 + 0.5*G3
ax = fig.gca(projection='3d')
c1 = ax.plot_surface(G2, G3, G4_1, label = "c1")
c1._facecolors2d=c1._facecolors3d
c1._edgecolors2d=c1._edgecolors3d

# Second
G3, G4 = np.meshgrid(g2, g3)
G2 = G3
c2 = ax.plot_surface(G2, G3, G4, label = "c2")
c2._facecolors2d=c2._facecolors3d
c2._edgecolors2d=c2._edgecolors3d

# Third
G2,G3 = np.meshgrid(g2,g3)
G4 = (0.408248290463863*G2 + 0.408248290463863*G3 -0.707106781186548)/1.63299316185545
c3 = ax.plot_surface(G2, G3, G4, label = "c3")
c3._facecolors2d=c3._facecolors3d
c3._edgecolors2d=c3._edgecolors3d

# And forth
G4 = (1.04903810567666 - (0.288675134594813*G2 + 0.288675134594813*G3))/0.577350269189626
c4 = ax.plot_surface(G2, G3, G4, label="c4")

c4._facecolors2d=c4._facecolors3d
c4._edgecolors2d=c4._edgecolors3d

ax.legend() # -> error : 'AttributeError: 'Poly3DCollection' object has no attribute '_edgecolors2d''


# labeling the figure
fig.suptitle("Constraints")
#plt.xlabel('g2', fontsize=14)
#plt.ylabel('g3', fontsize=14)
ax.set_xlabel(r'$g_2$', fontsize=15, rotation=60)
ax.set_ylabel('$g_3$', fontsize=15, rotation=60)
ax.set_zlabel('$g_4$', fontsize=15, rotation=60)
plt.savefig('Constraints.jpg')
plt.show()