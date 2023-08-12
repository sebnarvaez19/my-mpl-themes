import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

plt.style.use('./matrix.mplstyle')

x = np.linspace(-np.pi, np.pi, 101)
X, Y = np.meshgrid(np.cos(x), np.sin(x))

Z = X * Y

fig, ax = plt.subplots(1, figsize=(6, 6), tight_layout=True)

img = ax.pcolormesh(x, x, Z, vmin=-0.5, vmax=1.0)
ax.set(xlabel='Longitude [m]', ylabel='Latitude [m]', title='Rocket launch')

div = make_axes_locatable(ax)
cax = div.append_axes('right', size='5%', pad=0.10)
bar = plt.colorbar(img, cax=cax, label='Amplitude [μm]')

fig.savefig('./images/matrix_example.svg')
