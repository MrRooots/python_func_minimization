from utils.solver import Solver

"""
1. Define the objective function f(x, y) = 2(x-1)^2+(y-2)^3+sqrt((x+2)^2+(y+2)^2).
2. Define the Interior Penalty Function method with a penalty parameter and a tolerance parameter. 
   This will ensure that the solution satisfies the constraints.
3. Initialize x and y to random values within the constraints (0 <= x <= 4, 0 <= y <= 4).
4. While the Interior Penalty Function method has not converged:
     a. Use the Interior Penalty Function method to update x and y.
5. Use the method of the steepest descent with the dichotomy method as a line search method 
   to fine-tune the solution and converge to a local minimum:
     a. Initialize the step size alpha to a small value.
     b. While the gradient of the objective function is greater than the tolerance parameter:
       i. Calculate the gradient of the objective function.
       ii. Calculate the optimal step size using the dichotomy method as a line search method.
       iii. Update x and y using the optimal step size and the gradient.
6. The final values of x and y are the solution that minimizes the objective function with the given constraints.
"""


def main():
  # Initial values of k and alpha is stringly paired with initial point (x0, y0)
  x0, y0 = 2, 2
  k, alpha, precision = 2.1, 1.15, 1e-8

  max_iterations = (10, 100, 500)  # , 1_000, 10_000, 50_000)
  solver = Solver(x0, y0, k, alpha, precision)

  for max_iteration in max_iterations:
    solver.find_solution(max_iteration)

  solver.generate_report()


if __name__ == '__main__':
  main()
