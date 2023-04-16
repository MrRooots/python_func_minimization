import matplotlib.pyplot as plt
import numpy as np


class Plotter:
  """
  Class that helps to draw 3D graphs
  """

  @staticmethod
  def draw_function(function: callable,
                    x_domain: tuple[float, float],
                    y_domain: tuple[float, float]) -> None:
    """
    Draw 3D graph for given function
    """

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create points sequences
    x = np.linspace(x_domain[0], x_domain[1], 50)
    y = np.linspace(y_domain[0], y_domain[1], 50)
    x_points, y_points = np.meshgrid(x, y)

    ax.plot_surface(x_points, y_points,
                    np.vectorize(function)(x_points, y_points))

    plt.show()
