import utils
import numpy as np
import matplotlib.pyplot as plt

data = utils.TaskData(m=3)

print(f'x:{data.x}')
print(f'y:{data.f}')

data.solve()
data.print_solved()

splines = [
    utils.Spline(data.x[0]),
    utils.Spline(data.x[1]),
    utils.Spline(data.x[2]),
]

fig, ax = plt.subplots()
ax.scatter(data.x, data.f, c='black', zorder=2)
ax.grid(True, zorder=0.1)
for i in range(len(splines)):
    splines[i].setcoefs(a=data.f[i], b=data.b[i], c=data.c[i], d=data.d[i])
    print(splines[i], splines[i].to_standart())
    # print(data.x[i], splines[i].at_point(data.x[i]), '|',data.x[i+1],splines[i].at_point(data.x[i+1]))
    x_data = np.linspace(data.x[i], data.x[i + 1], 5)
    y_data = []
    for x in x_data:
        y_data.append(splines[i].at_point(x))
    # print(x_data, y_data)
    ax.plot(x_data, y_data, zorder=1)

plt.show()
