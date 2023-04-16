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
      c = (a + b) / 2

      f_0, f_1 = [f(x - i * dx, y - i * dy, k) for i in (a, c)]

      a, b = (a, c) if f_0 * f_1 < 0 else (c, b)

    return (a + b) / 2


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
      grad_x, grad_y = gradient(x, y, k)
      g_norm = math.sqrt(grad_x ** 2 + grad_y ** 2)
      alpha = DichotomyMethod.calculate(f,
                                        (x, y),
                                        (grad_x, grad_y),
                                        k,
                                        alpha,
                                        precision)

      x_new, y_new = x - alpha * (grad_x / g_norm), \
                     y - alpha * (grad_y / g_norm)

      if g_norm < precision:
        print(f'Normalized gradient')
        return x, y, False if i == max_iteration else i
      elif 0 <= x_new <= 4 and 0 <= y_new <= 4:
        x, y = x_new, y_new
      else:
        k *= 2

    return x, y, True
