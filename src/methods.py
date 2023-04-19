import math


class CalculationMethod:
  """
  Calculation methods base.
  """

  @staticmethod
  def calculate(*args, **kwargs) -> float | tuple[float, float]:
    """ Calculate something """


class DichotomyMethod(CalculationMethod):
  """
  Dichotomy method implementation.
  """

  @staticmethod
  def calculate(f: callable,
                points: tuple[float, float],
                gradient: tuple[float, float],
                k: float,
                alpha: float,
                precision: float) -> float:
    x, y = points
    dx, dy = gradient
    a, b = 0, alpha

    while b - a > precision:
      c = (a + b) / 2.0

      f_0, f_1 = [f(x - i * dx, y - i * dy, k) for i in (a, c)]

      a, b = (a, c) if f_0 * f_1 < 0 else (c, b)

    return (a + b) / 2.0


class SteepestDescendMethod(CalculationMethod):
  """
  Steepest descend method implementation.
  """

  @staticmethod
  def calculate(f: callable,
                gradient: callable,
                points: tuple[float, float],
                k: float,
                alpha: float,
                precision: float,
                max_iteration: int) -> tuple[float, float, bool | int]:
    x, y = points
    i = 0

    while i <= max_iteration:
      i += 1
      step = .00001
      grad_x, grad_y = gradient(x, y, k)
      g_norm = math.sqrt(grad_x ** 2 + grad_y ** 2)
      grad_x, grad_y = grad_x / g_norm, grad_y / g_norm

      changed = False
      while 0 <= x - alpha * grad_x <= 4 and 0 <= y - alpha * grad_y <= 4:
        alpha += step
        changed = True

      alpha = DichotomyMethod.calculate(f,
                                        (x, y),
                                        (grad_x, grad_y),
                                        k,
                                        alpha if not changed else alpha - step,
                                        precision)

      x_new, y_new = x - alpha * grad_x, y - alpha * grad_y

      if math.fabs(f(x, y, k) - f(x_new, y_new, k)) < precision:
        return x_new, y_new, False if i == max_iteration else i

      x, y = x_new, y_new
      k *= 2
      alpha = 0

    return x, y, True
