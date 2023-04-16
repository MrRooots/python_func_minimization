from src.functions import penalty_f, penalty_gradient, f
from src.methods import SteepestDescendMethod
from utils.plotter import Plotter
from utils.table_builder import TableBuilder
from utils.test_minimum import MinimumTester


class Solver:
  """
  Class provide solver for function minimization task
  using combination of three methods:
    1. Steepest Descent method
    2. Method of Interior Penalty Functions
    3. Dichotomy method
  """
  def __init__(self,
               x0: float,
               y0: float,
               k: float,
               alpha: float,
               precision: float) -> None:
    self.x0 = x0
    self.y0 = y0
    self.k = k
    self.alpha = alpha
    self.precision = precision
    self.table_builder = TableBuilder()

  def find_solution(self, max_iteration: int = 1000) -> None:
    """ Find solution for function minimization task """
    x, y, limit = SteepestDescendMethod.calculate(penalty_f,
                                                  penalty_gradient,
                                                  (self.x0, self.y0),
                                                  self.k,
                                                  self.alpha,
                                                  self.precision,
                                                  max_iteration)

    self.table_builder.add_data([
      max_iteration,
      limit,
      round(f(x, y), 5),
      (round(x, 5), round(y, 2))
    ])

  def generate_report(self,
                      table: bool = True,
                      graph: bool = True) -> None:
    """
    Generate table with calculations data and draw 3D plot of current function
    """
    self.table_builder.add_data([
      'Real minimum',
      'undefined',
      *MinimumTester.get_minimum(f, (0, 4), (0, 4))
    ])

    if table:
      self.table_builder.build_table()

    if graph:
      Plotter.draw_function(f, (0, 4), (0, 4))
