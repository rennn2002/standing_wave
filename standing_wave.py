import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

#環境設定
c = 3e8     #光速 m/s
f = 3e8     #周波数 Hz
T = 1 / f   #周期 s
ramda = c / f   #波長 m
beta = 2 * np.pi / ramda    #位相定数
omega = 2 * np.pi / T       #角周波数

x_range = np.linspace(-4*np.pi/beta, 0.0, 200)
t_range = np.linspace(0.0, 2*np.pi/omega, 100)

#x, y 座標上で時間tを変化させる
fig = plt.figure()
artists = []
artists2 = []

for t in t_range:
    v = 2*np.cos(beta*x_range)*np.cos(omega*t)

    
    im = plt.plot(x_range,v, color = "blue")

    
    artists.append(im)

    
ani = animation.ArtistAnimation(fig, artists,50)

ani.save('animation_test.gif')
