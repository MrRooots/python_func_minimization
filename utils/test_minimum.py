import numpy as np
from scipy.optimize import minimize


class MinimumTester:
  @staticmethod
  def get_minimum(function: callable,
                  x_domain: tuple[float, float],
                  y_domain: tuple[float, float]
                  ) -> tuple[float, tuple[float, float]]:
    minimum = minimize(function,
                       np.array([0, 0]),
                       bounds=[x_domain, y_domain])

    return round(minimum.fun, 5), tuple(round(i, 5) for i in minimum.x)
