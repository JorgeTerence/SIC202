import matplotlib.pyplot as plt
from graph import draw

if __name__ == "__main__":
    ax = draw()

    ax.set_title('data.csv')

    for angle in range(0, 360, 3):
        ax.view_init(24, angle)
        plt.draw()
        plt.pause(0.01)
