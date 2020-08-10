from matplotlib import pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from scipy import interpolate

import seaborn as sns

# initializing a figure in  
# which the graph will be plotted 
fig = plt.figure()

# marking the x-axis and y-axis
plt.title("Shifting Technique")
axis = plt.axes(xlim=(2, 41), ylim=(20, 130))
axis.spines["top"].set_visible(False)
axis.spines["bottom"].set_visible(False)
axis.spines["right"].set_visible(False)
axis.spines["left"].set_visible(False)

axis.get_xaxis().tick_bottom()
axis.get_yaxis().tick_left()

axis.xaxis.set_tick_params(length=0)
axis.yaxis.set_tick_params(length=0)
sns.despine(left=True, bottom=True)
# initializing a line variable
colors = [(31/255., 119/255., 180/255.), (174/255., 199/255., 232/255.), (255/255., 127/255., 14/255.)]
line1, = axis.plot([], [], lw=2, label='QR_unshifted', color=colors[0])
line2, = axis.plot([], [], lw=2, label='QR_shifted',color=colors[1])
line3, = axis.plot([], [], lw=2, label='QR_wilkinson_shifted',color=colors[2])
lines = [line1, line2, line3]
top_dim = 40
step = 1
dim_list = [2 + step * i for i in range(top_dim)]
QR_unshifted = [33.32,37.41,47.46,45.68,51.66,50.99,53.57,60.96,61.04,59.1,59.4,70.65,71.79,73.66,82.3,78.67,90.91,83.59,82.86,93.7,91.39,94.93,91.58,97.0,91.73,101.84,107.23,95.52,96.72,107.16,113.44,115.09,104.45,108.1,110.24,106.69,108.12,112.48,114.75,121.0]
QR_shifted=[32.37,24.06,37.96,52.18,42.07,55.51,54.49,48.04,62.07,40.33,50.33,46.58,54.23,70.19,66.14,76.12,68.11,69.57,78.62,68.34,69.3,72.34,64.03,98.3,84.61,80.3,88.76,82.34,96.0,79.32,81.31,109.01,90.24,112.89,93.82,111.25,77.96,86.86,88.0,81.47]
QR_wilkinson_shift=[29.77,21.91,38.06,44.79,36.65,50.97,44.31,47.34,65.91,42.74,74.34,55.77,49.01,69.07,70.36,62.97,60.69,67.28,78.29,71.22,70.16,75.06,73.74,100.59,91.49,87.65,75.27,84.18,94.89,73.01,84.51,81.42,75.44,110.16,97.13,77.45,81.25,92.96,100.15,77.68]
H_QR_unshifted=[33.32,37.41,47.46,45.68,51.66,50.99,53.57,60.96,61.04,59.1,59.4,70.65,71.79,73.66,82.3,78.67,90.91,83.59,82.86,93.7,91.39,94.93,91.58,97.0,91.73,101.84,107.23,95.52,96.72,107.16,113.44,115.09,104.45,108.1,110.24,106.69,108.12,112.48,114.75,121.0]
H_QR_shifted = [24.69,20.99,28.3,32.33,38.77,41.38,40.76,44.09,51.94,55.94,63.61,52.07,61.44,60.92,65.43,93.35,73.2,56.73,68.85,79.37,64.88,85.9,76.38,68.22,76.56,78.19,78.51,89.08,69.85,79.12,76.08,83.13,89.84,82.69,99.8,97.32,84.27,83.83,85.71,87.17]
H_QR_wilkinson_shift=[21.95,21.48,29.02,32.27,37.98,44.36,57.57,43.78,48.86,47.95,63.07,50.78,60.98,69.99,65.83,95.68,73.31,58.44,69.58,80.77,63.93,85.87,73.82,68.6,73.36,78.23,78.84,87.79,77.6,79.83,76.15,79.59,90.17,81.55,100.91,92.61,80.62,99.74,88.73,84.77]

x_base = np.linspace(2, 41, 400)
a_BSpline_QR_unshifted = interpolate.make_interp_spline(dim_list, QR_unshifted)
a_BSpline_QR_shifted = interpolate.make_interp_spline(dim_list, QR_shifted)
a_BSpline_QR_wilkinson_shift = interpolate.make_interp_spline(dim_list, QR_wilkinson_shift)
y_base_QR_unshifted = a_BSpline_QR_unshifted(x_base)
y_base_QR_shifted = a_BSpline_QR_shifted(x_base)
y_base_QR_wilkinson_shift = a_BSpline_QR_wilkinson_shift(x_base)
xdata = []
ydata1 = []
ydata2 = []
ydata3 = []
# data which the line will
# contain (x, y) 
def init():
    for line in lines:
        line.set_data([], [])
    return lines

def animate(i):
    xdata.append(x_base[i])
    # plots a sine graph 
    ydata1.append(y_base_QR_unshifted[i])
    ydata2.append(y_base_QR_shifted[i])
    ydata3.append(y_base_QR_wilkinson_shift[i])
    line1.set_data(xdata, ydata1)
    line2.set_data(xdata, ydata2)
    line3.set_data(xdata, ydata3)
    return lines


anim = FuncAnimation(fig, animate, init_func=init, frames=399, interval=20, blit=True)
axis.legend(frameon=False)
anim.save('gif_without_Hessenberg.mp4', writer='ffmpeg', fps=30)