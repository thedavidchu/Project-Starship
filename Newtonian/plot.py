import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def plt_plot(data, ):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.set_title('Space')

    ax.set_xlim3d([-100, 100])
    ax.set_xlabel('x')
    ax.set_ylim3d([-100, 100])
    ax.set_ylabel('y')
    ax.set_zlim3d([-100, 100])
    ax.set_zlabel('z')
    ax.view_init(25, 10)

    iterations = len(data)
    # anim = animation.FuncAnimation(fig, )


if __name__ == '__main__':
    data = None
    plt_plot()