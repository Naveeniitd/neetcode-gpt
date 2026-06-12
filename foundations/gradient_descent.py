class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        x = float(init)
        for i in range(iterations):
            func_der = 2*x
            x = x - learning_rate*func_der

        return int(x) if iterations ==0 else round(x, 5)
