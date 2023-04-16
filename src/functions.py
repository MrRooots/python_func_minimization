import math


def f(*args) -> float:
  """ Object function """
  x, y = args if len(args) > 1 else args[0]

  return 2 * (x - 1) ** 2 + (y - 2) ** 3 + math.sqrt((x + 2) ** 2 + (y + 2) ** 2)


def penalty_f(x: float, y: float, k: float) -> float:
  """ Object function with penalty term """
  return f(x, y) + k / 2 * (1 / x + 1 / (4 - x) + 1 / y + 1 / (y - 4))


def gradient(x: float, y: float) -> tuple[float, float]:
  """ Get both gradient values of object function """
  dx = 4 * (x - 1) + (x + 2) / math.sqrt((x + 2) ** 2 + (y + 2) ** 2)
  dy = 3 * (y - 2) ** 2 + (y + 2) / math.sqrt((x + 2) ** 2 + (y + 2) ** 2)

  return dx, dy


def penalty_gradient(x: float, y: float, k: float) -> tuple[float, float]:
  """
  Get the gradient of function.
  Returns grad[f] if constrains satisfied else grad[f] + grad[penalty_f]
  """
  dx, dy = gradient(x, y)

  if 0 <= x <= 4 and 0 <= y <= 4:
    return dx, dy
  else:
    dx += (4 * k * (-2 + x)) / ((4 - x) ** 2 * x ** 2) if x != 0 else 0
    dy += k / 2 * (-1 / (-4 + y) ** 2 - 1 / y ** 2) if y != 0 else 0

    return dx, dy
