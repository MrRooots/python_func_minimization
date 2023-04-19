import math


def f(*args) -> float:
  """ Object function """
  x, y = args if len(args) > 1 else args[0]

  return 2 * (x - 1) ** 2 + (y - 2) ** 3 + math.sqrt((x + 2) ** 2 + (y + 2) ** 2)


def penalty_f(x: float, y: float, k: float) -> float:
  """ Object function with penalty term """
  return f(x, y) + 1 / k * (1 / x + 1 / (4 - x) + 1 / y + 1 / (4 - y))


def object_gradient(x: float, y: float) -> tuple[float, float]:
  """ Get both gradient values of object function. """
  dx = 4 * (x - 1) + (x + 2) / math.sqrt((x + 2) ** 2 + (y + 2) ** 2)
  dy = 3 * (y - 2) ** 2 + (y + 2) / math.sqrt((x + 2) ** 2 + (y + 2) ** 2)

  return dx, dy


def penalty_gradient(x: float, y: float, k: float) -> tuple[float, float]:
  """ Get both gradient values of object function with penalty term. """
  dx, dy = object_gradient(x, y)
  excluded_domain = (0, 2)

  if x not in excluded_domain and y not in excluded_domain:
    dx += (8 * (x - 2)) / (k * (4 - x ** 2) * x ** 2)
    dy += (8 * (y - 2)) / (k * (4 - y ** 2) * y ** 2)

  return dx, dy
