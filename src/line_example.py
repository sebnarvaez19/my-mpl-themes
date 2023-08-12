import numpy as np
import matplotlib.pyplot as plt

plt.style.use('./basic.mplstyle')

x = np.linspace(0, 2*np.pi, 1000)
y1 = np.cos(x) + 1
y2 = np.sin(x) + 1

fig, ax = plt.subplots(1)

ax.plot(x, y1, label='f(x)=cos(x)')
ax.plot(x, y2, label='f(x)=sin(x)')
ax.set(xlabel='Time [s]', ylabel='Amplitude [μm]', title='Trigonometric functions')
ax.legend(title='Functions', loc='lower left')

fig.savefig('./images/line_example.svg')
